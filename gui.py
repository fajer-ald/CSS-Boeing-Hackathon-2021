import numpy as np
import matplotlib.pyplot as plt
import time
import main
from tqdm.auto import tqdm

data=main.main_code()

freqs=[10,15,20,34,35,36]
counts=[1,1,2,3,4,2]

symbols = [10,26,13,28]

pbar1 = tqdm(total=len(data[0]), position=0, desc='Sending data')
pbar2 = tqdm(total=len(data[0]), position=1, desc='Receiving data')

for i in range(len(data[0])):
    time.sleep(0.5)
    pbar1.update(1)
    time.sleep(0.5)
    pbar2.update(1)
	
fig, ax=plt.subplots()
freqs_g=ax.bar(freqs, counts, 0.8, color='blue')
ax.set_xlabel('Frequency, Hz')
ax.set_ylabel('Times transmitted')
plt.xlim([10, 36])
ax.set_title('Frequency spectrum of the transmission')
plt.show()