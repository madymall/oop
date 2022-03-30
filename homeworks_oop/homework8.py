from array import *

a = array('i', [1, 2, 3, 4])

class Solution:

    def plusOne(digits: list):
        b = list(a)
        b[-1] = b[-1] + 1

        return b

print(Solution.plusOne(a))


