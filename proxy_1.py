from abc import ABC, abstractmethod
from time import sleep
from typing import Dict, List

class IUser(ABC):
    """ Subject interface"""
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass

    
class RealUser(IUser):
    """Real Subject"""
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)
        self.firstname = firstname
        self.lastname = lastname

    
    def get_addresses(self) -> List[Dict]:
        sleep(2)    
        return[
            {
                'rua': 'Brasil', 'numero': '500'
            }
        ]
    
    def get_all_user_data(self) -> Dict:
        sleep(2)
        return{
            'cpf': '111.011.111-01',
            'rg': '1144488816'
        }

class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self._real_user: RealUser
        self._cached_adresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr (self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

   
    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr (self, '_cached_adresses'):
            self._cached_adresses = self._real_user.get_addresses()

        return self._cached_adresses
        
    
    def get_all_user_data(self) -> Dict:
        self.get_real_user()
        
        if not hasattr (self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == "__main__":
    carlos = UserProxy('Carlos', "Oliviera")


    print(carlos.firstname)
    print(carlos.lastname)
    print(carlos.get_all_user_data())
    print(carlos.get_addresses())

    print('Usando o cached de dados')
    
    for i in range(50):
        print(carlos.get_addresses())        

        

    
