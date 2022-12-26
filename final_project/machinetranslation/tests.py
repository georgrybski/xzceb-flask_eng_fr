import unittest
from translator import english_to_french, french_to_english

class TestTranslationFunctions(unittest.TestCase):

    def test_english_to_french_null_input(self):
        # Test for null input
        self.assertIsNone(english_to_french(None))

    def test_french_to_english_null_input(self):
        # Test for null input
        self.assertIsNone(french_to_english(None))

    def test_english_to_french_hello(self):
        # Test for translation of 'Hello'
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Salut')

    def test_french_to_english_bonjour(self):
        # Test for translation of 'Bonjour'
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Salut')

if __name__ == '__main__':
    unittest.main()
    