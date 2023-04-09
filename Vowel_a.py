from Parallel_formant import *
from Cascade_formant import *
from Generate_files import *

vowel_a = 'a'

# cascade model @mal
cas_f_a = [660, 1200, 2550, 3500, 4000]  # cutoff frequency
cas_b_a = [100, 70, 200, 250, 200]
(cas_amp_a, cas_pha_a) = cascade_frequency_response(vowel_a, cas_f_a, cas_b_a)

# parallel model @mal
f_a = [660, 1200, 2550] # cutoff frequency
b_a = [130, 70, 200] # bandwidth 45 200 400
gain = [1.76, 0.89,0.23] # amplitude control
(amp_a, pha_a) = parallel_frequency_response( gain, f_a, b_a)

# plot amplitude and phase responses
f_step = 1
f_Hz = np.arange(0, 5000, f_step)

plot_responses(f_Hz, cas_amp_a, amp_a, cas_pha_a, pha_a, vowel_a)