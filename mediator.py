from abc import ABC, abstractmethod
from typing import List

class Colleague(ABC):
    def __init__(self):
        self.name: str 

    @abstractmethod
    def broadcast(self, msg: str) -> None: pass
    
    @abstractmethod
    def direct(self, msg: str) -> None: pass

class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None: 
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        print(msg)

class Mediator(ABC):
    
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None:pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:pass


class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: list[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues


    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self,colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)            

    
    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return
        print(f'{colleague.name} disse: {msg}')
    
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return

        receiver_obj: List[Colleague] = [   
            colleague for colleague in self.colleagues
            if colleague.name == receiver
            ]
    

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}'
        )
        
if __name__ == "__main__":
    chat = Chatroom()

    carlos = Person('Carlos', chat)
    aline = Person('Aline', chat)
    helena = Person('Helena', chat)
    pedro = Person('Pedro', chat)

    chat.add(carlos)
    chat.add(aline)
    chat.add(helena)
    chat.add(pedro)

    print()

    carlos.broadcast('Oi como vocês estão ?')
    aline.broadcast('Estou bem !')

    print()

    carlos.send_direct("Aline", "Oi você está me Aula?")
    aline.send_direct("Carlos", "Não, estou jogando")

    print()