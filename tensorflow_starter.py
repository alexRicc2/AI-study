import tensorflow as tf  # now import the tensorflow module
print(tf.version)
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)

# print(tf.rank(rank2_tensor))
matriz = tf.ones([5,5,5,5])
print(matriz)
matriz_reshaped = tf.reshape(matriz, [625])
print(matriz)
# -1 argument lets tensorflow calculates what should be the level of it
matriz_auto_reshaped = tf.reshape(matriz, [5, -1])
print(matriz_auto_reshaped)
print("shape:",matriz_auto_reshaped.shape)