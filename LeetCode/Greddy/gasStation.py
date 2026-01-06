'''
https://leetcode.com/problems/gas-station?envType=problem-list-v2&envId=greedy
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        current_gas = 0
        start_index = 0
        for i in range(n):
            current_gas += gas[i] - cost[i]
            flag = True
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0
                flag = False
        if flag == True:
            return start_index
        return -1