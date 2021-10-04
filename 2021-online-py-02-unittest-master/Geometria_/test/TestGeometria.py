import os
import unittest
from unittest import mock

from Geometria_.model.Geometria import Geometria as g
from Geometria_.view.View import View
from Geometria_             import main

class TestGeometria(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('setUpClass() -> OK')
        self.obj_geometria_1 = g(1, 2, 3)
        self.obj_geometria_2 = g(12, -1, 100)
        self.obj_geometria_3 = g(1.2, -2.2, 33)

    #Data definition for test cases
    def setUp(self):
        print('SetUp()  -> OK')
        self.r = 0
        self.r_a = []
        self.obj_geometria_1 = g(1, 2, 3)
        self.obj_geometria_2 = g(12, -1, 100)
        self.obj_geometria_3 = g(1.2, -2.2, 33)
        self.obj_geometria_4 = g(1, 2, 3)

        self.valores_a = [1, 2, 3, 4, 5, 6, 7, 8]
        self.valores_b = [2, 3, 5, 6, 7, 2, 6, 1]
        self.valores_sw = [range(1,8)]

        self.figuras = {1 : "Cuadrado",2 : "Circulo",3 : "Triangulo",4 : "Rectangulo",5 : "Pentagono",6 : "Rombo",7 : "Romboide",8 : "Trapecio"}

    ###Test cases for each geometric form of the model
    def test_areaCuadrado(self):
        r = g.areaCuadrado(self,self.obj_geometria_1.a)
        #r_2 = g.areaCuadrado(self,self.obj_geometria_3.b)

        self.assertEqual(r, self.obj_geometria_1.a * self.obj_geometria_1.a)
        #self.assertEqual(r_2, self.obj_geometria_3.b * self.obj_geometria_3.b)
        print('test_areaCuadrado() - > OK')


    def test_areaCirculo(self):
        PI = 3.1416
        #Calculamos de forma manual el area para evaluarlo
        aux_res = [PI * pow(n,2) for n in self.valores_a]
        r_a = [g.areaCirculo(self,n) for n in self.valores_a]
        self.assertEqual(r_a,aux_res)

        print('test_areaCirculo() - > OK')

    def test_areaTiangulo(self):
        r = g.areaTiangulo(self,self.obj_geometria_1.a,self.obj_geometria_1.b)
        self.assertEqual(r, (self.obj_geometria_1.a * self.obj_geometria_1.b) / 2.0 )
        print('test_areaTiangulo() - > OK')


    def test_areaRectangulo(self):
        aux_res = [n[0] * n[1] for n in zip(self.valores_a,self.valores_b )]
        r_a = [g.areaRectangulo(self,n[0],n[1] ) for n in zip(self.valores_a, self.valores_b)]
        self.assertEqual(r_a, aux_res)
        print('test_areaRectangulo() - > OK')

    def test_areaPentagono(self):
        aux_res = [(n[0] * n[1]) / 2.0 for n in zip(self.valores_a, self.valores_b)]
        r_a = [g.areaPentagono(self, n[0], n[1]) for n in zip(self.valores_a, self.valores_b)]
        self.assertEqual(r_a, aux_res)
        print('test_areaPentagono() - > OK')

    def test_areaRombo(self):
        aux_res = [(n[0] * n[1]) / 2.0 for n in zip(self.valores_a, self.valores_b)]
        r_a = [g.areaRombo(self, n[0], n[1]) for n in zip(self.valores_a, self.valores_b)]
        self.assertEqual(r_a, aux_res)
        print('test_areaRombo() - > OK')


    def test_areaRomboide(self):
        aux_res = [(n[0] * n[1]) for n in zip(self.valores_a, self.valores_b)]
        r_a = [g.areaRomboide(self, n[0], n[1]) for n in zip(self.valores_a, self.valores_b)]
        self.assertEqual(r_a, aux_res)
        print('test_areaRomboide() - > OK')


    def test_areaTrapecio(self):
        aux_res = [ ( ( ( n[0] + n[1]) / 2.0) * self.obj_geometria_2.a ) for n in zip(self.valores_a, self.valores_b)]
        r_a = [g.areaTrapecio(self, n[0], n[1],self.obj_geometria_2.a) for n in zip(self.valores_a, self.valores_b)]
        self.assertEqual(r_a, aux_res)
        print('test_areaTrapecio() - > OK')

    def test_init(self):
        r = g(1, 2, 3)
        self.assertEqual(r.a, self.obj_geometria_1.a)
        print('test_init() - > OK')

    def test_figuraname(self):

        for n in self.figuras:
            self.obj_geometria_3.set_figuraName(n)
            self.assertEqual(self.obj_geometria_3.figuraName, self.figuras[n])
            print('test_figuraname_{0}() - > OK'.format(self.figuras[n]))
            print('test_figuraname() - > OK')

    def test_switch(self):
        for n in self.valores_sw:
            self.assertEqual(self.obj_geometria_4.switch(n), self.obj_geometria_1.switch(n))
            print('test_switch_Opcion Menu :: {0} () - > OK'.format(n))

    #Test view file falidation
    def testView(self):
        v = View()
        result = v.select(self.obj_geometria_1)
        self.assertEqual(result, 0)

    def testMain(self):
        result = os.system("python main.py")
        self.assertEqual(result, 0)

    #Release Resources
    def tearDown(self):
        del self.r
        del self.r_a
        del self.obj_geometria_1
        del self.obj_geometria_2
        del self.obj_geometria_3
        print('tearDown() - > OK')


if __name__ == '__main__':
    unittest.main()