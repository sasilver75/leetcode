"""
Flatten Nested Iterator

You are given a list of integers `nestedList`

Each element is EITHER an integer or a list whose elements may be integers
or other lists.

Implemenet an iterator to flatten it!

--

Implement the `NestedIterator` class:
    * NestedIterator(List<NestedInteger> nestedList)
        Initializes the iterator with the nested list `nestedList`
    * `int next()`
        Returns the next INTEGER in teh nested list
    * `boolean hasNext()`
        Returns `true` if there are still some integers in the nested
        list and `false otherwise

Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res

if `res` matches the expected flattened list, then your code will be
judged as correct!


"""
from typing import Union


class NestedIterator:
    def __init__(self, nums: list[Union[int, list]]):
        self.nums = self._process(nums)  # flatten eagerly into an un-nested list
        self.i = 0

    def _process(self, nums) -> list[int]:
        acc = []

        def _process_helper(target: Union[int, list]):
            # After being called on a target, appends the target to acc. If it's a list, recursively append that list to acc.
            if isinstance(target, int):
                acc.append(target)
            else:
                for elt in target:
                    _process_helper(elt)

        for element in nums:
            _process_helper(element)

        return acc

    def hasNext(self) -> bool:
        return self.i < len(self.nums)

    def next(self) -> int:
        # Should we raise exception perhaps if there isn't a next value to return?
        if self.i >= len(self.nums):
            return None
        res = self.nums[self.i]
        self.i += 1
        return res


# === Test Zone ===
# Case 1
nestedList = [[1, 1], 2, [1, 1]]
iterator = NestedIterator(nestedList)
res = []
while iterator.hasNext():
    res.append(iterator.next())
print(res)
assert res == [1, 1, 2, 1, 1]

# Case 2
nestedList = [1, [4, [6]]]
iterator = NestedIterator(nestedList)
res = []
while iterator.hasNext():
    res.append(iterator.next())
print(res)
assert res == [1, 4, 6]
