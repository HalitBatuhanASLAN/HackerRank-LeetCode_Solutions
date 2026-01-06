'''
https://leetcode.com/problems/house-robber-ii?envType=problem-list-v2&envId=dynamic-programming
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        case_with_h0 = self.classicRobber(n-1,nums[:-1])
        case_without_h0 = self.classicRobber(n-1,nums[1:])

        return max(case_with_h0, case_without_h0)

    def classicRobber(self,n:int,nums:List[int]) -> int:
        if n == 0: return 0
        if n == 1: return nums[0]
        
        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = max(nums[1],dp[0])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        return dp[n-1]