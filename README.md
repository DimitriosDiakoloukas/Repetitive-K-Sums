# Repetitive-K-Sums
My take on the repetitive K-Sums Recursion Problem.

PROBLEM

Alice thinks of a non-decreasing sequence of non-negative integers and wants Bob to guess it by providing him the set of all its K-sums with repetitions.
What is this? Let the sequence be {A[1], A[2], ..., A[N]} and K be some positive integer that both Alice and Bob know. Alice gives Bob the set of all possible values that can be genereated by this - A[i1] + A[i2] + ... + A[iK], where 1 ≤ i1 ≤ i2 ≤ ... ≤ iK ≤ N. She can provide the values generated in any order she wishes to. Bob's task is to restore the initial sequence.
Consider an example. Let N = 3 and K = 2. The sequence is {A[1], A[2], A[3]}. The sequence of its 2-sums with repetitions is {A[1] + A[1], A[1] + A[2], A[1] + A[3], A[2] + A[2], A[2] + A[3], A[3] + A[3]}. But its elements could be provided in any order. For example any permutation of {2, 3, 4, 4, 5, 6} corresponds to the sequence {1, 2, 3}
The total number of elements in any input sequence does not exceed 105
Each element of each input sequence is non-negative integer not exceeding 1018.
Each input sequence is a correct sequence of all K-sums with repetitions of some non-decreasing sequence of non-negative integers.
