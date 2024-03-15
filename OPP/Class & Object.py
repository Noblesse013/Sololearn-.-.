'''The __init__ function must be defined before you may add attributes to a class. The first parameter to this function is always self, which represents the class's instance. '''
class Car():
  def __init__(self, brand, color):
    self.brand = brand  #attribute
    self.color = color

my_car = Car('Tesla', 'orange') #object


