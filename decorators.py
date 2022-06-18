#decorador que averigua cuanto tiempo tarda en ejecutarse una funcion 
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos") #totalseconds nos permite obtener la diferencia en segundos
    return wrapper

#hacemos esto solo para ver cuanto tarda un for en dar 1000000 de vueltas
@execution_time
def random_func():
    for _ in range (1,10000000): #cuando no nos intereca el iterador "i" ponemos un "_" como convención
        pass

@execution_time
def suma(a : int, b : int) -> int:
    return a + b

@execution_time
def saludo(nombre = 'cesar'):
    print("hola " + nombre)



#TypeError: wrapper() takes 0 positional arguments but 2 were given
#Pasa que wrapper no tiene parametros pero cuando le paso al decorador la funcion suma esta tiene 2 parametros que neceistan ejecutarse, entonces podria poner wrapper(a,b) y a func(a,b) pero eso haria que mi funcion decorador este limitada a un tipo de función con 2 parametros, para evitar ese problema usaremos *args y **kwargs
# *args -- no importa la cantidad de argumentos posicionales que se le envien, la funcion los va a recibir
# *kwargs -- no importa la cantidad de argumentos nombrados, la funcion los va a recibir
# el * es el operador de desusctructuracion de python

# argumentos posicionales son por ejemplo en def suma(a,b) y argumentos nombrados son x ejemplo saludo(nombre='cesar') donde si no le paso el nombre, toma el nombre x defecto de cesar

if __name__ == "__main__":
    random_func()
    suma(5,5)
    saludo('Diego')