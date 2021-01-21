# Next Permutation

[Total Ordered Set](https://www.wikiwand.com/en/Total_order)

[Leetcode: Next Permutation](https://leetcode.com/problems/next-permutation/)

## Key Idea

Array, and specific algorithm.

## Steps

The algorithm has four steps:

1. Find the longest decreasing sequence starting from the end.
2. Again, once we have found the sequence, starting from the end, find the smallest element that is larger than the precede element, denote as smallestHigher.
3. Swap the precede element and the smallestHigher.
4. Reverse the sequence after the precede element.

## Code

[Next Permutation](https://github.com/xuhang57/Learn-Algorithms/blob/master/100-Days-Of-Algorithms/3-Next-Permutation/next_permutation.py)
