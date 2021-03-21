import numpy as np
import matplotlib.pyplot as plt
import time
import main
from tqdm.auto import tqdm

data=main.main_code()

freqs=list(range(10,46))
counts=[]

pbar1 = tqdm(total=len(data[0]), position=0, desc='Sending data')
pbar2 = tqdm(total=len(data[0]), position=1, desc='Receiving data')

for i in range(len(data[0])):
    time.sleep(0.5)
    pbar1.update(1)
    time.sleep(0.5)
    pbar2.update(1)
	
for i in range(len(freqs)):
    counts.append(data[0].count(freqs[i]))
	
fig, ax=plt.subplots()
freqs_g=ax.bar(freqs, counts, 0.8, color='blue')
ax.set_xlabel('Frequency, Hz')
ax.set_ylabel('Times transmitted')
plt.xlim([9, 36])
ax.set_title('Frequency spectrum of the transmission')
plt.show()