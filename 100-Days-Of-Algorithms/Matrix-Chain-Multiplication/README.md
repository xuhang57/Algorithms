# Matrix Chain Multiplication

[Matrix Chain Multiplication](https://www.wikiwand.com/en/Matrix_chain_multiplication)

[G4G: MCM](https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/)

[Tushar Roy Explanation](https://www.youtube.com/watch?v=vgLJZMUfnsU)

### Key Idea

**Dynamic Programming**. 

Since checking each possible parenthesization (brute force) would require a run-time that is exponential in the number of matrices, which is very slow and impractical for large n. 

A quicker solution to this problem can be achieving by breaking up the problem into a set of related subproblems. By solving subproblems once and reusing the solutions, the require run-time can be reduced.

### Steps

Let MCM denote a function that returns a minimum number of scalar multiplications. Then MCM can be defined as the best split among all possible choices:

$MCM(A_i, \dots, A_n) = min_i MCM(A_i, \dots, A_i) \otimes MCM(A_{i+1}, \dots, A_n)$

Time Complexity: $O(n^3)$  Space Complexity: $O(n^2)$

### Code
