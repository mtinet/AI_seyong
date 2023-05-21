# -*- coding: utf-8 -*-


import os
import io
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from glob import glob
import time
import copy
import shutil
import cv2
from PIL import Image
import json, requests


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
import fractions
import base64




# ==================================================================================================
# Variables

with open('./config_server.json', 'rb') as f:
    config = json.loads(f.read().decode())


SERVER_IP = config['server_ip']
PORT = config['server_port']
REST_API_URL = 'http://{}:{}/analyze'.format(SERVER_IP, PORT)


try:
    WIDTH = config.get('client_width')
except:
    WIDTH = 1920

try:
    HEIGHT = config.get('client_height')
except:
    HEIGHT = 1400



# ==================================================================================================
# Class

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class MyComboBox(QComboBox):
    def __init__(self, parent=None, scrollWidget=None, *args, **kwargs):
        super(MyComboBox, self).__init__(parent, *args, **kwargs)
        self.scrollWidget=scrollWidget
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
    #
    def wheelEvent(self, *args, **kwargs):
        return





# =======================================================================================================
# Main Window
class SmartMartClient(QMainWindow):
    def __init__(self):
        super(SmartMartClient, self).__init__()
        try:
            # 윈도우 특성 설정
            self.setWindowTitle('SmartMart Client')  # 윈도우 타이클 지정
            self.setGeometry(0, 0, WIDTH, HEIGHT)  # 윈도우 위치/크기 설정
            # ===================================================================
            # Object
            self.frame1 = QFrame(self)
            self.frame1.setGeometry(QtCore.QRect(0, 0, WIDTH, HEIGHT))
            self.frame1.setFrameShape(QFrame.StyledPanel)
            self.frame1.setFrameShadow(QFrame.Raised)
            #
            # File Open
            self.btn_filebox = QPushButton('File Select', self.frame1)
            self.btn_filebox.setGeometry(QtCore.QRect(0, 0, 100, 30))
            self.btn_filebox.clicked.connect(self.open_filebox)
            self.DATA_PATH = './'
            #
            #
            # Result
            self.label_result = QLabel('Result', self.frame1)
            self.label_result.setGeometry(QRect(10, 30, WIDTH - 20, 60))
            #
            self.label_img = QLabel('Worked Image', self.frame1)
            self.label_img.setGeometry(QRect(10, 100, WIDTH - 20, HEIGHT - 110))
            #
        except Exception as ex:
            print(str(ex))
    #
    # ==================================================================================================
    def open_filebox(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'OpenFile', self.DATA_PATH)
            file_path, _ = fname
            if file_path is None or file_path == '' or len(file_path.split('/')) < 2:
                return
            # ---------------------------------------------------------------------
            # 절대경로 -> 상대경로로 바꾸기
            file_path = os.path.relpath(file_path, os.getcwd()).replace('\\', '/')
            print('relative_path:', file_path)
            self.label_result.setText('...waiting server result')
            # ---------------------------------------------------------------------
            file_name = file_path.split('/')[-1]
            self.DATA_PATH = file_path.replace(file_name, '')
            #
            files = []
            files.append(
                ('files', (file_name, open(file_path, 'rb'), 'multipart/form-data'))
            )
            response = requests.request("POST", REST_API_URL, files=files, verify=False)
            self.label_result.setText(str(response.json()))
            #
            #
            print('img_url:', response.json().get('image'))
            response = requests.get(response.json().get('image'))
            img_pil = Image.open(io.BytesIO(response.content)).convert('RGB')
            img_np = np.array(img_pil)
            height, width = img_np.shape[: 2]
            if width > (WIDTH - 20):
                img_np = cv2.resize(img_np, ((WIDTH - 20), int(height * (WIDTH - 20) / width)))
                height, width = img_np.shape[: 2]
            #
            if height > (HEIGHT - 110):
                img_np = cv2.resize(img_np, (int(width * (HEIGHT - 110) / height), (HEIGHT - 110)))
            #
            #
            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            img_dst = Image.fromarray(img_np)
            data = img_dst.convert("RGBA").tobytes("raw", "RGBA")
            qimage = QtGui.QImage(data, img_dst.size[0], img_dst.size[1], QtGui.QImage.Format_ARGB32)
            pixmap = QPixmap.fromImage(qimage)
            self.label_img.setPixmap(pixmap)
            #
        except Exception as ex:
            print(str(ex))





# =======================================================================================================
def main():
    app = QApplication(sys.argv)
    win = SmartMartClient()
    win.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()


# exe파일 생성용
# pyinstaller --onefile smartM_client.py --hidden-import='sklearn.utils._cython_blas' --hidden-import='sklearn.neighbors.typedefs' --hidden-import='sklearn.neighbors.quad_tree' --hidden-import='sklearn.tree._utils'

