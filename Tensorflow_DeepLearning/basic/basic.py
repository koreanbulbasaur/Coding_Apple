import tensorflow as tf

height = 170
shoes = 260

a = tf.Variable(0.1)
b = tf.Variable(0.2)

def loss_f():
    return tf.square(shoes - (height * a + b))

opt = tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(300):
    opt.minimize(loss_f, var_list=[a, b])
    print(a.numpy(), b.numpy())