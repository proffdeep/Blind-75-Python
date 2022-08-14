class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            cursum += nums[i]
            max_sum = max(cursum,max_sum)

            if cursum < 0:
                cursum = 0

        return max_sum