# Bio-Inspired Low Frequency Underwater Acoustic Modem (WhaleDem)
Although oceans represent 70% of the Earth's surface, communication underwater is still proving to be an incredibly difficult task. Light and odour don't travel very well, and we can't use our conventional communication methods since they simply just do not work underwater.
However, sound moves at **1.5km/s** in water, as opposed to **343m/s** in air, which is 4 times as much. This in fact is what marine mammals have been using to communicate with each other over long distances. Amongst them are whales. Whale 'songs', patterns of regular and predictable noises, are some of the most sophisticated communication systems in the animal kingdom. 
They constitute the basis of our inspiration for our implementation. 

## How it Works

An alphanumeric message is to be inputted by the user, which will in turn be frequency modulated, within the range of 10-47Hz. Each character or number is to be assigned to a specific frequency, the resulting message transmitted in the ocean would be looking something like the frequency modulated (FM) signal in the GIF below.

![Alt Text](https://upload.wikimedia.org/wikipedia/commons/a/a4/Amfm3-en-de.gif)

Our code would generate the frequency spectrum of the message, the one below being the one for "Iloveapples", our message being without spaces. Again, the messages only support a-z, 0-9 symbols, and are case-insensitive

![Alt Text](https://i.ibb.co/fDs40Zq/Figure-1.png)
## Limitations
1. **Bandwith** The bitrate of the signal was chosen to be 1 symbol per second, i.e. the frequency changes every second to send the next symbol. Considering 1 symbol to be of 1 byte, that would result in 1 B/s transfer rate, which is extremely low and can only be used for text. To put that in perspective, average broadband speeds are around 50 megabits per second. Going for a lower "holding period" (less than 1 second) will improve the bitrate, however the hazards described in the next section will result in a larger packet loss as a result of this measure.
2. **Environmental factors** Temperature, salinity, pressure(depth) all influence density which, in turn, influences the local speed of sound. This, however, does not present a hazard as these fluctuations are realtively small and will not influence the delay. Environmental noise, on the other hand, can pose a threat to the integrity of the signal, as can moving water streams. Packet loss due to these factors could not be measured using software the team had on board and required field testing, which is not possible in the scope of this project.
