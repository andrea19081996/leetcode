# DIFFICULTY: MEDIUM
#
# Given a signed 32 - bit integer x, return x with its digits reversed.If reversing x causes the value to go outside
# the signed 32-bit integer range[-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64 - bit integers(signed or unsigned).
# Example 1:
# Input: x = 123
# Output: 321
# Example
# 2:
# Input: x = -123
# Output: -321
# Example
# 3:
# Input: x = 120
# Output: 21
#
# Constraints:
# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x >= 0:
            sign = 1
        else:
            sign = -1
            x *= sign

        while x != 0:
            result = result*10 + x%10
            x //= 10

        return 0 if result < (-2 ** 31) or result > (2 ** 31 - 1) else result*sign


if __name__ == '__main__':
    number = 0
    s = Solution()
    result = s.reverse(number)
    print(result)
    pass