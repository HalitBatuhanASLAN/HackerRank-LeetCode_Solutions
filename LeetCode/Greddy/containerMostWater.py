'''
https://leetcode.com/problems/container-with-most-water?envType=problem-list-v2&envId=greedy
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        i = 0
        j = len(height) -1
        while i < j:
            current_water = min(height[i],height[j]) * (j - i)
            if  height[i] < height[j]:
                i += 1
            else:
                j -= 1
            max_water = max(max_water,current_water)
        return max_water