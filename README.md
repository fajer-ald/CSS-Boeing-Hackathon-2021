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

## Limitations
1. **Bandwith** The bitrate of the signal was chosen to be 1 symbol per second, i.e. the frequency changes every second to send the next symbol. Considering 1 symbol to be of 1 byte, that would result in 1 B/s transfer rate, which is extremely low and can only be used for text. To put that in perspective, average broadband speeds are around 50 megabits per second. Going for a lower "holding period" (less than 1 second) will improve the bitrate, however the hazards described in the next section will result in a larger packet loss as a result of this measure.
2. **Environmental factors** Temperature, salinity, pressure(depth) all influence density which, in turn, influences the local speed of sound. This, however, does not present a hazard as these fluctuations are realtively small and will not influence the delay. Environmental noise, on the other hand, can pose a threat to the integrity of the signal, as can moving water streams. Packet loss due to these factors could not be measured using software the team had on board and required field testing, which is not possible in the scope of this project.



import random
import sys
import math


class Vessel:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def gen_coords(self):
        self.x = random.randrange(0, 101)
        self.y = random.randrange(0, 101)
        self.z = random.randrange(-110, 1)

def receiver_noise(ship_Range,t):
    spreading_loss=20*math.log(ship_Range)
    attenuation=ship_Range*0.5
    total_transmission_loss=spreading_loss+attenuation
    array_gain=10
    snr_ratio=spreading_loss-(2*total_transmission_loss)+63+array_gain
    bandwidth=1/t
    return snr_ratio, total_transmission_loss,bandwidth

def main_code():
    """
    Random generation of Vessel Location
    """
    ship = Vessel()
    ship.gen_coords()
    ship.z = 0
    submarine = Vessel()
    submarine.gen_coords()

    """
    Calculation of the time it takes for the message to be delivered
    """
    arbitrary_underwater_speed_of_sound = 1500
    x_component = ship.x - submarine.x
    y_component = ship.y - submarine.y
    z_component = ship.z - submarine.z
    distance_between_two_vessels = math.sqrt(
        math.pow(x_component, 2) + math.pow(y_component, 2) + math.pow(z_component, 2))
    time_taken = distance_between_two_vessels / arbitrary_underwater_speed_of_sound

    """
    Calculation equation for the speed of sound in sea-water as a function of temperature, salinity and depth 
    is given by Coppens equation 1981.
    Range of validity: temperature 0 to 35 °C, salinity 0 to 45 parts per thousand, depth 0 to 4000 m
    """
    temperature = random.randrange(0, 35)
    salinity = random.randrange(0, 45)
    depth = random.randrange(0, 4000)
    component_1 = 45.7 * temperature
    component_2 = 5.21 * math.pow(temperature, 2)
    component_3 = 0.23 * math.pow(temperature, 3)
    component_4 = 0.126 * temperature
    component_5 = 0.009 * math.pow(temperature, 2)

    realistic_speed_of_sound = (1449.05 + component_1) - component_2 + component_3 + (
                1.333 - component_4) + component_5 * (salinity - 35)



    """
    Message transcription into list of frequencies
    """

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    values = letters+ numbers
    freq = list(range(10, 46))
    code = dict(zip(values, freq))
    transcript = []

    msg = input('Please enter your message: ')
    msg = msg.lower()
    if msg.isalnum() is False:
        print('Message not alphanumeric, unable to send')
    sys.exit(1)
    for i in range(len(msg)):
        transcript.append(code.get(msg[i]))
    return transcript, ship.x, ship.y, ship.z, submarine.x, submarine.y, submarine.z, time_taken, realistic_speed_of_sound
