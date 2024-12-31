import cv2
import numpy as np
import scipy.io.wavfile as wavefile
from scipy.signal import wiener

fs , noisy_signal = wavefile.read('noisy_audio.wav',cv2.IMREAD_GRAYSCALE)
noisy_signal = noisy_signal / np.max(np.abs(noisy_signal))

filtered_signal = wiener(noisy_signal , noise=1e-1)
filtered_signal = (filtered_signal * 32726).astype(np.int16)
wavefile.write("Filtered" , fs , filtered_signal)