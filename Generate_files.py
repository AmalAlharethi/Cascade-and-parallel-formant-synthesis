import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

def plot_individual_formant_amplitude(vowel,f_Hz, amp_1, amp_2, amp_3, amp_4, amp_5):
    '''
    input:
    f_Hz: numpy array, frequency in Hz
    amp_1, amp_2, amp_3, amp_4, amp_5: numpy array, amplitude in dB for formants 1, 2, 3, 4 and 5

    output: plot of the amplitude spectrum of five resonators
    '''
    plt.figure(f'individual formant for amplitude [{vowel}]')
    plt.plot(f_Hz, amp_1[0], label='F1', color="blue")
    plt.plot(f_Hz, amp_2[0], label='F2', color="green")
    plt.plot(f_Hz, amp_3[0], label='F3', color="pink")
    plt.plot(f_Hz, amp_4[0], label='F4', color="darkorange")
    plt.plot(f_Hz, amp_5[0], label='F5', color="purple")
    plt.xlabel('frequency (Hz)')
    plt.ylabel('amplitude (dB)')
    plt.legend()
    plt.title(f'Amplitude spectrum of five resonators for vowel [{vowel}]')
    plt.grid(linestyle='-.')
    plt.savefig('formant_amplitude_' + str(vowel) + '.jpg', dpi=300)
    plt.show()

# Cascade synthesiser waveform, amplitude and phase responses graphs

def plot_individual_formant_phase(vowel,f_Hz, pha_1, pha_2, pha_3, pha_4, pha_5):
    '''
    Plot the individual formant phase spectra of five resonators.

    Parameters:
        f_Hz (numpy.ndarray): frequency values in Hz
        pha_1 (numpy.ndarray): phase values for the first formant
        pha_2 (numpy.ndarray): phase values for the second formant
        pha_3 (numpy.ndarray): phase values for the third formant
        pha_4 (numpy.ndarray): phase values for the fourth formant
        pha_5 (numpy.ndarray): phase values for the fifth formant
    '''
   
    plt.figure(f'individual formant for phase [{vowel}]')
    plt.plot(f_Hz, pha_1[0], label='F1', color="blue")
    plt.plot(f_Hz, pha_2[0], label='F2', color="green")
    plt.plot(f_Hz, pha_3[0], label='F3', color="pink")
    plt.plot(f_Hz, pha_4[0], label='F4', color="darkorange")
    plt.plot(f_Hz, pha_5[0], label='F5', color="purple")
    plt.xlabel('frequency (Hz)')
    plt.ylabel('phase (degree)')
    plt.legend()
    plt.title(f'Phase spectrum of five resonators for vowel [{vowel}]')
    plt.grid(linestyle='-.')
    plt.savefig('formant_Phase_' + str(vowel) + '.jpg', dpi=300)
    plt.show()

def plot_responses(f_Hz, cas_amp, amp, cas_pha, pha, vowel):
    # amplitude response
    plt.figure(f"Amplitude response of [{vowel}]")
    plt.xlabel('frequency (Hz)')
    plt.ylabel('amplitude (dB)')
    plt.plot(f_Hz, cas_amp[0], label='cascade model', color="blue")
    plt.plot(f_Hz, amp[0], '--', color='red', label='parallel model')
    plt.legend()
    plt.title(f'Amplitude Response for vowle [{vowel}]')
    plt.grid(linestyle='-.')
    plt.savefig('amplitude_respons_' + str(vowel) + '.jpg', dpi=300)

    # phase response
    plt.figure(f"Phase response of [{vowel}]")
    plt.xlabel('frequency (Hz)')
    plt.ylabel('phase (degree)')
    plt.plot(f_Hz, cas_pha[0], label='cascade model', color="blue")
    plt.plot(f_Hz, pha[0], '--', color='red', label='parallel model')
    plt.legend()
    plt.title(f'Phase Response for vowle [{vowel}]')
    plt.grid(linestyle='-.')
    plt.savefig('phase_response_' + str(vowel) + '.jpg', dpi=300)

    plt.show()

def plot_waveform(time, cas_output, output, vowel):
    plt.figure("Output waveform")
    plt.xlabel('time (ms)')
    plt.ylabel('amplitude')
    plt.plot(time[2:300], cas_output[2:300], label='cascade model', color='blue')
    plt.plot(time[2:300], output[2:300], label='parallel model', color='red')
    plt.legend()
    plt.grid(linestyle='-.')
    plt.savefig('Output_wavefor_' + str(vowel) + '.jpg', dpi=300)
    plt.title('Output waveform[' + str(vowel) + ']')

    plt.show()

def plot_cascade_waveform_for_vowel(time, output_5, name):
    plt.figure("Output waveform")
    plt.plot(time[2:300], output_5[2:300])
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.title("Cascade Output Waveform - {}".format(name))
    plt.grid(linestyle='-.')
    plt.savefig('cascade_waveform_{}.jpg'.format(name), dpi=300)
    plt.show()

def plot_parallel_waveform_for_vowel(time, output,vowel):
    """
    Plots and saves a waveform plot of the output signal.
    
    Parameters:
        - time (numpy.ndarray): the time values for the signal.
        - output (numpy.ndarray): the output signal values.
        - vowel (str): the vowel of the waveform plot.
        
    Returns:
        None.
    """
    plt.figure("Output waveform")
    plt.xlabel('time (ms)')
    plt.ylabel('amplitude')
    plt.plot(time[2:300], output[2:300])
    plt.title("Parallel Output Waveform - " + str(vowel))
    plt.grid(linestyle='-.')
    plt.savefig('parallel_waveform_' + str(vowel) + '.jpg', dpi=300)
    plt.show()

def save_audio_file(output, f_s, vowel):
    '''
    Saves a waveform as an audio file.

    Arguments:
    output -- array containing the waveform data
    f_s -- the sampling frequency of the waveform
    fileName -- the name of the file to be saved
    '''
    wav_data = np.array(output)
    fileName = "{}_output.wav".format(vowel)
    wavfile.write(fileName, f_s, wav_data.astype(np.int16))