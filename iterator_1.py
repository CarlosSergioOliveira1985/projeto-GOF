from collections.abc import Iterator, Iterable
from typing import List, Any

class MyIterator(Iterator):
    def __init__(self, collection:List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

class ReverseIterator(Iterator):
    def __init__(self, collection:List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) ->None:
        self._items : List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'

if __name__ == "__main__":

    mylist = MyList()
    mylist.add('Luiz')
    mylist.add('Carlos')
    mylist.add('Helena')
    mylist.add('João')
    mylist.add('Aline')
    mylist.add('Pedro')
    mylist.add('Antonio')
    mylist.add('Maria')
    
    mylist.add(100)
    mylist.add(30.5)
    mylist.add('Pedro Mariano')
    mylist.add(['Carlos', 20, 33345454588444])
   


    print('Peguei um valor', next(mylist.__iter__()))
    print()

    for value in mylist:
        print(value)

    print()


    for value in mylist.reverse_iterator():
        print(value)

    