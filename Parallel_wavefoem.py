import numpy as np
import math
import matplotlib.pyplot as plt
from Generate_files import *

def _privateParallel_difference(formant, gain, A, B, C):
    '''
    Args:
    formant: int, the nth formant
    gain: list, amplitude control
    A, B, C: list, 3 coefficients

    Retruns: list, amplitude value for each 1 ms
    '''
    assert isinstance(A, list) and isinstance(B, list) and isinstance(C, list) and isinstance(gain, list)
    output = []
    index = formant - 1

    # impulse_train, altogether 100 ms, an impulse / 10 ms, namely 100 Hz for f0
    imp = [0, 0, 1000]  # predefine amplitude at -2, -1, 0 ms
    for _ in range(100):  # 10 ms/impulse
        for _ in range(99):  # 1 ms = 1 sample
            imp.append(0)
        imp.append(1000)  # adjust impulse train

    output = [0] * 4003  # initialize output list with 1003 zeros
    for i in range(4001):  # let normal voicing go through resonator
        output[i + 2] = A[index] * gain[index] * imp[i + 1] + B[index] * output[i + 1] + C[index] * output[i]
    return output


def parallel_waveform(vowel, gain, f_n, b_n):
    '''
    Args:
    vowel: str, vowel name
    f_n: list, cutoff frequency (F)
    b_n: list, bandwidth (BW)

    Retruns: 
    waveform graph, amplitude list in linear scale
    '''
    assert isinstance(f_n, list) and isinstance(b_n, list)
    f_s = 10000  # int, sampling frequency (Fs): 10 kHz
    t_s = 1 / f_s  # float, sampling period (Ts) = 1/sampling frequency = 0.1 ms
    time = np.arange(-0.2, 100.1, t_s * 1000)  # waveform length: 100.2 ms

    # compute sigma, omega
    sigma, omega = [], []
    for i in range(len(f_n)):
        sigma.append(-np.pi * b_n[i])
        omega.append(2 * np.pi * f_n[i])

    # compute A,B,C
    A, B, C = [], [], []
    for i in range(len(f_n)):
        C.append(-math.exp(2 * sigma[i] * t_s))
        B.append(2 * math.exp(sigma[i] * t_s) * np.cos(omega[i] * t_s))
        A.append(1 - B[i] - C[i])

    # # first order low-pass filter
    # B.append(math.exp(-2 * math.pi * 100 * t_s))
    # A.append(1 - B[3])

    # waveform of 3 formant resonators in cascade
    output_1 = _privateParallel_difference(1, gain, A, B, C)
    output_2 = _privateParallel_difference(2, gain, A, B, C)
    output_3 = _privateParallel_difference(3, gain, A, B, C)

    output = []
    for i in range(len(output_1)):
        output.append(output_1[i] - output_2[i] + output_3[i])
    
    # plot wave for vowel
    plot_parallel_waveform_for_vowel(time, output,vowel)
    return output
