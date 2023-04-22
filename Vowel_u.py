from Parallel_formant import *
from Cascade_formant import *
from Generate_files import *

vowel_u = 'u'

# cascade model
cas_f_u = [350, 900, 2500, 3400, 4210]  # cutoff frequency
cas_b_u = [80, 110, 140, 250,400]  # bandwidth
(cas_amp_u, cas_pha_u) = cascade_frequency_response(vowel_u, cas_f_u, cas_b_u)

# parallel model
f_u = [350, 900, 2500] # cutoff frequency
b_u = [80, 110, 140] # bandwidth
gain = [1.16, 0.21, 0.065] # amplitude control
(amp_u, pha_u) = parallel_frequency_response(gain, f_u, b_u)

# plot amplitude and phase responses
f_step = 1
f_Hz = np.arange(0, 5000, f_step)

plot_responses(f_Hz, cas_amp_u, amp_u, cas_pha_u, pha_u, vowel_u)

