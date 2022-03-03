# Creando palindromo
def palin(palabra):
    palabra = palabra.lower().replace(" ", "")
    if palabra[::] == palabra[::-1]:
        return True
    else:
        return False


def run():
    palabra = input("Ingrese la palabra: ")
    paindromo = (palin(palabra))
    if paindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    run()


# Numeros primos

def run(divi,divisor,cont):
    while divisor < divi:
        divisor = divisor+1
        if divi % divisor == 0 and divi//divisor <= divi:
            cont = cont+1
    if cont == 2:
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run(int(input("Ingrese un numero: ")),0,0)

