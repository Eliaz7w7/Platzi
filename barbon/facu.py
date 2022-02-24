# PALINDROMO

def palin(palabra):
    palabra=palabra.replace(" ","").lower()
    if palabra[::]==palabra[::-1]:
        return True
    else:
        return False

def run():
    palabra=input("Ingrese palabra: ")
    es_palin=palin(palabra)
    if es_palin==True:
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__=="__main__":
    run()
    print()

# PRIMOS

def run():
    divi = int(input("Ingrese un numero: "))
    disor = 0
    cont = 0

    while disor < divi:
        disor = disor+1
        if divi % disor == 0 and divi//disor <= divi:
            cont = cont+1
    if cont == 2:
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()
    print()