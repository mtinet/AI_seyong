
# /usr/bin/env python



import os
import copy
import time
import datetime
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt
import json
import random
import easydict
from flask import Flask, request, render_template, session, redirect, url_for, send_file




import torch
from torchvision import transforms
import torch.nn as nn
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader


from models.experimental import attempt_load
from utils.datasets import LoadImages, LoadStreams
from utils.general import apply_classifier, check_img_size, check_imshow, check_requirements, check_suffix, colorstr, \
    increment_path, non_max_suppression, print_args, save_one_box, scale_coords, set_logging, \
    strip_optimizer, xyxy2xywh
from utils.plots import Annotator, colors
from utils.torch_utils import load_classifier, select_device, time_sync
from utils.augmentations import Albumentations, augment_hsv, copy_paste, letterbox, mixup, random_perspective





# ----------------------------------------------------------------------------------------
# configuration

import json
with open('./config_server.json', 'rb') as f:
    config = json.loads(f.read().decode())



SERVER_IP = config.get('server_ip')
SERVER_PORT = config.get('server_port')


UPLOAD_DIR = config.get('upload_dir')
os.makedirs(UPLOAD_DIR, exist_ok=True)


SAVE_DIR = config.get('save_dir')
os.makedirs(SAVE_DIR, exist_ok=True)


# 로그파일 Writer 생성
LOG_DIR = 'logs/'
os.makedirs(LOG_DIR, exist_ok=True)


LABELS = config.get('labels')
LABELS.sort()


L_MARGIN = config.get('left_margin')
R_MARGIN = config.get('right_margin')



# ============================================================================================
# GPU Setting

os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
os.environ['CUDA_VISIBLE_DEVICES'] = config.get('gpu_nums')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')




# =========================================================================================================
# Functions

def _is_box1_overlap_box2(box1, box2, overlap_ratio=0.5):
    overlap = False
    try:
        b1_x1, b1_y1, b1_x2, b1_y2 = box1[: 4]
        b1_wid = b1_x2 - b1_x1
        b1_hei = b1_y2 - b1_y1
        if b1_wid * b1_hei == 0:
            return overlap
        b2_x1, b2_y1, b2_x2, b2_y2 = box2[: 4]
        b2_wid = b2_x2 - b2_x1
        b2_hei = b2_y2 - b2_y1
        #
        # -------------------------------------------------------
        overlap_wid = np.max([0, b1_wid + b2_wid - ( np.max([b1_x2, b2_x2]) - np.min([b1_x1, b2_x1]) )])
        overlap_hei = np.max([0, b1_hei + b2_hei - (np.max([b1_y2, b2_y2]) - np.min([b1_y1, b2_y1]))])
        #
        # print('\t\toverlap_ratio:', (overlap_wid * overlap_hei) / (b1_wid * b1_hei))
        if (overlap_wid * overlap_hei) / (b1_wid * b1_hei) > overlap_ratio:       # box1 ����
            overlap = True
    except Exception as ex:
        error = 1
    return overlap





# ==========================================================================================
# Detection Model

MODEL_DIR = config.get('model_dir')
MODEL_DETECTOR = config.get('model_detector')


import easydict
opt = easydict.EasyDict({
    'imgsz': [640, 640],
    'conf_thres': 0.1,
    'iou_thres': 0.4,
    'max_det': 1000,
    'view_img': True,
    'save_txt': False,
    'save_conf': False,
    'save_crop': False,
    'nosave': False,
    'classes': None,
    'agnostic_nms': False,
    'augment': True,
    'visualize': False,
    'update': False,
    'exist_ok': True,
    'line_thickness': 3,
    'hide_labels': False,
    'hide_conf': False
})




# with torch.no_grad():
imgsz = opt.imgsz
conf_thres = opt.conf_thres
iou_thres = opt.iou_thres
max_det = opt.max_det
view_img = opt.view_img
save_txt = opt.save_txt
save_conf = opt.save_conf
save_crop = opt.save_crop
nosave = opt.nosave
classes = opt.classes
agnostic_nms = opt.agnostic_nms
augment = opt.augment
visualize = opt.visualize
update = opt.update
exist_ok = opt.exist_ok
line_thickness = opt.line_thickness
hide_labels = opt.hide_labels
hide_conf = opt.hide_conf



detector = attempt_load(MODEL_DIR + MODEL_DETECTOR, map_location=device)  # load FP32 model
detector = detector.to(device)
stride = int(detector.stride.max())  # model stride
names = detector.module.names if hasattr(detector, 'module') else detector.names  # get class names
print(names)



