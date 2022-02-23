#PALINDROMO

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

