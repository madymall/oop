def get_list() -> list:
    return list(range(0, 1_000_000_000, 2))

class Solution:

    def find_target(self, list, target):
        steps = 0
        start = 0
        end = len(list)

        while start < end:
            center = (start + end) // 2
            steps += 1

            if target == center:
                return steps

            elif target > center:
                start = center + 1

            else:
                end = center - 1
        return steps

a = Solution().find_target(get_list(), 2_345_678)
print(a)

