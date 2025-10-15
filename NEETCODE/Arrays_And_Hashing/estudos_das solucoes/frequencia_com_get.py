def topFrequent(nums):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        return count


print(topFrequent([1,2,2,3,3,3,3]))