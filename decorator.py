from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict 
from copy import deepcopy

#Ingredients

@dataclass
class Ingredient:
    price: float

@dataclass
class Bread(Ingredient):
    price: float = 1.50
@dataclass
class Sausage(Ingredient):
    price: float = 3.50
@dataclass
class Bacon(Ingredient):
    price: float = 2.25
@dataclass
class Egg(Ingredient):
    price: float = 1.50
@dataclass
class PotatoSticks(Ingredient):
    price: float = 2.30
@dataclass
class MashedPotatoes(Ingredient):
    price: float = 3.40
@dataclass
class Chease(Ingredient):
    price: float = 4.10

# Hotdogs

class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]),2)
    
    @property
    def name(self) -> str:
        return self._name
    @property
    def ingredient(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}({self.price}) -> {self._ingredients}'
        



class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name : str = 'SimpleHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]

class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name : str = 'SpecialHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks(), 
            Bacon(),
            Egg(),
            MashedPotatoes(),
            Chease()
        ]

#decorators

class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog) -> None:
        self.hotdog = hotdog 

    @property
    def price(self) -> float:
        return self.hotdog.price
    
    @property
    def name(self) -> str:
        return self.hotdog.name
    @property
    def ingredient(self) -> List[Ingredient]:
        return self.hotdog.ingredients

class BaconDecorator(HotdogDecorator):
    def __init__(self, hotdog: Hotdog) -> None:
        super().__init__(hotdog)

        self._ingredient = Bacon()
        self._ingredients = deepcopy(self.hotdog._ingredients)
        self._ingredients.append(self._ingredient)


    @property
    def price(self) -> float:
        return round(sum([
                    ingredient.price for ingredient in self._ingredients
                ]),2)
    
    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'
    @property
    def ingredient(self) -> List[Ingredient]:
        return self._ingredients

   
if __name__ == "__main__":

    # print()

    # simple_hotdog = SimpleHotdog()
    # print(simple_hotdog)

    # print()

    # special_hotdog = SpecialHotdog()
    # print(special_hotdog)

    print()

    simple_hotdog = SimpleHotdog()
    decorated_simple_hotdog = HotdogDecorator(simple_hotdog)
    bacon_simple_hotdog = BaconDecorator(simple_hotdog)
    bacon_simple_hotdog = BaconDecorator(bacon_simple_hotdog)
    print(simple_hotdog)

    print()

    print(bacon_simple_hotdog)

    print()