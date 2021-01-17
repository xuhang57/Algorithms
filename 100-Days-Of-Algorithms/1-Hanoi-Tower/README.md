# Hanoi Tower

[Tower of Hanoi - Wikipedia](https://en.wikipedia.org/wiki/Tower_of_Hanoi)
The minimum number number of moves required to solve a Tower of Hanoi puzzle is $2^n -1$, where n is the number of disks.

## Key Idea

**Recursion**: in order to move the largest disk to the right tower, we need to move all disks other than the largest to the middle tower. Therefore, we are dealing the very same problem with one less disk.

## Steps

1. Move [N-1] disks from left to middle tower recursively
2. Move largest disk from left to right tower
3. Move [N-1] disks from middle to right recursively

## Code

* [hanoi_tower.py](https://github.com/xuhang57/Learn-Algorithms/blob/master/100-Days-Of-Algorithms/1-Hanoi-Tower/hanoi_tower.py)

