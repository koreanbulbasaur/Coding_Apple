import tensorflow as tf

height = 195
shoes = 300

a = tf.Variable(0.1)
b = tf.Variable(0.2)

def loss():
    actual_value = shoes
    predicted_value = height * a + b
    return tf.square(actual_value - predicted_value)

opt = tf.keras.optimizers.Adam(learning_rate=0.1)

cycle = 300

for i in range(cycle):
    opt.minimize(loss, var_list=[a, b])
print(f'{cycle}번 :', a.numpy(),'/', b.numpy())