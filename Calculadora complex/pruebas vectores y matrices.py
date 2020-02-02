import unittest,calculator
class TestCases(unittest.TestCase):
    def test_addicionVectorial(self):
        a=[(3,4),(2,5)]
        b=[(4,5),(3,3)]
        self.assertEqual(calculator.adicionVectorial(a,b),[(7, 9), (5, 8)])
    def test_inverso_vectorial(self):
        a=[(3,4),(2,5)]
        self.assertEqual(calculator.inversa_vector(a),[(-3, -4), (-2, -5)])
    def test_multi_vector_escalar(self):
        a=[[2,3,2],[3,3,2]]
        b=3
        self.assertEqual(calculator.multiplicaionVectorEscalar(a,b),[(6, 9), (9, 9)])
    def test_matriz_suma(self):
        a=[[(2,3),(3,2)],[(3,2),(4,3)]]
        b=[[(2,3),(3,2)],[(3,2),(4,3)]]
        self.assertEqual(calculator.suma_matrices_complejos(a,b),[[(4, 6), (6, 4)], [(6, 4), (8, 6)]])
    def test_matriz_inversa(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.matriz_inversa(a),[[(-4, -6), (-6, -4)], [(-6, -4), (-8, -6)]])
    def test_multiplicacion_matriz_escalar(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        b=6
        self.assertEqual(calculator.multiplicacion_matriz_Escalar(a,b),[[(24, 36), (36, 24)], [(36, 24), (48, 36)]])
    def test_matriz_conjugada(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.matriz_conjugada(a),[[(4.0, -6.0), (6.0, -4.0)], [(6.0, -4.0), (8.0, -6.0)]])
    def test_matriz_transpuesta(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.matriz_transpuesta(a),[[(4, 6), (6, 4)], [(6, 4), (8, 6)]])
    def test_matriz_conjugada(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.matriz_conjugada(a),[[(4.0, -6.0), (6.0, -4.0)], [(6.0, -4.0), (8.0, -6.0)]])
    def test_matriz_adjunta(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.matriz_adjunta(a),[[(4.0, -6.0), (6.0, -4.0)], [(6.0, -4.0), (8.0, -6.0)]])
    def test_matriz_normal(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.matriz_normal(a),(7.211102550927978, 7.211102550927978))
    def test_matriz_hermitian(self):
        a=[[(6, 4), (8, 6)],[(3,5),(6,2)]]
        self.assertEqual(calculator.matriz_hermitian(a),False)
    def test_tensor(self):
        a=[(2,3),(2,3)]
        b=[(3,4),(2,4)]
        self.assertEqual(calculator.tensor(a,b),[[(-6, 17), (-8, 14)], [(-6, 17), (-8, 14)]])
if __name__=="__main__":
  unittest.main()
