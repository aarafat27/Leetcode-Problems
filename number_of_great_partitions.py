'''
problem link: https://leetcode.com/problems/number-of-great-partitions/
'''
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        n = len(nums)
        
        @cache
        def dp(i,cur):
            if i==n:
                return 1

            # do not include the current nums[i]
            remove = dp(i+1,cur)
            keep = 0

            # include the current nums[i]
            if cur+nums[i]<k:
                keep =  dp(i+1,cur+nums[i])
            return remove+keep

        invalid_partitions = dp(0,0)
        res = pow(2,n) - invalid_partitions*2
        return max(res,0) % mod
