import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv(r'Tensorflow_DeepLearning\project1\gpascore.csv')

data = data.dropna() # 빈 값인 해당 행을 삭제함

y_data = data['admit'].values
x_data = []

for i, rows in data.iterrows():
    x_data.append([rows['gre'], rows['gpa'], rows['rank']])

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(np.array(x_data), np.array(y_data), epochs=1000, verbose=0)

# 예측
pred_v = model.predict([[750, 3.70, 3], [400, 2.2, 1]])
print(pred_v)