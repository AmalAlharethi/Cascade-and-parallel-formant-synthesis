from Parallel_formant import *
from Cascade_formant import *
from Generate_files import *

vowel_i = 'i'

# cascade model
cas_f_i = [550, 2200, 3000, 3800, 4800]
cas_b_i = [60, 130, 160, 210, 260] 
(cas_amp_i, cas_pha_i) = cascade_frequency_response(vowel_i, cas_f_i, cas_b_i)

# parallel model
f_i = [550, 2200, 3000] # cutoff frequency
b_i = [60, 130, 160] # bandwidth
gain = [1.82, 0.82, 0.14] # amplitude control
(amp_i, pha_i) = parallel_frequency_response(gain, f_i, b_i)

# plot amplitude and phase responses
f_step = 1
f_Hz = np.arange(0, 5000, f_step)

plot_responses(f_Hz, cas_amp_i, amp_i, cas_pha_i, pha_i, vowel_i)
