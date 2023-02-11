"""
Rotate Image

Given an n*n 2D matrix representing an image, rotate the image by 90 degrees (clockwise)

You have to rotate the image in-place, meaning you have to modify the input 2D matrix directly!
DO NOT allocate another 2D matrix and do the rotation.

"""

"""

5   1   9   11              15  13  2   5
2   4   8   10      ->      14  3   4   1
13  3   6   7               12  6   8   9
15  14  12  16              16  7   10  11


So imagine that we had a magical do_rotate(...) function that, given a row/col, did the correct
mutative rotation, finding the right cells, etc.

If we did have that, which cells would we call it on?

_   _   _   .     
.   _   .   .      
.   .   .   .               
.   .   .   .

So we called it on the _ cells, and the . are ones that had the correct value rotated to them

What if we had a 5x5?

1   2   3   4   5           21  16  11  6   1
6   7   8   9   10          22  17  12  7   2
11  12  13  14  15      ->  23  18  13  8   3
16  17  18  19  20          24  19  14  9   4
21  22  23  24  25          25  20  15  10  5


_   _  _  _   .
.   _  _  .    .          
.  .  13   .    .      
.  .   .   .    .          
.  .   .   .    .          


So I think we can use four pointers
    TL              TR
ST  1   2   3   4   5       
    6   7   8   9   10          
    11  12  13  14  15      
    16  17  18  19  20          
SB  21  22  23  24  25          

So I think we call rotate() on the ST'th row, from [TL,TR)
then recurse, moving ST/SB and TL/TR closer. We do this while ST!=SB

       TL       TR
    _   _   _   _   .       
ST  .   7   8   9   .          
    .   12  13  14  .      
SB  .   17  18  19  .          
    .   .   .   .   .
    
AGAIN

              TL/TR
        _   _   _   _   .       
        .   _   _   .   .          
ST/SB   .   .  13  .   .      
        .   .   .   .   .          
        .   .   .   .   .

Great, done! :)


So given a cell, how do we determine the four cells that are going to be involved in the swap?

              TL/TR
        _   _   _   _   .       
        .   []   _   .   .          
ST/SB   .   .  13  .   .      
        .   .   .   .   .          
        .   .   .   .   .
        
Say we were targeting this one?
The "offset" is 1

So we want: 
    - A: Our called cell
    - B: Same row, last cell minus offset
    - C: Same col as B, last row minus offset 
    - D: Same row as C, first cell plus offset
    
Then given [A, B, C, D]

we need to do a rotation 

How do we do a rotation of four values?

a=1           a=4
b=2           b=1
c=3     ->    c=2
d=4           d=3


The direction of iteration and the direction of looking/assignment

[a]       b


c         d


Save the topLeft value as temp
move bottomLeft value into topLeft location
move bottomRight value into bottomLeft location
move topRight value into bottomRight location
move temp value into the topRight location

So we just need to have our [A,B,C,D] arrange such that this becomes easy! 

"""


def rotate(matrix: list[list[int]]) -> None:
    ...


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]][[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]][[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(matrix)
assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
