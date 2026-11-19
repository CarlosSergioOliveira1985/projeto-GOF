from abc import ABC, abstractmethod

class IControl(ABC):
    @abstractmethod
    def top(self)-> None:pass

    @abstractmethod
    def left(self)-> None:pass

    @abstractmethod
    def down(self)-> None:pass
    
    @abstractmethod
    def rigth(self)-> None:pass

class Control(IControl):
    
    def top(self)-> None:
        print('Movedo para cima')


    def left(self)-> None:
        print('Movedo para esquerda')

    def down(self)-> None:
        print('Movedo para baixo')

    def rigth(self)-> None:
        print('Movedo para direita')

class NewControl:
    
    def move_top(self)-> None:
        print('new Movedo para cima')


    def move_left(self)-> None:
        print('new Movedo para esquerda')

    def move_down(self)-> None:
        print('new Movedo para baixo')

    def move_rigth(self)-> None:
        print('new Movedo para direita')

class ControlAdapter:
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self)-> None:
        self.new_control.move_top()
    
    def left(self)-> None:
        self.new_control.move_left()

    def down(self)-> None:
        self.new_control.move_down()

    def rigth(self)-> None:
        self.new_control.move_rigth()

class ControlAdapter2(Control, NewControl):

    def top(self)-> None:
        self.move_top()
    
    def left(self)-> None:
        self.move_left()

    def down(self)-> None:
        self.move_down()

    def rigth(self)-> None:
        self.move_rigth()

if __name__ == "__main__":

    c1 = Control()
    c1.left()
    c1.rigth()
    c1.top()
    c1.down()

    print()

    c2 = NewControl()
    c1 = ControlAdapter(c2)
    
    
    c1.left()
    c1.rigth()
    c1.top()
    c1.down()

    print()
    
    c3 = ControlAdapter2()
     
    c3.left()
    c3.rigth()
    c3.top()
    c3.down()