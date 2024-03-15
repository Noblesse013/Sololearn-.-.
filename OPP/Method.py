'''In addition to properties, more features may be added to a class by declaring functions within it. These functions, called as methods, should include the'self' argument to communicate with the class instance. You may access these methods using the dot. notation, just like you would for attributes.'''
class Car:
  def __init__(self, brand, color):
    self.brand = brand #attributes
    self.color = color #attributes
    
  def honk(self): #method
    print(str(self.brand)+" is "+"honking!")

one_car=Car("Tesla","Barbie Pink")
one_car.honk()
