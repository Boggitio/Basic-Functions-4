import unittest
import Functions4

class TestFunctions4(unittest.TestCase):
    def test_checkperfsqrt(self):
        self.assertEqual(Functions4.checkperfsqrt(144), "144  is a perfect square.")
        self.assertEqual(Functions4.checkperfsqrt(87), "87  is NOT a perfect square.")

    def test_sumdig(self):
        self.assertEqual(Functions4.sumdig(657), 18)
        self.assertEqual(Functions4.sumdig(16208), 17)
        self.assertEqual(Functions4.sumdig(96554), 29)

    def test_isNPali(self):
        self.assertEqual(Functions4.isNPali(654321), "It is not a palindrome.")
        self.assertEqual(Functions4.isNPali(16788761), "It is a palindorme.")

    def test_findcommonword(self):
        self.assertEqual(Functions4.findcommonword("Hopefully, you know what you know."), "Most common word is |you|, and it appears 2 times.")
        self.assertEqual(Functions4.findcommonword("She sells sea shells by the sea shore. She loves the sea shells."), "Most common word is |sea|, and it appears 3 times.")

    #The random password generator function works as intended and since it's length and structure varies due to
    #it's randomness, it is too difficult to be tested unless a random seed is used, yet that would defeat the
    #purpose of the password being random.




if __name__ == '__main__':
    unittest.main()