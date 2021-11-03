import tensorflow as tf


# Get GPUs and ensure use only as much memory as needed
gpus = tf.config.list_physical_devices("GPU")
# tf.config.set_visible_devices(gpus[0], "GPU") Can use this instead of export CUDA_VISIBLE_DEVICES
tf.config.experimental.set_memory_growth(gpus[0], True)

# Test CUDA launched correctly
a = tf.constant(1)
print(f"\nFound gpus: {gpus}")

