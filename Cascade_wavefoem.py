import numpy as np
import math
import matplotlib.pyplot as plt
from Generate_files import *

def _private_cas_difference2(formant, inp, A, B, C):
    '''
    Args:
    formant: int, the nth formant
    inp: list, input value
    A, B, C: list, 3 coefficients

    Returns: list, amplitude value for each 1 ms
    '''
    assert isinstance(inp, list) and isinstance(A, list) and isinstance(B, list) and isinstance(C, list)
    n = len(inp)
    output = [0] * (n + 2)  # initialize output with 0s

    for i in range(2, n + 2):
        output[i] = A[formant-1] * inp[i-2] + B[formant-1] * output[i-1] + C[formant-1] * output[i-2]
    
    return output[2:]  # remove first two values of output

def _private_cas_difference(formant, inp, A, B, C):
    '''
    Args:
    formant: int, the nth formant
    inp: list, input value
    A, B, C: list, 3 coefficients

    Retruns: list, amplitude value for each 1 ms
    '''
    assert isinstance(inp, list) and isinstance(A, list) and isinstance(B, list) and isinstance(C, list)
    output = []
    index = formant - 1
    for i in range(4003):
        output.append(0)
    for i in range(4001):
        output[i + 2] = A[index] * inp[i + 1] + B[index] * output[i + 1] + C[index] * output[i]
    return output


def cas_lp_filter(formant, inp, A, B, C):
    '''
    Args:
    formant: int, the nth formant
    inp: list, input value
    A, B, C: list, 3 coefficients

    Retruns: list, amplitude value for each 1 ms
    '''
    assert isinstance(inp, list) and isinstance(A, list) and isinstance(B, list) and isinstance(C, list)
    output = []
    index = formant - 1
    for i in range(1003):
        output.append(0)
    for i in range(1001):
        output[i + 2] = A[index] * inp[i + 2] + B[index] * output[i + 1]
    return output


def cascade_waveform(vowel, f_n, b_n):
    '''
    Args:
    vowel: str, vowel name
    f_n: list, cutoff frequency (F)
    b_n: list, bandwidth (BW)

    Retruns: 
    waveform graph, amplitude list in V
    '''
    assert isinstance(f_n, list) and isinstance(b_n, list)
    f_s = 10000  # int, sampling frequency (Fs): 10 kHz
    t_s = 1 / f_s  # float, sampling period (Ts) = 1/sampling frequency = 0.1 ms
    time = np.arange(-0.2, 100.1, t_s * 1000)  # waveform length: 100.2 ms

    # compute sigma, omega
    sigma, omega = [], []
    for i in range(5):
        sigma.append(-np.pi * b_n[i])
        omega.append(2 * np.pi * f_n[i])

    # compute A,B,C
    A, B, C = [], [], []
    for i in range(5):
        C.append(-math.exp(2 * sigma[i] * t_s))
        B.append(2 * math.exp(sigma[i] * t_s) * np.cos(omega[i] * t_s))
        A.append(1 - B[i] - C[i])

    # # first order low-pass filter
    # B.append(math.exp(-2 * math.pi * 100 * t_s))
    # A.append(1 - B[5])

    # impulse_train, altogether 100 ms, an impulse / 10 ms, namely 100 Hz for f0
    impulse_train = [0, 0, 1000]  # predefine amplitude at -2, -1, 0 ms
    for impulse in range(100):  # 10 ms/impulse
        for interval in range(99):  # 1 ms = 1 sample
            impulse_train.append(0)
        impulse_train.append(1000)  # 1000/impulse

    # waveform of five formant resonator in cascade
    output_1 = _private_cas_difference(1, impulse_train, A, B, C)
    output_2 = _private_cas_difference(2, output_1, A, B, C)
    output_3 = _private_cas_difference(3, output_2, A, B, C)
    output_4 = _private_cas_difference(4, output_3, A, B, C)
    output_5 = _private_cas_difference(5, output_4, A, B, C)
    
    # plot wave for vowel
    plot_cascade_waveform_for_vowel(time, output_5, vowel)

    return output_5
