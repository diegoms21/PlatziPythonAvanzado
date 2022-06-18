# Hola 3 - HolaHolahola
# Facundo 2 - FacundoFacundo
# Plazti 4 - PlatziPlatziPlatziPlatzi

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string*n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Amigo"))

def make_division_by(n):
    '''this clousure returns a function that returns the division of an x number by n'''
    def dividendo(integer):
        assert type(integer) == int, "solo debes colocar números"
        return integer / n
    return dividendo

def core():
    
    division_by_3 = make_division_by(3)
    print(division_by_3(18)) #6
    
    division_by_5 = make_division_by(5)
    print(division_by_5(100)) #20

    division_by_18 = make_division_by(18)
    print(division_by_18(54)) #3

if __name__ == "__main__":
    #run()
    core()