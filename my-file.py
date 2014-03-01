# LEARNING PYTHON PART TWO

#...     pass
#... 
#>>> fido = Dog()
#>>> fido.name = "Fido"

#>>> class Cat(object):
#...     
#...     def sound(self):
#...             print "meow"
#... 
#>>> fuzzy = Cat()
#>>> fuzzy.sound()
#meow

# normally testing in one file
# import code in a nice clean place
# to test: python -m unittest -v my-file

from unittest import TestCase 
#TestCase is a class of unittest

class Cat(object):

	def sound(self):
		return "meow"

class TestCat(TestCase):

	def test_sound(self):
		cat = Cat()
		self.assertEqual(cat.sound(), "meow")
		