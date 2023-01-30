import tensorflow as tf

print("TENSORFLOW M1/M2 devices: " + str(tf.config.list_physical_devices('GPU')))
print("TENSORFLOW CPU devices: " + str(tf.config.list_physical_devices('CPU')))