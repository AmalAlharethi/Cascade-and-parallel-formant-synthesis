from Parallel_formant import *
from Cascade_formant import *
from Generate_files import *

vowel_i = 'i'

# cascade model
cas_f_i = [310, 2030, 2960, 4080, 4950]
cas_b_i = [45, 200, 400, 400, 690]
(cas_amp_i, cas_pha_i) = cascade_frequency_response(vowel_i, cas_f_i, cas_b_i)

# parallel model
f_i = [310, 2030, 2960] # cutoff frequency
b_i = [45, 200, 400] # bandwidth
gain = [1.06, 0.18, 0.4] # amplitude control
(amp_i, pha_i) = parallel_frequency_response(vowel_i, gain, f_i, b_i)

# plot amplitude and phase responses
f_step = 1
f_Hz = np.arange(0, 5000, f_step)

plot_responses(f_Hz, cas_amp_i, amp_i, cas_pha_i, pha_i, vowel_i)
