
# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
# y otra función que calcule el área de un círculo recibiendo el radio del mismo.
if __name__ == '__main__':
    print("por favor introduzca la base del triangulo deseado")
    base = float(input())
    print("por favor introduzca la altura del trinagulo deseado")
    altura = float(input())
    print("por favor introduzca el radio del circulo deseado")
    radio = float(input())

    def calculoTriangulo(base, altura):
        if base >= 0 and altura >= 0:
            AreaTriangulo = (base * altura) / 2
            print("El parea del triangulo es: " + str(AreaTriangulo))
        else:
            print("los valores de base y altura deben de ser positivos")

    def calculoCirculo(radio):
        if radio >= 0:
            AreaCirculo = 3.1416 * (radio * radio)
            print("El área del cirvulo es : " + str(AreaCirculo))
        else:
            print("El radio debe de ser positivo")

    calculoTriangulo(base, altura)
    calculoCirculo(radio)
