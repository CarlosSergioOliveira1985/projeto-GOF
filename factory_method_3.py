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

class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular esta buscado o cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'economico':
            return CarroEconimico()
        if tipo == 'moto':
            return MotoLuxo()
        if tipo == 'moto_popular':
            return MotoPopular()
        assert 0, "Veiculo não existe"

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'economico':
            return CarroEconimico()
        if tipo == 'moto_popular':
            return MotoPopular()
        assert 0, "Veiculo não existe"


if __name__ == '__main__':
    from  random import choice
    veiculos_disponiveis_zona_norte = ['luxo', 'economico', 'moto', 'moto_popular']
    veiculos_disponiveis_zona_sul = [ 'economico','moto_popular']


    
    print('Zona Norte')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print()

    print('Zona Sul')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
        

