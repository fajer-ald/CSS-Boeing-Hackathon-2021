




# populating the dictionary for our code.

dicts = {}
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
values = letters + numbers
print(len(values))
frequency_range = list(range(10,47))
code = dict(zip(frequency_range, values))

class Vessel:
    def __init__(self, xcoordinate, ycoordinate, zcoordinate):
        self.xcoordinate=xcoordinate
        self.ycoordinate=ycoordinate
        self.zcoordinate=zcoordinate
    def coordinates_generator(self,xcoordinate,ycoordinate,zcoordinate):
        x=list(range(0,101))
        y=list(range(0,111))
        z=list(range(0,101))

"""
class Loudspeaker:
    def __init__(self):

class Hydrophone:
    def __init__(self,signal):
        # signal is Boolean
        self.signal=signal
  """  
    
surface_vessel=Vessel(randrange(),randrange(),100)
submarine=Vessel(randrange(),randrange(),0)
