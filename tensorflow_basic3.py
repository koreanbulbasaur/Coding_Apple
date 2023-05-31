import tensorflow as tf

train_x = list(range(1, 8))
train_y = list(range(3, 16, 2))

a = tf.Variable(0.1)
b = tf.Variable(0.1)

def loss():
    pred_y = train_x * a + b
    return tf.keras.losses.mse(train_y, pred_y)

opt = tf.keras.optimizers.Adam(learning_rate=0.01)

cycle = 2500

for i in range(cycle):
    opt.minimize(loss, var_list=[a, b])
    print(f'{i}번 :', a.numpy(),'/', b.numpy())