# class Meta(type):
#     def __call__(self, *args, **kwargs):
#         print('Call é executado')
#         return super().__call__(*args, **kwargs)

# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('New é ececutado')
#         return super().__new__(cls)

#     def __init__(self, nome):
#         print('init é ececutado')
#         self.nome = nome

#     def __call__(self, x, y):
#         print('call chamado', self.nome, x+y)

# p1 = Pessoa('Carlos')
# print(p1.nome)
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class APPSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = "O tema escuro"
        self.fonte = '18px'


if __name__ =="__main__":
    as1 = APPSettings()
    as1.tema = 'O tema claro'

    print(as1.tema)
    
    as2 = APPSettings()


   
    print(as2.tema)
