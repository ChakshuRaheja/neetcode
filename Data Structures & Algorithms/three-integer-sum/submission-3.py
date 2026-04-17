class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []                 # stores final triplets
        nums.sort()              # sort array for two-pointer logic

        # pick one number at a time as first element
        for i, a in enumerate(nums):

            # if first number > 0, no triplet can make 0
            # because all numbers after this are also >= a
            if a > 0:
                break

            # skip duplicate starting numbers
            # avoids duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # two pointers
            l = i + 1            # left pointer
            r = len(nums) - 1    # right pointer

            while l < r:
                total = a + nums[l] + nums[r]

                if total > 0:
                    # sum too big -> move right left
                    r -= 1

                elif total < 0:
                    # sum too small -> move left right
                    l += 1

                else:
                    # valid triplet found
                    res.append([a, nums[l], nums[r]])

                    # move both pointers
                    l += 1
                    r -= 1

                    # skip duplicate values on left
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l<r and nums[r] == nums [r+1]:
                        r = r-1
        return res
        