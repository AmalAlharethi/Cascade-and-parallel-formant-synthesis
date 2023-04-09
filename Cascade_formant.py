import numpy as np
import math
from Generate_files import *

# amplitude response
def _private_cascadeAmplitudeResponse(A, B, C, omega_Hz, array, formant, t_s):
    '''
    Args:
    A, B, C: list, 3 coefficients
    omega_Hz: float, angular frequency, = 2*pi*frequency
    array: array, to store result
    formant: int, forman number, 1-5
    t_s: float, sampling period Ts

    Retruns:
    int, amplitude values in dB for every frequency
    '''

    assert isinstance(array, np.ndarray) # formant resonator, frequency domain...
    for i in range(5000):
        # calculate intermediate variables
        cos_term = (1 - C[formant]) * np.cos(omega_Hz[i] * t_s) - B[formant]
        sin_term = (1 + C[formant]) * np.sin(omega_Hz[i] * t_s)
        amplitude = A[formant] / np.sqrt(cos_term**2 + sin_term**2)
        # convert amplitude to dB and store in array
        array[0][i] = 20 * np.log10(amplitude).reshape(1, -1)
    
    return array


# phase response
def _private_cascadePhaseResponse(A, B, C, omega_Hz, array, formant, t_s):
    '''
    Args:
    A, B, C: list, 3 coefficients
    omega_Hz: float, angular frequency, = 2*pi*frequency
    array: array, to store result
    formant: int, formant number, 1-5
    t_s: float, sampling period Ts

    Retruns: int, phase values in degree for every frequency
    '''
    assert isinstance(array, np.ndarray)
    for i in range(5000):
        # calculate intermediate variables
        cos_term = (1 - C[formant]) * np.cos(omega_Hz[i] * t_s) - B[formant]
        sin_term = (1 + C[formant]) * np.sin(omega_Hz[i] * t_s)
        phase = -np.arctan2(sin_term, cos_term)

        # convert phase to degrees and store in array
        array[0][i] = (phase * 180 / np.pi).reshape(1, -1)
    return array

# frequency response
def cascade_frequency_response(vowel, f_n, b_n):
    '''
    Args:
    vowel: str, vowel name
    f_n: list, cutoff frequency (F)
    b_n: list, bandwidth (BW)

    Retruns:
    amplitude response graph, phase response graph, amplitude response array, phase response array
    '''
    assert isinstance(f_n, list) and isinstance(b_n, list) 
    f_step = 1  # int, frequency step
    f_s = 10000  # int, sampling frequency (Fs): 10 kHz
    f_Hz = np.arange(0, 5000, f_step)  # array, frequency range(0Hz,5000Hz), with frequency step 1 Hz, altogether 5000 samples
    omega_Hz = 2 * math.pi * f_Hz  # array, angular frequency = 2*pi*f
    t_s = 1 / f_s  # float, sampling period (Ts) = 1/sampling frequency = 0.1 ms = 0.0001 s


#transfer function equation @mal
    # compute sigma & omega
    sigma, omega = [], []
    for i in range(5):
        sigma.append(-np.pi * b_n[i])  # σ = -pi*BW
        omega.append(2 * np.pi * f_n[i])  # ω = 2*pi*F

    # compute A,B,C
    A, B, C = [], [], []
    for i in range(5):
        C.append(-math.exp(2 * sigma[i] * t_s))  # C = -exp(-2*pi*BW*Ts) = -exp(2*σ*Ts)
        B.append(2 * math.exp(sigma[i] * t_s) * np.cos(omega[i] * t_s))  # B = 2*exp(-pi*BW*Ts)*cos(2*pi*F*Ts) = 2*exp(σ*Ts)*cos(ω*Ts)
        A.append(1 - B[i] - C[i])  # A = 1- B - C

    # # # first order low-pass filter @mal
    # B.append(math.exp(-2 * math.pi * 100 * t_s))
    # A.append(1 - B[5])

    # Frequency domain eqs (amplitude and phase responses) @mal

    # create arrays for storing amplitude response of 5 formants        
    amp_1 = np.empty([1, 5000], dtype=float)
    amp_2 = np.empty([1, 5000], dtype=float)
    amp_3 = np.empty([1, 5000], dtype=float)
    amp_4 = np.empty([1, 5000], dtype=float)
    amp_5 = np.empty([1, 5000], dtype=float)

    # compute amplitude response of 5 formants  @mal
    # where i is 0 to 4  
    for i, amp in enumerate([amp_1, amp_2, amp_3, amp_4, amp_5]):
        _private_cascadeAmplitudeResponse(A, B, C, omega_Hz, amp, i, t_s)
    
    plot_individual_formant_amplitude(vowel,f_Hz, amp_1, amp_2, amp_3, amp_4, amp_5)

    # sum up 5 sets of amplitude response @mal
    amp_sum = np.empty([1, 5000], dtype=float)
    for i in range(5000):
        amp_sum[0][i] = amp_1[0][i] + amp_2[0][i] + amp_3[0][i] + amp_4[0][i] + amp_5[0][i]

    # create arrays for storing phase response of 5 formants
    pha_1 = np.empty([1, 5000], dtype=float)
    pha_2 = np.empty([1, 5000], dtype=float)
    pha_3 = np.empty([1, 5000], dtype=float)
    pha_4 = np.empty([1, 5000], dtype=float)
    pha_5 = np.empty([1, 5000], dtype=float)

    # compute phase response of 5 formants
    # where i is 0 to 4
    for i, pha in enumerate([pha_1, pha_2, pha_3, pha_4, pha_5]):
        _private_cascadePhaseResponse(A, B, C, omega_Hz, pha, i, t_s)

    plot_individual_formant_phase(vowel,f_Hz,pha_1, pha_2, pha_3, pha_4, pha_5)

    # sum up 5 sets of phase response
    pha_sum = np.empty([1, 5000], dtype=float)
    for i in range(5000):
        pha_sum[0][i] = pha_1[0][i] + pha_2[0][i] + pha_3[0][i] + pha_4[0][i] + pha_5[0][i]

    return amp_sum, pha_sum
