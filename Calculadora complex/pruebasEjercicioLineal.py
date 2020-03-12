import unittest,calculator
class TestCases(unittest.TestCase):
    def test_proba(self):
        a=2
        b=[(7,5),(2,3),(1,2)]
        self.assertEqual(calculator.probabilidad(a,b),16.0)
    def test_transicion(self):
        a=[(7,5),(5,2),(4,2)]
        b=[(7,5),(2,3),(1,2)]
        self.assertEqual(calculator.transicion(a,b),(98.0, -17.0))
    
if __name__=="__main__":
    unittest.main()
