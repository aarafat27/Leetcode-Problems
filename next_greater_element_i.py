'''
problem link: https://leetcode.com/problems/next-greater-element-i/
'''
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [next_greater.get(num, -1) for num in nums1]
