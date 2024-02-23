# %%
import pyfar as pf
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

signal = [[np.sin(np.linspace(0, 2*np.pi, 1024))],
          [np.sin(np.linspace(0, 6*np.pi, 1024)) * .5],
          [np.sin(np.linspace(0, 10*np.pi, 1024)) * .25]]

signal = pf.Signal(signal, 1024)
ax = pf.plot.time(signal, linewidth=4)
plt.axis('off')
plt.savefig('thumbnail_pyfar_audio_objects.png')
