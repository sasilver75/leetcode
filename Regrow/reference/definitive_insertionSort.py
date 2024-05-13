"""
Insertion Sort (or Bubble Sort) are interesting
because they're O(N^2) time complexity instead of O(nlogn)
but they're also O(1) memory, in contrast to ones like MergeSort that are O(N) memory

Insertion Sort works similarly to how we might sort cards into our hand
in a card game -- like the dealer might deal out a bunch of facedown cards
to you (unsorted), and then you're inserting them into your hand in a sorted order
as you pick each card up.

We assume that the first card is already sorted.
Then, we select an unsorted card.
If the unsorted card is greater than the card in
hand, it is placed on the right Otherwise, it is placed on the left.

https://www.programiz.com/dsa/insertion-sort
"""

def insertion_sort(array: list[int]) -> list[int]:
    for i in range(1, len(array)):
        key = array[i] # "Extract" the key
        j = i - 1

        # Compare key with each element on the left of it until we find a smaller element
        # This is sort of "holding the insertion cars and scanning backwards to find its location, updating indices' values as it goes"
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1

        # Play key after the element just smaller than it (or equal to, in this case)
        # We've finally found the location where we should insert the card to the right of. Because of how we adjusted the indexes on the was down, it's safe to just overwrite the item to the right.
        array[j+1] = key

    return array

print(insertion_sort([3,2,9,1,4,6,7,5,8])) # 1, 2, 3, 4, 5, 6, 7, 8
print(insertion_sort([1, 0])) # 0, 1