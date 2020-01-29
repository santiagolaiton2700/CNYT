import unittest,calculator
class TestCases(unittest.TestCase):
    def test_suma(self):
        a=(-3,3)
        b=(7,-2)
        self.assertEqual(calculator.suma(a,b),(4,1))
    def test_resta(self):
        a=(-3,3)
        b=(7,-2)
        self.assertEqual(calculator.resta(a,b),(-10,5))
    def test_multi(self):
        a=(1,-1)
        b=(2,-3)
        self.assertEqual(calculator.multi(a,b),(-1,-5))
    def test_division(self):
        a=(3,2)
        b=(1,-2)
        self.assertEqual(calculator.division(a,b),(-1/5,8/5))
    def test_conjugado(self):
        a=(3,4)
        self.assertEqual(calculator.conjugado(a),(3,-4))
    def test_modulo(self):
        a=(0,3)
        self.assertEqual(calculator.modulo(a),(3))
    def test_polar_cartesianas(self):
        a=(2,90)
        self.assertEqual(calculator.polar_a_cartesiano(a),(1.2246467991473532e-16,2.0))
    def test_cartesiano_polar(self):
        a=(1.2246467991473532e-16,2.0)
        self.assertEqual(calculator.cartesiano_a_polar(a),(1024.0, 90.0))
    def test_fase(self):
        a=(6,7)
        self.assertEqual(calculator.fase(a),(0.8621700546672264))
if __name__=="__main__":
    unittest.main()
