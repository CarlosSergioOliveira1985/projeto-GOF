from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo esta buscado o cliente...')

class CarroEconimico(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro economico esta buscado o cliente...')

class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo esta buscado o cliente...')


class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'economico':
            return CarroEconimico()
        if tipo == 'moto':
            return MotoLuxo()
        assert 0, "Veiculo não existe"

    def buscar_cliente(self):
        self.carro.buscar_cliente()

if __name__ == '__main__':
    from  random import choice
    carros_disponiveis = ['luxo', 'economico', 'moto']

    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()
        

