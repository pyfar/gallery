# %%
import pyfar as pf
import matplotlib.pyplot as plt

impulse = pf.signals.impulse(44100)

pf.plot.use()


# %% audio filter (bell and shelves) ------------------------------------------
_, ax = plt.subplots(1, 1, figsize=(15/2.54, 12/2.54), sharey=True)

# bell and shelve
frequency = 5e2
linewidth = 8
axis = ax
y = pf.dsp.filter.bell(impulse, frequency, 10, 2)
pf.plot.freq(y, ax=axis, label='Bell', lw=linewidth)

y = pf.dsp.filter.bell(impulse, frequency, -10, 2)
pf.plot.freq(y, ax=axis, label='Bell', lw=linewidth)

y = pf.dsp.filter.high_shelve(impulse, 8*frequency, 10, 2, 'II')
pf.plot.freq(y * 10**(-20/20), ax=axis, label='High-shelve', lw=linewidth)

y = pf.dsp.filter.high_shelve(impulse, 8*frequency, -10, 2, 'II')
pf.plot.freq(y * 10**(-20/20), ax=axis, label='High-shelve', lw=linewidth)

y = pf.dsp.filter.low_shelve(impulse, 1/4*frequency, 10, 2, 'II')
pf.plot.freq(y * 10**(-40/20), ax=axis, label='Low-shelve', lw=linewidth)

y = pf.dsp.filter.low_shelve(impulse, 1/4*frequency, -10, 2, 'II')
pf.plot.freq(y * 10**(-40/20), ax=axis, label='Low-shelve', lw=linewidth)

axis.set_title('')
axis.set_xlim(20, 20e3)
axis.set_ylim(-51, 11)
axis.set_xlabel('')
axis.set_ylabel('')
axis.set_xticklabels([])
axis.set_yticklabels([])

plt.savefig('thumbnail_pyfar_filter_types.png', dpi=150)
