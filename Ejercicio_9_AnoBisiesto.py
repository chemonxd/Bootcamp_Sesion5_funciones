# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

if __name__ == '__main__':

    print("por favor ingrese el año deseado")
    year = int(input())

    def is_leap_year(year):
        if year % 4 == 0 and (year % 100 or not year % 400):
            print("este es un año bisiseto")
        else:
            print("este año no es bisiesto")

    is_leap_year(year)

