import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
	
fig1, ax1=plt.subplots()
freqs_g=ax1.bar(freqs, counts, 0.8, color='blue')
ax1.set_xlabel('Frequency, Hz')
ax1.set_ylabel('Times transmitted')
plt.xlim([9, 36])
ax1.set_title('Frequency spectrum of the transmission')
fig2 = plt.figure()
ax2 = plt.axes(projection='3d')
ax2.scatter([data[1],data[4]],[data[2],data[5]],[data[3],data[6]])
plt.show()