# ==========================================================================================
# Classification Model

MODEL_DIR = config.get('model_dir')
MODEL_CLASSIFIER = config.get('model_classifier')


# Evaluate model
print('---Classifier')
classifier = torch.load(MODEL_DIR + MODEL_CLASSIFIER)
classifier = classifier.to(device)
classifier = classifier.eval()



# transform
pixel_mean, pixel_std = 0.66133188,  0.21229856
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([pixel_mean] * 3, [pixel_std] * 3)
])




# ================================================================================================
# 웹서버 기본 모듈 생성

app = Flask(__name__)
app.secret_key = 'any random string'
with app.app_context():
    print(app.name)



# CORS정책 (필요시에만)
if False:
    from flask_cors import CORS, cross_origin
    CORS(app)
    # CORS(app, resources={r'*': {'origins': '*'}})
    # CORS(app, resources={r'*': {'origins': 'http://3.35.2.241/'}})
    # CORS(app, resources={r'/_api/*': {'origins': 'https://webisfree.com:5000'}})




# ================================================================================================
# 웹서버 functions 정의
@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    start = time.time()
    LOG_FILE = LOG_DIR + 'log_{}.txt'.format(datetime.datetime.now().strftime('%Y%m%d'))
    Logger = open(LOG_FILE, 'a', encoding='utf-8')
    print('\t로그파일생성시간: ', time.time() - start)
    mid = time.time()

    #
    #
    filename = ''
    results = ''
    msg = ''
    image = ''
    analizingTimeCheck = ''
    result_dict = {
        'filename': filename,
        'result': results,
        'image': image,
        'msg': msg,
        'analizingTimeCheck' : analizingTimeCheck
    }
    #
    if request.method == 'POST':
        try:
            up_file = request.files['files']
            filename = up_file.filename
            ext = filename.split('.')[-1]
            print('filename:', filename)
            up_path = UPLOAD_DIR + '{}'.format(filename)
            up_file.save(up_path)
            #
            print('\t파일저장시간: ', time.time() - mid)
            mid = time.time()
            # -------------------------------------------------------------
            # Image or Video
            # 1. Image
            if ext.lower() in ['jpg', 'png']:
                print('\tImage', up_path)
                img_pil = Image.open(up_path).convert('RGB')
                img_ori = np.array(img_pil)
            #
            elif ext.lower() in ['mp4']:
                # ----------------------------------------------------------
                # 이미지 연결
                vidcap = cv2.VideoCapture(up_path)  # Sample Video File
                FPS = vidcap.get(cv2.CAP_PROP_FPS)
                print('\tVideo:', up_path, ', fps:', FPS)
                #
                success, img = vidcap.read()  # first frame (720, 1280)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # ---------------------------------------
                # Margin cut
                # img = img[:, 384: -346]  # 1650
                img = img[:, L_MARGIN: -R_MARGIN]
                # ---------------------------------------
                height, width = img.shape[: 2]
                print('\tafter margin cut:', height, width)  # (1080, 1190)
                img_half = img[: height // 2, :]
                #
                # -------------------------------------
                if True:
                    img = cv2.flip(img, 1)
                else:
                    img_half = img[: height // 2, :]
                    img_half_flip = cv2.flip(img_half, 1)
                    img[: height // 2, :] = img_half_flip
                # -------------------------------------
                #
                # CYCLE_TIME = 6   # 전체 다
                VID_LENGTH = vidcap.get(cv2.CAP_PROP_FRAME_COUNT) // FPS
                # INTERVAL = 0.04   # 초
                INTERVAL = 0.0337      # 초
                # INTERVAL = 1 / FPS
                cnt_frame = 0
                cnt_captures = 0
                #
                img_merge = img
                while success:
                    # -------------------------------------------------------
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = img[:, L_MARGIN: -R_MARGIN]
                    height, width = img.shape[: 2]
                    # -------------------------------------
                    if True:
                        img = cv2.flip(img, 1)
                    else:
                        img_half = img[: height // 2, :]
                        img_half_flip = cv2.flip(img_half, 1)
                        img[: height // 2, :] = img_half_flip
                    # -------------------------------------
                    #
                    # -------------------------------------------------------
                    # Image Stitch
                    # - 연결할 이미지
                    img = img[:, int(width / (VID_LENGTH / INTERVAL)):]
                    hei, wid = img.shape[: 2]
                    #
                    wid_move = width - wid
                    temp_merge = np.zeros((height, img_merge.shape[1] + wid_move, 3), dtype='uint8')
                    temp_merge[:, : img_merge.shape[1]] = img_merge
                    temp_merge[:, -wid:] = np.array(img)
                    img_merge = temp_merge
                    #
                    # -------------------------------------------------------
                    # read img
                    success, img = vidcap.read()
                    cnt_captures += 1
                    cnt_frame += 1
                vidcap.release()
                img_ori = img_merge
            #
            print('\t이미지처리시간: ', time.time() - mid)
            mid = time.time()
            # ---------------------------------------------------------------------------
            img_box = copy.deepcopy(img_ori)
            save_path = SAVE_DIR + filename.replace('.mp4', '.png')
            #
            #
            img = letterbox(img_ori, imgsz, stride)[0]  # (384, 640, 3)
            img = img.transpose((2, 0, 1))  # already RGB
            #
            #
            # Run inference
            hei_ori, wid_ori = img_ori.shape[: 2]
            img = torch.from_numpy(img).to(device)
            img = img / 255.0  # 0 - 255 to 0.0 - 1.0
            if len(img.shape) == 3:
                img = img[None]  # expand for batch dim
            #
            #
            # Inference
            with torch.no_grad():
                preds = detector(img)[0]  # 15120
            #
            #
            preds = non_max_suppression(preds, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)
            preds[0][:, :4] = scale_coords(img.shape[2:], preds[0][:, : 4], img_ori.shape).round()
            preds = preds[0].cpu().numpy()
            #
            print('\tDetection시간: ', time.time() - mid)
            mid = time.time()
            #
            #
            # Total boxes
            boxes = []
            for index, pred in enumerate(preds):
                x1, y1, x2, y2, conf, c_index = pred
                x1, y1, x2, y2, c_index = int(x1), int(y1), int(x2), int(y2), int(c_index)
                boxes.append([x1, y1, x2, y2, (x1 + x2) // 2, (y1 + y2) // 2, c_index])
            # -------------------------------------------------------------
            boxes.sort(key=lambda k: k[4])  # center_x 좌표순에 따라 sort
            # -------------------------------------------------------------
            #
            top_list = []
            bot_list = []
            results = []
            for b1 in range(len(boxes)):
                box = boxes[b1]
                x1, y1, x2, y2 = box[: 4]
                # ----------------------------------------------------
                # 가장자리 잘린 제품 무시
                if (x1 <= 2 and x2 < wid_ori / 15) or (x1 >= wid_ori * 14 / 15 and x2 >= wid_ori - 2):
                # if (x1 <= 5) or (x2 >= wid_ori - 5):
                    msg = msg.replace('사이드에 걸친 제품이 있습니다.', '') + ' ' + '사이드에 걸친 제품이 있습니다.'
                    img_box = cv2.rectangle(img_box, (x1, y1), (x2, y2), (255, 0, 0), 1)
                    continue
                # ----------------------------------------------------
                img_copy = copy.deepcopy(img_ori)
                INNER_BOX = False
                for b2 in range(len(boxes)):
                    if b1 == b2:  # 자기 자신은 제외
                        continue
                    o_box = boxes[b2]
                    o_x1, o_y1, o_x2, o_y2 = o_box[: 4]
                    o_hei, o_wid = o_box[4: 6]
                    if _is_box1_overlap_box2(box[: 4], o_box[: 4], 0.9):
                        INNER_BOX = True
                        break
                #
                if INNER_BOX:
                    print('\tfound Inner box')
                    continue
                #
                # ----------------------------------------------------
                # Classification
                crop = img_copy[y1: y2, x1: x2]
                #
                #
                crop_pil = Image.fromarray(crop).convert('RGB')
                crop_tensor = preprocess(crop_pil)
                crop_tensor = Variable(crop_tensor.unsqueeze(0))
                crop_tensor = crop_tensor.to(device)
                #
                #
                # Forward
                with torch.no_grad():
                    output = classifier(crop_tensor)
                #
                output = nn.Sigmoid()(output)
                score, pred_index = torch.max(output.data, 1)
                score = score.cpu().numpy()[0]
                score = np.round(score, 3).astype('float')
                pred_index = np.array(pred_index.cpu())[0]
                pred_name = LABELS[pred_index]
                #
                # ------------------------------------------------------------------------------
                # Top, Bottom 분류
                # if y2 < hei_ori // 2:     # y2가 half를 넘어서는 경우가 있음
                if (y1 + y2) // 2 < hei_ori // 2:
                    top_list.append([x1, y1, x2, y2, (x1 + x2) // 2, (y1 + y2) // 2, pred_name, score])
                else:
                    bot_list.append([x1, y1, x2, y2, (x1 + x2) // 2, (y1 + y2) // 2, pred_name, score])
                #
                # ------------------------------------------------------------------------------
                # Save
                save_dir_crop = SAVE_DIR + '{}/'.format(pred_name)
                os.makedirs(save_dir_crop, exist_ok=True)
                crop_pil.save(save_dir_crop + '{}_c{}.png'.format(filename, '%03d' % index))
                # print('\t', b1, x1, y1, x2, y2, pred_index, pred_name, score)
                # print('\t', time.time() - start)
                #
                # label = '{}({})'.format(pred_name, str(score))
                label = '{}({})'.format(pred_name, '%.3f' % score)
                if pred_name not in ['_no_target']:
                    img_box = cv2.rectangle(img_box, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    img_box = cv2.rectangle(img_box, (x1, y1), (x2, y1 + 20), (0, 0, 0), -1)
                    # ----------------------------------------------------------------
                    try:
                        fontpath = config.get('font_path')  # "fonts/gulim.ttc"        # windows
                        # fontpath = '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'    # ubuntu
                        # ----------------------------------------------------------------
                        font = ImageFont.truetype(fontpath, 18)
                        img_box_pil = Image.fromarray(img_box)
                        draw = ImageDraw.Draw(img_box_pil)
                        draw.text((x1, y1), label, font=font, fill=(235, 235, 235, 0))
                        # img_box = cv2.putText(img_box, screen_label, (x1, y1_text + 15), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0, 0), 2)
                        img_box = np.array(img_box_pil)
                    except Exception as ex:
                        print(str(ex))
                else:
                    img_box = cv2.rectangle(img_box, (x1, y1), (x2, y2), (255, 0, 0), 2)
                print('\tClassification시간: ', b1, time.time() - mid)
                mid = time.time()

            # analizing time check
            accum_time = 0
            accum_time = time.time() - start
            analizingTimeCheck = f'인식속도(초) {round(float(accum_time),3)}\n'
            print(analizingTimeCheck)
            #
            #
            # Save results (image with detections)
            dst_pil = Image.fromarray(img_box)
            dst_pil.save(save_path)
            image = 'http://{}:{}/{}'.format(SERVER_IP, SERVER_PORT, save_path)
            #
            #
            # -----------------------------------------------------------------------
            # 결과값 저장
            for bot in bot_list:
                bx1, by1, bx2, by2, bcen_x, bcen_y, bpred, bscore = bot
                print('pred:', bpred)
                results.append([bpred, np.round(bscore, 3)])
            for bot in top_list:
                tx1, ty1, tx2, ty2, tcen_x, tcen_y, tpred, tscore = bot
                print('pred:', tpred)
                results.append([tpred, np.round(tscore, 3)])

            #
            # ------------------------------------------------------------------------
            #  개수체크
            if len(bot_list) != len(top_list):
                msg = msg + ' ' + f'Top리스트는 {len(top_list)}, Bottom리스트는 {len(bot_list)}개 입니다.'
            # -----------------------------------------------------------------------
            result_dict = {
                'filename': filename,
                'results': results,
                'image': image,
                'msg': msg,
                'analizingTimeCheck' : analizingTimeCheck
            }
        except Exception as ex:
            print(str(ex))
            result_dict = {
                'filename': filename,
                'results': results,
                'image': image,
                'msg': '알 수 없는 에러가 발생하였습니다.',
                'analizingTimeCheck' : analizingTimeCheck
            }
    #
    Logger.write('\n{}: {}, Total time: {}'.format( datetime.datetime.now(), str(result_dict), (time.time() - start) ))
    Logger.flush()
    # print('\tTotal시간: ', time.time() - start)
    return json.dumps(result_dict, ensure_ascii=False).encode('utf8')






# ================================================================================================
# Flask web 실행

if __name__ == "__main__":
    app.run(host=SERVER_IP, port=SERVER_PORT)
    # ---------------------------------------
    print('\nGood Bye~\n\n')



# 일반용
# nohup python smartM_ai_server.py   output.log 2&1


# exe파일 생성용
# pyinstaller --onefile smartM_ai_server.py --hidden-import='sklearn.utils._cython_blas' --hidden-import='sklearn.neighbors.typedefs' --hidden-import='sklearn.neighbors.quad_tree' --hidden-import='sklearn.tree._utils'
