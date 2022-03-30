arr = 123456

class Solution:

    def plusOne(digits):

        b = [int(i) for i in str(arr)]
        b[-1] = b[-1] + 1

        return b

print(Solution.plusOne(arr))



