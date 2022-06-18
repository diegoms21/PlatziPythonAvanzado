def is_palindrome(string: str) -> bool:
    #si nuestro palindromo es una frase con espacios en blanco, los reemplazamos con la cadena vacia, con lower lo colocamos en minuscula para que si colcoamos algo como Ana, es un palindromo pero la computadora no es igual por que la A mayuscula tiene otro codigo ascii que la a minusacula
    string = string.replace(" ","").lower() 
    return string == string[::-1]
    #compara si un string es igual al mismo string pero invertido, por ejemplo ana == ana (True), pero Ana == anA (False)

def is_primo(number: int) -> bool:

    result_list = [x for x in range(2,number) if number % x == 0]
    return len(result_list) == 0


def run():
    print(is_palindrome(1000))

if __name__ == "__main__":
    #run()
    number = 'hola'
    #number = int(input("Ingrese un numero: "))
    number_is_primo = is_primo(number)
    if number_is_primo:
        print("el numero ingresado {} SI es un numero primo".format(number))
    else:
        print("el numero ingresado {} NO es un numero primo".format(number))

#colocar en la terminal:
# $ mypy palindrome.py --check-untyped-defs