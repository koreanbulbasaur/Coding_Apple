import tensorflow as tf

tensor = tf.constant([1, 2, 3])
# print(tensor)

tensor2 = tf.constant([4, 5, 6])
# print(tensor + tensor2)

tensor3 = tf.constant([[1, 2], [3, 4]])
# print(tf.add(tensor, tensor2))

tensor4 = tf.zeros(10)
# print(tensor4)

tensor4_2 = tf.zeros([2, 2])
# print(tensor4_2)

tensor4_3 = tf.zeros([2, 2, 3])
# print(tensor4_3)

w = tf.Variable(1.0)
print(w)
print(w.numpy())

w.assign(2)
print(w)