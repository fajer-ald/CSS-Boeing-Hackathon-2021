import random
import sys
import math

class Vessel:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
    def gen_coords(self):
        self.x=random.randrange(0,101)
        self.y=random.randrange(0,101)
        self.z=random.randrange(-110,1)

def main_code():
    """
    Random generation of Vessel Location
    """
    ship = Vessel()
    ship.gen_coords()
    ship.z=0
    submarine = Vessel()
    submarine.gen_coords()
    
    """
    Calculation of the time it takes for the message to be delivered
    """
    arbitrary_underwater_speed_of_sound = 1500
    x_component = ship.x - submarine.x
    y_component = ship.y - submarine.y
    z_component = ship.z - submarine.z
    distance_between_two_vessels = math.sqrt(math.pow(x_component, 2) + math.pow(y_component, 2) + math.pow(z_component, 2))
    time_taken = distance_between_two_vessels / arbitrary_underwater_speed_of_sound
    
    temperature = random.randrange(0, 35)
    salinity = random.randrange(0, 45)
    depth = random.randrange(0, 4000)
    component_1 = 45.7 * temperature
    component_2 = 5.21 * math.pow(temperature, 2)
    component_3 = 0.23 * math.pow(temperature, 3)
    component_4 = 0.126 * temperature
    component_5 = 0.009 * math.pow(temperature, 2)
    realistic_speed_of_sound = (1449.05 + component_1) - component_2 + component_3 + (1.333 - component_4) + component_5 * (salinity - 35)
    
    """
    Message transcription into list of frequencies
    """

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    values = letters + numbers
    freq = list(range(10,46))
    code = dict(zip(values,freq))
    transcript=[]

    msg = input('Please enter your message: ')
    msg = msg.lower()
    if msg.isalnum() is False:
        print('Message not alphanumeric, unable to send')
        sys.exit(1)
    for i in range(len(msg)):
        transcript.append(code.get(msg[i]))
    return transcript,ship.x,ship.y,ship.z,submarine.x,submarine.y,submarine.z,time_taken,realistic_speed_of_sound

		
