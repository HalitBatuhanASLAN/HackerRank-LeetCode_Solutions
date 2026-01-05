'''
https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array?envType=problem-list-v2&envId=aphrw7b3
'''

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(x) for x in nums]
        target_index = len(nums) - k
        
        return str(self.quickSelect(nums, 0, len(nums) - 1, target_index))
    def quickSelect(self, nums: List[int], low: int, high: int, k: int) -> int:
        if low == high:
            return nums[low]
        s = self.lomutoPartition(nums,low,high)
        if s == k:
            return nums[s]
        elif s > k:
            return self.quickSelect(nums,low,s-1,k)
        else:
            return self.quickSelect(nums,s+1,high,k)
    def lomutoPartition(self,nums:List[str],low:int,high:int) -> int:
        rand_idx = random.randint(low, high)
        nums[rand_idx], nums[high] = nums[high], nums[rand_idx]
        
        pivot = nums[high]
        i = low - 1
        for j in range(low,high):
            if nums[j] <= pivot:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i+1],nums[high] = nums[high],nums[i+1]
        return i + 1