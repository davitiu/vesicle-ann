import numpy as np

def encapsulate_memory_block(input_data, mode='keyed', key=42):
    if mode == 'keyed':
        np.random.seed(key)
        noise = np.random.normal(0, 0.01, size=input_data.shape)
        encoded = input_data + noise
    elif mode == 'noise_filter':
        threshold = np.mean(input_data)
        encoded = np.where(input_data > threshold, input_data, 0)
    elif mode == 'scale_compress':
        encoded = input_data / (np.max(input_data) + 1e-8)
    else:
        encoded = input_data
    return encoded
