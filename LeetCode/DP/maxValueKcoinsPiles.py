'''
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles?envType=problem-list-v2&envId=dynamic-programming
'''

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k + 1)
        for pile in piles:
            n = len(pile)
            cumulatif_pile = [0] * (n + 1)
            for i in range(n):
                cumulatif_pile[i + 1] = pile[i] + cumulatif_pile[i]
            
            # toplam kaç kart alacağız
            for j in range(k,0,-1):
                for x in range(1,min(n,j) + 1):
                    dp[j] = max(dp[j],dp[j-x] + cumulatif_pile[x])
        return dp[k]