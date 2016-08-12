import unittest #You need this module
import myscript #This is the script you want to test


class mytest(unittest.TestCase):

  def test_one(self):
    self.assertEqual("result I need", myscript.myfunction(myinput))
    
  def test_two(self)
  	thing1=myscript.myfunction(myinput1)
  	thing2=myscript.myfunction(myinput2)
    self.assertNotEqual(thing1, thing2)

if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()


