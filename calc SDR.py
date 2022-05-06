import numpy as np

rms = 6.1983
x = 5.6848

res = 10 * np.log10 (x**2/(rms**2-x**2))

print (res)