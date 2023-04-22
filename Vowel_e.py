from Parallel_formant import *
from Cascade_formant import *
from Generate_files import *

vowel_u = 'e'

# cascade model
cas_f_e = [530, 1840, 2480, 3600, 4800] # cutoff frequency
cas_b_e = [90, 100, 200, 540, 800]
(cas_amp_e, cas_pha_e) = cascade_frequency_response(vowel_u, cas_f_e, cas_b_e)

# parallel model
f_e = [530, 1840, 2480]  # cutoff frequency
b_e = [60, 90, 130]  # bandwidth
gain = [1.82, 0.82, 0.14] # amplitude control
(amp_e, pha_e) = parallel_frequency_response(gain, f_e, b_e)

# plot amplitude and phase responses
f_step = 1
f_Hz = np.arange(0, 5000, f_step)

plot_responses(f_Hz, cas_amp_e, amp_e, cas_pha_e, pha_e, vowel_u)

