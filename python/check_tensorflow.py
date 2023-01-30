import tensorflow as tf

print("TENSORFLOW CUDA devices: " + str(tf.config.list_physical_devices('GPU')))

# deprecated
# if tf.test.is_gpu_available():
#     print("TENSORFLOW CUDA devices: " + str(tf.config.list_physical_devices('GPU')))
# else:
#     print(":(")