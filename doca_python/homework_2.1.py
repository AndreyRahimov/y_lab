"""Надо написать класс CyclicIterator.
Итератор должен итерироваться по итерируемому объекту (list, tuple, set, range,
Range2, и т. д.), и когда достигнет последнего элемента, начинать сначала."""


class CyclicIterator:

    def __init__(self, iterator):
        self.iterator = iterator
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < len(self.iterator) - 1:
            self.position += 1
            return self.iterator[self.position]
        self.position = 0
        return self.iterator[self.position]


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
