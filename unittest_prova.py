from solucio3 import *
from solucio4 import *
import unittest

class TestProva03(unittest.TestCase):
    
    def test1(self):
        
        '''
        Funció per comprovar si el resultat de la funció 
        es la mateixa que la prova que hem fet
        '''
        
        resultat = trobar_min_max_rendiment(10, 2, 3)
        self.assertEqual(resultat, (2.0, 10.0))
    
    def test2(self):
        
        '''
        Funció per comprovar si el resultat de la funció 
        es la mateixa que la prova que hem fet
        ''' 
        
        resultat = comptar_estudiants(notes_estudiants)
        self.assertEqual(resultat, 4)
    
    def test3(self):
        
        '''
        Funció per comprovar si el resultat de la funció 
        es la mateixa que la prova que hem fet
        ''' 
        
        resultat = comptar_estudiants_materia(notes_estudiants, "Matemàtiques")
        self.assertEqual(resultat, 3)
    
class TestProva04(unittest.TestCase):
    
    def test4(self):
        
        '''
        Funció per comprovar si el resultat de la funció 
        es un True
        ''' 
        
        resultat = cercar_el(m_ex, 6, True)
        self.assertTrue(resultat, (True, None))
    
    def test5(self):
        
        '''
        Funció per comprovar si el resultat de la funció 
        es un True
        ''' 
        
        resultat = sumar_fila(m_ex)
        self.assertTrue(resultat, None)
    
    def test6(self):
        
        '''
        Funció per comprovar si el resultat de la funció 
        es la mateixa que la prova que hem fet
        ''' 
        
        resultat = sumar_matriu(m_ex)
        self.assertEqual(resultat, 45)
    
    def test7(self):
        
        '''
        Funció per comprovar si el resultat de la funció 
        es la mateixa que la prova que hem fet
        ''' 
        
        resultat = transformar(m_ex, 10, "+")
        self.assertEqual(resultat, None)
    
if __name__ == "__main__":
    unittest.main()