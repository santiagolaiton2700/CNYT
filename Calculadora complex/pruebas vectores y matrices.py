import unittest,calculator
class TestCases(unittest.TestCase):
    def test_addicionVectorial(self):
        a=[(3,4),(2,5)]
        b=[(4,5),(3,3)]
        self.assertEqual(calculator.adicionVectorial(a,b),[(7, 9), (5, 8)])
    def test_inverso_vectorial(self):
        a=[(3,4),(2,5)]
        self.assertEqual(calculator.inversa_vector(a),[(-3, -4), (-2, -5)])
if __name__=="__main__":
  unittest.main()
