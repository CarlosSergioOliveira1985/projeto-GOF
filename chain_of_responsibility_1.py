def handler_ABC(letter: str) -> str:
    letters = ['A' , 'B', 'C']

    if letter in letters:
        return f'hendler_ABC: conseguiu tratar o valor {letter}'
    return handler_DEF(letter)

def handler_DEF(letter: str) -> str:
    letters = ['D' , 'E', 'F']

    if letter in letters:
            return f'hendler_DEF: conseguiu tratar o valor {letter}'
    return handler_unsolved(letter)

def handler_unsolved(letter: str) -> str:
     return f'hendler_unsilved: não sei tratar a {letter}'

if __name__ == "__main__":
     print(handler_ABC("A"))
     print(handler_ABC("D"))
     print(handler_ABC("Z"))
