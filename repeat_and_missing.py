# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        a, b = 0, 0
        d = dict([[i, 0] for i in range(1, n + 1)])
        for i in A:
            if d[i] == 1:
                a = i
            else:
                d[i] = 1
        b = sum(A) - ((n * (n + 1)) // 2) - a
        return [a, -1 * b]
