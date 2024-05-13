"""
341 Flatten Nested Iterator

Given a nested list of integers `nestedList`, each element is either an
integer, or a list, whose elements may also be integers or otehr lists.
Implement an iterator to flatten it.
"""
from typing import Union


class FlattenNestedIterator:
    def __init__(self, nestedList: list[Union[int, list]]):
        self.nestedList = nestedList
        self.elements = self._generate_flattened_elements(self.nestedList)
        self.offset = 0

    def _generate_flattened_elements(self, lst: list):
        acc = []
        for element in lst:
            if isinstance(element, int):
                # Int: Just append it
                acc.append(element)
            else:
                # List: Extend the acc with the unpacked elments
                # This should be EXTEND, not APPEND!
                acc.extend(self._generate_flattened_elements(element))

        self.offset = 0
        return acc

    def next(self) -> int:
        element = self.elements[self.offset]
        self.offset += 1
        return element

    def hasNext(self) -> bool:
        return self.offset < len(self.elements)

    def print_elements(self):
        print(self.elements)


nestedList = [[1, 1], 2, [1, 1]]
fni = FlattenNestedIterator(nestedList)
fni.print_elements()
acc = []
while fni.hasNext():
    acc.append(fni.next())
assert acc == [1,1,2,1,1]

nestedList = [1,[4,[6]]]
fni = FlattenNestedIterator(nestedList)
fni.print_elements()
acc = []
while fni.hasNext():
    acc.append(fni.next())
assert acc == [1,4,6]
