from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN esta buscado o cliente...')

class CarroEconimicoZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro economico ZN esta buscado o cliente...')

class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZN esta buscado o cliente...')

class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZN esta buscado o cliente...')

class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZS esta buscado o cliente...')

class CarroEconimicoZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro economico ZS esta buscado o cliente...')

class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZS esta buscado o cliente...')

class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZS esta buscado o cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo:
        pass
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular:
        pass
    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo:
        pass
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular:
        pass

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroEconimicoZN()
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return CarroEconimicoZN()
    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return CarroEconimicoZN()
    
class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroEconimicoZS()
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return CarroEconimicoZS()
    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return CarroEconimicoZS()

class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()        

    
if __name__ == '__main__':
  Cliente = Cliente()
  Cliente.busca_clientes()
        

