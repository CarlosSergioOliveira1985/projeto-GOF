from abc import ABC, abstractmethod
from typing import List

class BoxStruture(ABC):
    """Component"""
    @abstractmethod
    def print_content(self) -> None : pass

    @abstractmethod
    def get_price(self) -> float : pass  

    
    def add(self, child: BoxStruture) -> None : pass

    def remove(self, child: BoxStruture) -> None : pass

   
class Box(BoxStruture):
    """Composite"""   

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStruture] = []
    
    def print_content(self) -> None :
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    
    def get_price(self) -> float :
        return sum([
            child. get_price() for child in self._children
        ])


    def add(self, child: BoxStruture) -> None :
        self._children.append(child)

    def remove(self, child: BoxStruture) -> None :
        if child in self._children:
            self._children.remove(child)

class Product(BoxStruture):
    """leaf"""
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None :
        print(self.name, self.price)
    
    def get_price(self) -> float :
        return self.price

if __name__ == "__main__":

    #leaf

    camiseta1 = Product("Camiseta P", 45.50)
    camiseta2 = Product("Camiseta M", 55.50)
    camiseta3 = Product("Camiseta g", 65.50)

    #composite

    caixa_camisetas = Box('Caixa de camisetas')
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)
    caixa_camisetas.print_content()
    print(caixa_camisetas.get_price())

    #leaf
    
    smartphone1 = Product("Iphone16", 5500.00)
    smartphone2 = Product("Samsung S25fe", 3900.00)
    smartphone3 = Product("Motorola 70 Fusion", 2800.00)

    #composite

    caixa_smartphones = Box('Caixa de smart phones')
    caixa_smartphones.add(smartphone1)
    caixa_smartphones.add(smartphone2)
    caixa_smartphones.add(smartphone3)
    caixa_smartphones.print_content()
    print(caixa_smartphones.get_price())

    
    #composite
    caixa_grande = Box("Caixa Grande")
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_content()
    print(caixa_grande.get_price())
    
    