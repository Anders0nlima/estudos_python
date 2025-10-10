def hasDuplicate(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False

print(hasDuplicate([1, 2, 3, 3]))

   