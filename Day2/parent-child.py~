class Parent():
  def __init__(self, sex, firstname, lastname):
    self.sex = sex
    self.firstname = firstname
    self.lastname = lastname
    self.kids = []

  def role(self):
    if self.sex == "Male":
      return "Father"
    else:
      return "Mother"

  def have_child(self, name):
    child = Child(name, self)
    print self.firstname + " is having a child named " + child.name()
    print "They will make a very good " + self.role()
    self.kids.append(child)
    return child

  def list_children(self):
    for kid in self.kids:
      print "I am the " + self.role() + " of " + kid.name()

class Child():
  def __init__(self, firstname, parent):
    self.parent = parent 
    self.lastname = parent.lastname
    self.firstname = firstname

  def set_name(self, new_first_name, new_last_name):
    self.firstname = new_first_name
    self.lastname = new_last_name

  def name(self):
    return "%s %s" % (self.firstname, self.lastname)

  def introduce(self):
    return "Hi I'm " + self.name()

  def siblings(self):
    for kid in self.parent.kids:
      if kid != self:
        print "I have a sibling named " + kid.name()
  
  def __str__(self):
  	return "%s" %self.firstname 

mom = Parent("Female", "Jane", "Smith")
mom.list_children()
jill=mom.have_child("Jill")
jill.firstname
jill.parent.firstname
jill.set_name("Jillian", "Jones")
print jill.introduce()
print jill == mom.kids[0]
jack = mom.have_child("Jack")
print jack.introduce()
jack.parent.kids[0].parent.list_children()
jack.siblings()

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

