import numpy as np
import matplotlib.pyplot as plt
import time
#import main
from tqdm.auto import tqdm

vessel_x=30
vessel_y=14
vessel_z=40
freqs=[34,46,50]
counts=[1,2,3]

symbols = [10,26,13,28]

pbar1 = tqdm(total=len(symbols), position=0, desc='Sending data')
pbar2 = tqdm(total=len(symbols), position=1, desc='Receiving data')

for i in range(len(symbols)):
    time.sleep(0.5)
    pbar1.update(1)
    time.sleep(0.5)
    pbar2.update(1)
	
fig, ax=plt.subplots()
freqs_g=ax.bar(freqs, counts, 0.8, color='blue')
ax.set_xlabel('Frequency, Hz')
ax.set_ylabel('Score')
ax.set_title('Frequency spectrum of the transmission')
plt.show()