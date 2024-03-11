# %%
import pyfar as pf
import matplotlib.pyplot as plt

pf.plot.use()
fig, ax = plt.subplots(2, 1, figsize=(6.4, 4.8))

impulse = pf.signals.impulse(1e3)
signal = pf.dsp.filter.butterworth(
    impulse, 3, frequency=(4000, 5000), btype='bandpass')
pf.plot.time_freq(signal, lw=6, ax=[ax[0], ax[-1]])
ax[0].set_xlim(0, 0.005)
ax[0].set_axis_off()
ax[1].set_axis_off()
fig.text(0.5, 0.5, "FFT", fontsize=100, ha='center', va='center')

plt.savefig('thumbnail_fast_fourier_transform.png')