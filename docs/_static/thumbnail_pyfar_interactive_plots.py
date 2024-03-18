%%

import pyfar as pf
import matplotlib.pyplot as plt

hrirs, sources = pf.signals.files.head_related_impulse_responses(position='horizontal')

pf.plot.use()
plt.figure()
pf.plot.time(hrirs)
plt.savefig('thumbnail_pyfar_interactive_plots.png')