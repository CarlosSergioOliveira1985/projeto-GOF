from typing import Dict, List
from copy import deepcopy

class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state', state)


    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, name, value):
        raise AttributeError('Sorry, I am Immutable')

class ImageEditor:
    def __init__(self, name: str , width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.heidth = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self) -> None:
        return f'{self.__class__.__name__}({self.__dict__})'

class Caretake:
    def __init__(self, originator: ImageEditor):
        self._originator = originator
        self._mementos: List[Memento] = []

    def beckup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self)-> None:
        if not self._mementos:
            return
        self._originator.restore(self._mementos.pop())


if __name__ == "__main__":
    img = ImageEditor ('FotoMinha.jpg', 500 , 400)
    caretake = Caretake(img)

    caretake.beckup()

    img.name = "FotoNossa"
    img.width = 300
    img.heidth = 200

    caretake.beckup()

    img.name = "FotoNossa2"
    img.width = 200
    img.heidth = 100
    
    caretake.beckup()

    img.name = "FotoNossa3"
    img.width = 100
    img.heidth = 50
    
    caretake.restore()

    print(img)
    
    caretake.restore()

    print(img)
   