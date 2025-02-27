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
# 169. Majority Element
import collections


# class Solution:
#     def majorityElement(self, nums) -> int:
#         d = collections.defaultdict(int)
#         for n in nums:
#             d[n] += 1
#
#         d = sorted(d.items(), key=lambda x:x[1])
#
#         return d[-1][0]
#
#
# sol = Solution()
# print(sol.majorityElement([2, 2, 3]))
# # print(sol.convertToTitle(27))

# Task 5/150
# 171. Excel Sheet Column Number

# class Solution:
#     def titleToNumber(self, columnTitle: str) -> int:
#         title = reversed(columnTitle)
#         res = 0
#         n = 0
#         for c in title:
#             res += 26 ** n * (ord(c) - 64)
#             n += 1
#
#         return res
#
#
# sol = Solution()
# print(sol.titleToNumber('AAAB'))

# Task 6/150
# 191. Number of 1 Bits

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         bin = '{0:b}'.format(n)
#         res = 0
#         for n in bin:
#             if n == '1':
#                 res +=1
#
#         return res
#
#
# sol = Solution()
# print(sol.hammingWeight(128))

# Task 7/150
# 168. Excel Sheet Column Title

# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         res = ''
#         whole = columnNumber
#         remainder = 0
#         while whole > 26:
#             remainder = whole % 26
#             whole = whole // 26
#             if remainder != 0:
#                 res = chr(remainder + 64) + res
#             else:
#                 res = chr(26 + 64) + res
#                 whole -= 1
#
#         res = chr(whole + 64) + res
#         return res
#
#
# sol = Solution()
# print(sol.convertToTitle(52))

# Task 8/150
# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        curr = n
        summ = 0
        history = []
        while summ != 1:
            summ = 0
            history.append(curr)
            for n in range(len(str(curr))):
                summ += (curr % 10) ** 2
                curr = curr // 10
            curr = summ
            if curr in history:
                return False

        return True

sol = Solution()
print(sol.isHappy(19))
