#estudar depois (muito complexo)


def threeSum(nums):
        n = len(nums)
        res = []
        if n < 3:
            return res

        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res


print(threeSum([-1,0,1,2,-1,-4]))