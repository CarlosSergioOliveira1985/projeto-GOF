def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class
    


@singleton
class APPSettings:
    def __init__(self):
        self.tema = "O tema escuro"
        self.fonte = '18px'

@singleton
class Teste:
    def __init__(self):
        pass


if __name__ =="__main__":
    as1 = APPSettings()
    as1.tema = 'O tema claro'

    print(as1.tema)
    
    as2 = APPSettings()
   
    print(as2.tema)

    t1 = Teste()
    print(t1)