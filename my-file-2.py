from unittest import TestCase




class Candidate(object):

	def __init__(self, raw_name, party):
		self.raw_name = raw_name
		self.party = party
		self._parse_name()

	# Private methods
	def _parse_name(self):
		name_bits = self.raw_name.split(',')
		self.last_name = name_bits[0].strip()
		self.first_name = name_bits[1].strip()



# python -m unittest -v my-file-2
# test-driven development =
# better to write test first, then write code to pass
class TestCandidate(TestCase):

	def test_name_parsing(self):
		cand = Candidate("Smith, John", "IND")
		self.assertEqual(cand.last_name, "Smith")
		self.assertEqual(cand.first_name, "John")
