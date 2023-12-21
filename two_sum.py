'''
problem link: https://leetcode.com/problems/two-sum/
'''
class Solution(object):
    def twoSum(self, nums, target):
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]
            hash_table[num] = i
        return []
