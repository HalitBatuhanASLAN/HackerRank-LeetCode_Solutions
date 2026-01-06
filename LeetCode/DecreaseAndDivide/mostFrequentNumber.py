def mostFrequentNumber(nums:List[int],starting,end) -> int:
    if starting == end:
            return List[starting]
    middle = (starting + end)/2
    left_one = mostFrequentNumber(nums,starting,middle)
    right_one = mostFrequentNumber(nums,middle + 1,end)
    if left_one == right_one:
        return left_one
    left_count = sum(1 for i in range(starting, end + 1) if nums[i] == left_one)
    right_count = sum(1 for i in range(starting, end + 1) if nums[i] == right_one)

    return left_one if left_count > right_count else right_one