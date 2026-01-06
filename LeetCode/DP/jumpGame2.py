'''
https://leetcode.com/problems/jump-game-ii?envType=problem-list-v2&envId=greedy
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")]*(n)
        dp[0] = 0
        for i in range(1,n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i],dp[j] + 1)
        return dp[n-1]