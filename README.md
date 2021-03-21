# Bio-Inspired Low Frequency Underwater Acoustic Modem (WhaleDem)
Although oceans represent 70% of the Earth's surface, communication underwater is still proving to be an incredibly difficult task. Light and odour don't travel very well, and we can't use our conventional communication methods since they simply just do not work underwater.
However, sound moves at **1.5km/s** in water, as opposed to **343m/s** in air, which is 4 times as much. This in fact is what marine mammals have been using to communicate with each other over long distances. Amongst them are whales. Whale 'songs', patterns of regular and predictable noises, are some of the most sophisticated communication systems in the animal kingdom. 
They constitute the basis of our inspiration for our implementation. 

## How it Works

An alphanumeric message is to be inputted by the user, which will in turn be frequency modulated, within the range of 10-47Hz. Each character or number is to be assigned to a specific frequency, the resulting message transmitted in the ocean would be looking something like the frequency modulated(FM) signal in the GIF below.

![Alt Text](https://upload.wikimedia.org/wikipedia/commons/a/a4/Amfm3-en-de.gif)

Our code would generate the frequency spectrum of the message, the one below being the one for "Iloveapples", our message being without spaces. 

![Alt Text](https://i.ibb.co/fDs40Zq/Figure-1.png)
## Limitations
1. **Bandwith** That the frequency of the acoustic waves is so low that it limits communication speed to around a kilobit per second. To put that in perspective, average broadband speeds are around 50 megabits per second (50,000 times as fast).
2. **Environmental factors** Temperature, salinity, pressure(depth) all influence density which influence the speed
