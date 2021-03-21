import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import main
import PySimpleGUI as sg

data=main.main_code()


sg.theme('Reddit')
error_data=main.error_statistics()

freqs=list(range(10,46))
counts=[]

pb1 = [
    [sg.ProgressBar(len(data[0]), orientation='h', size=(51, 10), key='pb1')]
]
pb2 = [
    [sg.ProgressBar(len(data[0]), orientation='h', size=(51, 10), key='pb2')]
]
layout = [
    [sg.Frame('Send',layout=pb1)],
    [sg.Frame('Receive',layout=pb2)]
]
window = sg.Window('Data Transfer', layout)
progress_bar1 = window['pb1']
progress_bar2 = window['pb2']

while True:
    print('lol')
    window.read(timeout=10)
    for i,item in enumerate(data[0]):
        print(i)
        time.sleep(0.1)
        progress_bar1.UpdateBar(i+1)
        time.sleep(data[7])
        progress_bar2.UpdateBar(i+1)
    break
window.close()
	
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