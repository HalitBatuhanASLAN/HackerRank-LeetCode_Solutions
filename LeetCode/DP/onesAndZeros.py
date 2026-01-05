'''
https://leetcode.com/problems/ones-and-zeroes?envType=problem-list-v2&envId=dynamic-programming
'''

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(size + 1)]
        for i in range(1,size + 1):
            s = strs[i-1]
            zeros = s.count('0')
            ones = s.count('1')
            for z in range(0,m+1):
                for o in range(0,n + 1):
                    dp[i][z][o] = dp[i-1][z][o]
                    if z >= zeros and o >= ones:
                        take_it = 1 + dp[i-1][z - zeros][o - ones]
                        dp[i][z][o] = max(dp[i][z][o], take_it)
        return dp[size][m][n]