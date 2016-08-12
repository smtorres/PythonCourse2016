class Animal(object):
  living="Yes!"
  def __init__(self, name):    # Constructor of the class
      self.name = name
      
  def talk(self):              # Abstract method, defined by convention only
  	raise NotImplementedError("Subclass must implement abstract method")
  	 
class Cat(Animal):
  def talk(self):
    return self.meow()
    
  def meow(self):
    return 'Meow!'
 
class Dog(Animal):
  def talk(self):
    return self.bark()
  
  def bark(self):
    return 'Woof! Woof!'
      
class Fish(Animal):
  
  def swim(self):
    pass
  
  def __str__(self):
    return "I am a fish!"

  def __repr__(self):
    return "I am a fish!"
      
animals = [Cat('Foo'),
           Dog('Bar'),
           Fish('nemo')]
 
for animal in animals: print animal.name
for animal in animals: print animal.talk()
for animal in animals: print animal

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
