#  Escribe una función que pueda decirte si un número (número entero) es primo o no.

if __name__ == '__main__':

    print("por favor introduzca un número entero positivo")
    number = int(input())

    def calc_primo(number):
        for i in range(2, int(number)):
            if number % i == 0:
                print("El número no es un npumero primo ya que se puede dividir con", i)
                return False
        print("El número es primo")

    calc_primo(number)
