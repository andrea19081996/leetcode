# DIFFICULTY: MEDIUM
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
#
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

class Solution:
    def change_direction(self, actual_row):
        if actual_row == 1:
            increment = 1
            is_diagonal = False
        else:
            increment = -1
            is_diagonal = True
        return increment, is_diagonal

    def convert(self, s: str, numRows: int) -> str:
        actual_row = 1
        increment = 1
        is_diagonal = False
        split_by_row = {}
        for letter in s:
            split_by_row[str(actual_row)] = split_by_row.get(str(actual_row), "") + letter
            actual_row += increment
            if not is_diagonal and actual_row > numRows:
                actual_row = max(numRows - 1, 1)
                increment, is_diagonal = self.change_direction(actual_row)

            elif is_diagonal and actual_row == 1:
                actual_row = 1
                increment, is_diagonal = self.change_direction(actual_row)


        res = ""
        for order_line in split_by_row.keys():
            res += split_by_row[order_line]
        return res

if __name__ == '__main__':
    solution = Solution()
    result = solution.convert(s="PAYPALISHIRING", numRows=3)
    # result = "PAHNAPLSIIGYIR"
    print(result)