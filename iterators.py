import time

class FiboIter():

    def __init__(self, max_itarations:int = None):
        self.max_itarations = max_itarations

    def __iter__(self): 
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
    
            if self.counter <= self.max_itarations:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                #la tecnica se conoce como swapping
                self.n1 , self.n2 = self.n2 , self.aux
                self.counter += 1
                return self.aux
            else:
                raise StopIteration

        

if __name__ == "__main__":
    finonacci = FiboIter(50)
    for element in finonacci:
        print(element)
        time.sleep(0.05)

#Al hacer el "for i in range", el programa ya reconoce los metodos __iter__ y __next__ y los usa para calcular los siguientes elementos en la iteración