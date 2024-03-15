'''Inheritance is an important notion in instances when you have an existing class with established properties and behaviors and require a new class that not only inherits these features but also has its own independent ones. Inheritance enables the new class to 'inherit' properties from its parent class while adding or altering particular features as required.
'''
class Animal:
  def __init__(self,name):
    self.name=name
#To inherit characteristics from the parent class, use super().__init__(), then create any new attributes as normal.
class Dog(Animal):
  def __init__(self, name, breed, color):
    super().__init__(name)
    self.breed = breed
    self.color = color
    one_dog=Dog("Mike","Husky","White")
