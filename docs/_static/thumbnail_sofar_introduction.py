# %%
import pyfar as pf
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

pf.plot.use()
fig = plt.figure(figsize=(2.5, 2))

h, sources = pf.signals.files.head_related_impulse_responses('horizontal')
h = pf.dsp.pad_zeros(h, 4410)

ax, qm, _ = pf.plot.freq_2d(
    h[:, 0], indices=sources.azimuth / np.pi * 180, cmap='RdBu_r',
    colorbar=False)

ax.set_ylim(200, 20e3)
qm.set_clim(-25, 25)
ax.axis('off')

plt.savefig('thumbnail_sofar_introduction.png',
            bbox_inches='tight', pad_inches=0)
