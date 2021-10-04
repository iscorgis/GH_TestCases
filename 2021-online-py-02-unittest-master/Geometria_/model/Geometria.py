
class Geometria:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.figuraName = ""

    def areaCuadrado(self, n):
        return n * n

    def areaCirculo(self, r):
        PI = 3.1416
        return PI * pow(r, 2)

    def areaTiangulo(self, a, b):
        return (a * b)/2

    def areaRectangulo(self, a, b):
        return a * b

    def areaPentagono(self, p, a):
        return (p * a)/2

    def areaRombo(self, d, d_):
        return (d * d_)/2

    def areaRomboide(self, b, h):
        return b * h

    def areaTrapecio(self, b, b_, h):
        return ((b + b_)/2)*h


    def set_figuraName(self, case):
        if case == 1:
            self.figuraName = "Cuadrado"
        if case == 2:
            self.figuraName = "Circulo"
        if case == 3:
            self.figuraName = "Triangulo"
        if case == 4:
            self.figuraName = "Rectangulo"
        if case == 5:
            self.figuraName = "Pentagono"
        if case == 6:
            self.figuraName = "Rombo"
        if case == 7:
            self.figuraName = "Romboide"
        if case == 8:
            self.figuraName = "Trapecio"

    # Selector de figuras
    def switch(self, case):
        sw = {
            1: self.areaCuadrado(self.a),
            2: self.areaCirculo(self.a),
            3: self.areaTiangulo(self.a, self.b),
            4: self.areaRectangulo(self.a, self.b),
            5: self.areaPentagono(self.a, self.b),
            6: self.areaRombo(self.a, self.b),
            7: self.areaRomboide(self.a, self.b),
            8: self.areaTrapecio(self.a, self.b, self.c)
        }
        return sw.get(case)

