
from typing import List, Dict

class Cliente:
    """Context"""
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

    # extrinsic adress data
        self.address_number : str
        self.address_complement : str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_complement)

class Address:
    """flyweight"""
    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbouhood = neighbourhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_complement: str ) -> None:
        print(self._street, address_number, self._neighbouhood, address_complement, self._zip_code)

class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self,**kwargs) -> str:
        return ''.join(kwargs.values())
    
    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            addresse_flyweigth = self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            addresse_flyweigth = Address(**kwargs)
            self._addresses[key] = addresse_flyweigth
            print('Criando novo objeto')
        return addresse_flyweigth

if __name__ == "__main__":

    address_factory = AddressFactory ()

    a1 = address_factory.get_address(
        street= 'Brasil', neighbourhood= 'Centro', zip_code= '4185-6000')
    
    a2 = address_factory.get_address(
        street= 'Brasil', neighbourhood= 'Centro', zip_code= '4185-6000')
    
    carlos = Cliente('Carlos')
    carlos.address_number = '50'
    carlos.address_complement ='Casa3'
    carlos.add_address(a1)
    carlos.list_addresses()

    aline = Cliente('Aline')
    aline.address_number = '100'
    aline.address_complement ='ap5'
    aline.add_address(a2)
    aline.list_addresses()


