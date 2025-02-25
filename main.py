# Task 1/150
# 121. Best Time to Buy and Sell Stock

# class Solution:
#     def maxProfit(self, prices):
#         lowest_price = 99999999999999999999
#         max_profit = 0
#         for i in range(len(prices)):
#             if prices[i] < lowest_price:
#                 lowest_price = prices[i]
#             if prices[i] - lowest_price > max_profit:
#                 max_profit = prices[i] - lowest_price
#
#         print(max_profit)
#
# sol = Solution()
# sol.maxProfit(prices = [7,1,5,3,6,4])

# Task 2/150
# 125. Valid Palindrome

# import re
#
#
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = re.sub(r'[-_.,+=&?<>{}[]|/! \]+', '', s)
#
#         for i in range(int(len(s) / 2)):
#             if s[i] != s[-i - 1]:
#                 return False
#         return True
#
#
# sol = Solution()
# print(sol.isPalindrome('ab_a'))


# Task 3/150
# 136. Single Number

# class Solution:
#     def singleNumber(self, nums) -> int:
#         temp = 0
#         for n in nums:
#             temp = temp^n
#
#         return temp
# sol = Solution()
# print(sol.singleNumber([2,2,1]))

# Task 4/150
# 168. Excel Sheet Column Title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26:
            return chr(columnNumber + 64)
        else:
            whole = columnNumber
            output = ''
            if whole % 26 != 0:
                while whole > 26:
                    remainder = whole % 26
                    whole = whole // 26
                    output = chr(remainder + 64) + output

                output = chr(whole + 64) + output
            else:
                whole = whole - 1
                n = 0
                while whole > 26:
                    remainder = whole % 26
                    whole = whole // 26
                    if n == 0:
                        output = chr(remainder + 64 + 1) + output
                    else:
                        output = chr(remainder + 64) + output
                    n += 1

                output = chr(whole + 64) + output

        return output


sol = Solution()
print(sol.convertToTitle(18278))
# print(sol.convertToTitle(27))
