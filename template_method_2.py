from abc import ABC, abstractmethod             

class Pizza(ABC):
    """CLass Abstract"""
    def prepare(self)-> None:
        """Template method"""
        self.hook_before_add_ingredients()
        self.add_ingredientes() # Abstract pode ser diferene para cada tipo de pizza
        self.hook_after_add_ingredients()
        self.cook()# Abstract pode ter tempo diferene
        self.cut() # Concret method
        self.serve()# Concret method

    def hook_before_add_ingredients(self) -> None:
        pass

    def hook_after_add_ingredients(self) -> None:
        pass


    def cut(self) -> None:
        print(f'{self.__class__.__name__} Pizza cortada em 8 pedaços')

    def serve(self) -> None:
        print(f'{self.__class__.__name__} Pizza servida ao cliente')

    @abstractmethod
    def add_ingredientes(self) -> None:pass

    @abstractmethod
    def cook(self) -> None:pass

class AModa(Pizza):
     
    def add_ingredientes(self) -> None:
        print(f'{self.__class__.__name__}, presunto, queijo, cebola e orégado')
    
    def cook(self) -> None:
        print(f'{self.__class__.__name__}, deixar no forno a lenha por 3,5 minutos ')

class Calabresa(Pizza):
     
    def add_ingredientes(self) -> None:
        print(f'{self.__class__.__name__}, calabresa, queijo, cebola e orégado')
    
    def cook(self) -> None:
        print(f'{self.__class__.__name__}, deixar no forno a lenha por 5 minutos ')

class QuatroQueijos(Pizza):
     
    def add_ingredientes(self) -> None:
        print(f'{self.__class__.__name__}, mussarela, catupiry, provolone, gorgonzola e orégado')
    
    def cook(self)-> None:
        print(f'{self.__class__.__name__}, deixar no forno a lenha por 6 minutos ')

class Veg(Pizza):

    def hook_before_add_ingredients(self)-> None:
        print(f'{self.__class__.__name__}, lavar os ingredinetes')
     
    def add_ingredientes(self)-> None:
        print(f'{self.__class__.__name__}, kit ingredientes veganos e orégado')

    def hook_after_add_ingredients(self)-> None:
        print(f'{self.__class__.__name__}, verificar se não tem ingredientes mal posicionados')
        
    
    def cook(self)-> None:
        print(f'{self.__class__.__name__}, deixar no forno a lenha por 2 minutos ')

if __name__ == "__main__":
    pizza_a_moda = AModa()
    pizza_a_moda.prepare()

    print()

    pizza_a_moda = Calabresa()
    pizza_a_moda.prepare()

    print()

    pizza_a_moda = QuatroQueijos()
    pizza_a_moda.prepare()

    print()

    pizza_a_moda = Veg()
    pizza_a_moda.prepare()
    
    