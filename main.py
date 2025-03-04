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
from typing import Optional, List


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

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         if n == 1:
#             return True
#         curr = n
#         summ = 0
#         history = []
#         while summ != 1:
#             summ = 0
#             history.append(curr)
#             for n in range(len(str(curr))):
#                 summ += (curr % 10) ** 2
#                 curr = curr // 10
#             curr = summ
#             if curr in history:
#                 return False
#
#         return True
#
# sol = Solution()
# print(sol.isHappy(19))

# Task 9/150
# 203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         dummy = ListNode(0, head)
#         prev = dummy
#         curr = head
#         while curr is not None:
#             if curr.val != val:
#                 prev = curr
#                 curr = curr.next
#             else:
#                 if curr.next is not None:
#                     prev.next = curr.next
#                     curr = curr.next
#                 else:
#                     prev.next = None
#                     curr = prev
#
#         return dummy.next
#
# sol = Solution()
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(4)))))
# new_head = sol.removeElements(head, 2)
#
# while new_head.next is not None:
#     print(new_head.val)
#     new_head = head.next

# Task 10/150
# 205. Isomorphic Strings

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         s_dict = dict()
#         t_dict = dict()
#         s_new = str()
#         t_new = str()
#
#         n = 0
#         if len(s) != len(t):
#             return False
#         else:
#             for c in s:
#                 if c in s_dict.keys():
#                     s_new = s_new + str(s_dict[c]) + '.'
#                 else:
#                     s_dict[c] = n
#                     n += 1
#                     s_new = s_new + str(s_dict[c]) + '.'
#
#             n = 0
#             for c in t:
#                 if c in t_dict.keys():
#                     t_new = t_new + str(t_dict[c]) + '.'
#                 else:
#                     t_dict[c] = n
#                     n += 1
#                     t_new = t_new + str(t_dict[c]) + '.'
#
#             if t_new == s_new:
#                 return True
#             else:
#                 return False


# sol = Solution()
# print(sol.isIsomorphic('paper', 'title'))

# Task 11/150
# 217. Contains Duplicate

# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         if len(set(nums)) != len(nums):
#             return True
#         else:
#             return False

# Task 12/150
# 228. Summary Ranges

# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         if len(nums) == 0:
#             return []
#         start = nums[0]
#         end = nums[0]
#         ranges = []
#         for i in range(len(nums)):
#             if i != len(nums) - 1:
#                 if nums[i] + 1 != nums[i+1]:
#                     end = nums[i]
#                     if start != end:
#                         ranges.append(f'{start}->{end}')
#                     else:
#                         ranges.append(f'{start}')
#                     start = nums[i+1]
#             else:
#                 end = nums[i]
#                 if start != end:
#                     ranges.append(f'{start}->{end}')
#                 else:
#                     ranges.append(f'{start}')
#
#         return ranges
#
# sol = Solution()
# print(sol.summaryRanges([0,1,2,4,5,7]))

# Task 13/150
# 231. Power of Two

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         n_bin = "{0:b}".format(n)
#         res = 0
#         if n < 1:
#             return False
#         for n in n_bin:
#             if n == '1':
#                 res +=1
#                 if res > 1:
#                     return False
#
#         return True
#
# sol = Solution()
# print(sol.isPowerOfTwo(1))

# Task 14/150
# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)