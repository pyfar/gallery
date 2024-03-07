# %%
import pyfar as pf
import matplotlib.pyplot as plt
%matplotlib inline

signal = pf.dsp.filter.crossover(pf.signals.impulse(2**12), 8, 2e2)
signal2 = pf.dsp.filter.crossover(signal[1], 8, 2e3)

ax = pf.plot.freq(signal[0], linewidth=8)
pf.plot.freq(signal2, linewidth=8)
ax.set_ylim(-40, 5)
plt.axis('off')
plt.savefig('thumbnail_pyfar_filtering.png')
