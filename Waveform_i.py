import numpy as np
from Parallel_wavefoem import parallel_waveform
from Cascade_wavefoem import cascade_waveform
from Generate_files import *

# i
vowel = 'i'

# cascade model
cas_f_i = [310, 2020, 2960, 3300, 4200]  # cutoff frequency
cas_b_i = [45, 200, 400, 250, 690]  # bandwidth
cas_output = cascade_waveform(vowel, cas_f_i, cas_b_i)

# parallel model
f_i = [310, 2020, 2960]  # cutoff frequency
b_i = [45, 200, 400]  # bandwidth
gain = [1.06, 0.18, 0.4]  # amplitude control
parallel_output = parallel_waveform(vowel, gain, f_i, b_i)

# plot waveform and save file

f_s = 10000  # int, sampling frequency (Fs): 10 kHz
t_s = 1 / f_s  # float, sampling period (Ts) = 1/sampling frequency = 0.1 ms
time = np.arange(-0.2, 100.1, t_s * 1000)
'''
creates an array time which contains the time values for the signal,
from -0.2 seconds to 100.1 seconds, spaced t_s milliseconds apart.
This array is useful for plotting the signal in the time domain. 
'''
plot_waveform(time, cas_output, parallel_output, vowel)
save_audio_file(cas_output, f_s, "cascade_{}".format(vowel))
save_audio_file(parallel_output, f_s, "parallel_{}".format(vowel))