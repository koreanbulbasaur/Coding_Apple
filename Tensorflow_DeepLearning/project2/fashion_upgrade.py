import os, sys
current_dir = os.path.dirname(os.path.abspath("module.py"))
sys.path.append(current_dir)
from module import *

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

# 이미지 데이터 전처리 0~255 -> 0~1로 압축해서 넣음
X_train = X_train / 255.0
X_test = X_test / 255.0

# 4차원으로 바꿈
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt',
               'Sneaker', 'Bag', 'Ankleboot']

model = Sequential([
    Conv2D(32, (3, 3), padding="same", activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    # Dense(128, input_shape=(28, 28), activation='relu'),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax'), # 결과를 0~1으로 압축(카테고리 예측문제에 사용)
])

model.summary()

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, validation_data=(X_test, y_test),epochs=5)