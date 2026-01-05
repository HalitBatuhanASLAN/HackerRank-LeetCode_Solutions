'''
https://leetcode.com/problems/01-matrix?envType=problem-list-v2&envId=dynamic-programming
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
        for i in range(m):
            for j in range(n):
                if(mat[i][j] != 0):
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if dp[i][j] != 0:
                    if i < m - 1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                    if j < n - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
        return dp