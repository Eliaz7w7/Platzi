#Creando palindromo
def palin(palabra):
    palabra=palabra.lower().replace(" ","")
    if palabra[::]==palabra[::-1]:
        return True
    else:
        return False



def run():
    palabra=input("Ingrese la palabra: ")
    paindromo=(palin(palabra))
    if paindromo==True:
        print ("Es palindromo")
    else:
        print("No es palindromo")


if __name__=="__main__":
    run()