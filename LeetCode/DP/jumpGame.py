'''
https://leetcode.com/problems/jump-game?envType=problem-list-v2&envId=dynamic-programming
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if(n == 1):
            return True
        if(nums[0] == 0):
            return False
        for i in range(0,n):
            if(nums[i] == 0):
                flag = False
                for j in range(i - 1, -1, -1):
                    if i == n - 1:
                        if nums[j] >= i - j:
                            flag = True
                            break
                    if(nums[j] > i - j):
                        flag = True
                        break
                if(flag != True):
                    return False
        return True