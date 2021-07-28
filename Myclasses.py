
class Animal:
  #Animal class

  #class variables
  gtype = 'lifeform'

  def __init__(self,name):
    self.name = name

  def makeSound(self, sound):
    print(f'{self.name} makes the sound "{sound}!"')

  def __str__(self):
    return f'This is an animal called {self.name}'

  def __add__(self,other):
    return f'{self.name} and {other.name}'

class Horse(Animal)


