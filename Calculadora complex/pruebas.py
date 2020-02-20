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
    def test_vector_conjugado(self):
        a=[(4, 6), (6, 4), (6, 4), (8, 6)]
        self.assertEqual(calculator.vector_conjugado(a),[(4.0, -6.0), (6.0, -4.0), (6.0, -4.0), (8.0, -6.0)])        
    def test_matriz_transpuesta(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.matriz_transpuesta(a),[[(4, 6), (6, 4)], [(6, 4), (8, 6)]])
    def test_vector_transpuesto(self):
        a=[(3,4),(2,5)]
        self.assertEqual(calculator.vector_transpuesto(a),[(3, 4), (2, 5)])
    def test_vector_adjunto(self):
        a=[(3,4),(2,5)]
        self.assertEqual(calculator.vector_adjunto(a),[(3.0, -4.0), (2.0, -5.0)])  
    def test_matriz_conjugada(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.matriz_conjugada(a),[[(4.0, -6.0), (6.0, -4.0)], [(6.0, -4.0), (8.0, -6.0)]])
    def test_productor_matriz(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.multiplicacion_matrices(a,a),[[(0, 96), (24, 120)], [(24, 120), (48, 144)]])
    def test_producto_vectores(self):
        a=[(3,4),(2,5)]
        b=[(4,5),(3,3)]
        self.assertEqual(calculator.producto_vectores(a,b),(-17, 52))
    def test_producto_vectores(self):
        a=[(3,4),(2,5)]
        b=[(4,5),(3,3)]
        self.assertEqual(calculator.producto_interno_vectores(a,b),(53.0, -10.0))
    def test_matriz_adjunta(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.matriz_adjunta(a),[[(4.0, -6.0), (6.0, -4.0)], [(6.0, -4.0), (8.0, -6.0)]])
    def test_matriz_normal(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.matriz_normal(a),(7.211102550927978, 7.211102550927978))
    def test_distancia_vector(self):
        a=(3,4)
        b=(2,5)
        self.assertEqual(calculator.distancia_vectorial(a,b),(1.4142135623730951))        
    def test_matriz_hermitian(self):
        a=[[(6, 4), (8, 6)],[(3,5),(6,2)]]
        self.assertEqual(calculator.matriz_hermitian(a),False)
    def test_tensor_vector(self):
        a=[(2,3),(2,3)]
        b=[(3,4),(2,4)]
        self.assertEqual(calculator.tensorVector(a,b),[[(-6, 17), (-8, 14)], [(-6, 17), (-8, 14)]])
    def test_unitaria(self):
        a=[[(4, 6), (6, 4)], [(6, 4), (8, 6)]]
        self.assertEqual(calculator.unitaria(a),False)
    def test_tensor_metrices(self):
        a=[[(6, 4), (8, 6)],[(3,5),(6,2)]]
        b=[[(6, 4), (8, 6)],[(3,5),(6,2)]]
        self.assertEqual(calculator.tensorMatrices(a,b),[[[(20, 48), (24, 68)], [(24, 68), (28, 96)]], [[(-2, 42), (28, 36)], [(-6, 58), (36, 52)]], [[(-2, 42), (-6, 58)], [(28, 36), (36, 52)]], [[(-16, 30), (8, 36)], [(8, 36), (32, 24)]]])
if __name__=="__main__":
    unittest.main()
