'''
https://leetcode.com/problems/distribute-money-to-maximum-children?envType=problem-list-v2&envId=greedy
'''

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money == children * 8:
            return children
        dp = [1] * (children)
        money = money - children
        count = 0
        i = 0
        for i in range(children):
            if money <= 0:
                break
            if dp[i] != 8:
                if money < 8 - dp[i]:
                    break
                money = money - 7
                dp[i] = 8
                count += 1
        if i == children-1:
            if money > 0 and dp[i] == 8:
                count -= 1
            elif money == 3:
                count -= 1
        return count