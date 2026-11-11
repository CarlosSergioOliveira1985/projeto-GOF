
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple



class Light:

    """Receiver"""
    def __init__(self, name: str, room_name: str) -> None :
        self.name = name
        self.room_name = room_name
        self.color = "Defaut color"

    def on(self)-> None:
        print(f'{self.name} no {self.room_name} entá ON')

    def off(self) -> None:
        print(f'{self.name} no {self.room_name} está OFF')

    def change_color(self, color: str) ->None:
        self.color = color
        print(f'{self.name} no {self.room_name} is now {self.color}')


class ICommand(ABC):
    """ Interface de Comando"""
    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    """ comando concreto"""
    def __init__(self, light: Light) -> None:
        self.light = light
   
    def execute(self) -> None:
        self.light.on()
    
    def undo(self) -> None:
        self.light.off()

class LightColor(ICommand):
    """ comando concreto"""
    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color
   
    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)
        

    def undo(self) -> None:
        self.light.change_color(self._old_color)
    
  
class RemoteController:
    """ Invoker"""

    def __init__(self) -> None:
        self._buttons: Dict [str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def button_add_command(self, name:str, command:ICommand)->None:
        self._buttons[name] = command

    def button_pressed(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))


    def button_pressed_again(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    def global_undo(self) -> None:
        if not self._undos:
            return None

        button_name, action = self._undos[-1]

        if action == "execute":
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()
        self._undos.pop()


if __name__ == "__main__":

    bedroom_ligth = Light('Luz', 'Quarto')
    bathroom_ligth = Light('Luz', 'Banheiro')

    bedroom_ligth_on = LightOnCommand(bedroom_ligth)
    bathroom_ligth_on = LightOnCommand(bathroom_ligth)
    bedroom_ligth_blue = LightColor(bedroom_ligth, 'blue')
    bedroom_ligth_red = LightColor(bedroom_ligth, 'red')
    bedroom_ligth_yellow = LightColor(bedroom_ligth, 'yellow')
    

    remote = RemoteController()

    remote.button_add_command('first_button', bedroom_ligth_on)
    remote.button_add_command('second_button', bathroom_ligth_on)
    remote.button_add_command('color_button', bedroom_ligth_blue)
    remote.button_add_command('color_two_button', bedroom_ligth_red)
    remote.button_add_command('color_three_button', bedroom_ligth_yellow)


    remote.button_pressed('first_button')
    remote.button_pressed_again('first_button')
    remote.button_pressed('second_button')    
    remote.button_pressed_again('second_button')
    remote.button_pressed('color_button')
    remote.button_pressed('color_two_button')
    remote.button_pressed('color_three_button')
    remote.button_pressed_again('color_button')

    print()

    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    
   

