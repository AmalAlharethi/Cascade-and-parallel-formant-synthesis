import numpy as np
from Parallel_wavefoem import parallel_waveform
from Cascade_wavefoem import cascade_waveform
from Generate_files import *

# a
vowel = 'a'

# cascade model
cas_f_a = [660, 1200, 2550, 3500, 4000]  # cutoff frequency
cas_b_a = [100, 70, 200, 250, 200]
cas_output = cascade_waveform(vowel, cas_f_a, cas_b_a)

# parallel model
f_a = [660, 1200, 2550]  # cutoff frequency
b_a = [130, 70, 200]  # bandwidth
gain = [1.76, 0.89, 0.23] # amplitude control
parallel_output = parallel_waveform(vowel, gain, f_a, b_a)

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
