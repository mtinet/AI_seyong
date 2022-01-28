import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# imagenet에 미리 훈련된 ResNet50 모델 불러오기
model = ResNet50(weights='imagenet')
model.summary()

# 테스트할 이미지 불러오기
img_path = 'test1.jpg'
img = load_img(img_path, target_size=(224, 224))

# ResNet에 입력하기 전에 이미지 전처리
x = img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# 이미지 분류
preds = model.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])
