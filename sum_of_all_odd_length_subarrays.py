'''
problem link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
'''
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if (j - i + 1) % 2 == 1:
                    total_sum += sum(arr[i:j+1])
        return total_sum
