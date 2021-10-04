
class View:

    def select(self, object):
        print("Selecciona acción:------------------\n"
              "1: Calcular Área del Cuadrado\n"
              "2: Calcular Área del Circulo\n"
              "3: Calcular Área del Triangulo\n"
              "4: Calcular Área del Rectangulo\n"
              "5: Calcular Área del Pentagono\n"
              "6: Calcular Área del Rombo\n"
              "7: Calcular Área del Romboide\n"
              "8: Calcular Área del Trappecio\n")

        case = int(input("Seleccione una opcion: "))
        object.set_figuraName(case)
        print("Opcion seleccionada: ", case)
        print(object.figuraName)
        result = object.switch(case)

        print("Resultado del área del " + object.figuraName + " es: " + str(result) + " mm2")