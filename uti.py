import unittest

class TestString(unittest.TestCase):

	def test_upper(self):
		test_str = 'Flow'
		self.assertEqual(test_str.upper(), 'FLOW')

	def test_lower(self):
		test_str = 'Glow'
		self.assertEqual(test_str.lower(), 'glow')

	def test_split(self):
		split_str = 'Split String'
		self.assertEqual(split_str.split(' '), ['Split', 'String']

if __name__ == '__main__':
	unittest.main()