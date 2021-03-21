# Bio-Inspired Low Frequency Underwater Acoustic Modem (WhaleDem)
Although oceans represent 70% of the Earth's surface, communication underwater is still proving to be an incredibly difficult task. Light and odour don't travel very well, and we can't use our conventional communication methods since they simply just do not work underwater.
However, sound moves at **1.5km/s** in water, as opposed to **343m/s** in air, which is 4 times as much. This in fact is what marine mammals have been using to communicate with each other over long distances. Amongst them are whales. Whale 'songs', patterns of regular and predictable noises, are some of the most sophisticated communication systems in the animal kingdom. 
They constitute the basis of our inspiration for our implementation. 

## How it Works

An alphanumeric message is to be inputted by the user, which will in turn be frequency modulated, within the range of 10-47Hz. Each character or number is to be assigned to a specific frequency, the resulting message transmitted in the ocean would be looking something like the frequency modulated (FM) signal in the GIF below.


![Alt Text](https://upload.wikimedia.org/wikipedia/commons/a/a4/Amfm3-en-de.gif)

The progress bar in the CLI indicates the progress of sending the message as well as receiving it by the other client, depending on the distance to the receiver.

Our code would generate the frequency spectrum of the message, the one below being the one for "Iloveapples", our message being without spaces. Again, the messages only support a-z, 0-9 symbols, and are case-insensitive

![Alt Text](https://i.ibb.co/fDs40Zq/Figure-1.png)

Last but not least, an interactive 3D map is presented with the relative coordinates of the vessels in space, to give a perspective of the distance.


## Submarine Search Sonar: 
**Signal-to-Noise Ratio**
Although the characteristics of submarine search sonars vary substantially for different systems, typical sizes of the terms in the sonar equation can be obtained by working through an example for a hypothetical mid-frequency sonar operating at 8,000 Hz. The active sonar equation is:

snr_ratio=spreading_loss-(2*total_transmission_loss)+63+array_gain

**Transmission loss**
The transmission loss TL includes both sound spreading loss and attenuation. Sound spreading loss assuming spherical spreading for a range R of 10,000 m is:

Spreading loss (dB) = 20 log R

The attenuation due to sound absorption calculated using the absorption coefficient α (alpha) of about 0.5 dB/km at a frequency of 8,000 Hz is:

Attenuation (dB) = αR = (0.5 dB/km x 10 km)

total_transmission_loss=spreading_loss+attenuation




## Limitations
1. **Bandwith** The bitrate of the signal was chosen to be 1 symbol per second, i.e. the frequency changes every second to send the next symbol. Considering 1 symbol to be of 1 byte, that would result in 1 B/s transfer rate, which is extremely low and can only be used for text. To put that in perspective, average broadband speeds are around 50 megabits per second. Going for a lower "holding period" (less than 1 second) will improve the bitrate, however the hazards described in the next section will result in a larger packet loss as a result of this measure.
2. **Environmental factors** Temperature, salinity, pressure(depth) all influence density which, in turn, influences the local speed of sound. This, however, does not present a hazard as these fluctuations are realtively small and will not influence the delay. Environmental noise, on the other hand, can pose a threat to the integrity of the signal, as can moving water streams. Packet loss due to these factors could not be measured using software the team had on board and required field testing, which is not possible in the scope of this project.


