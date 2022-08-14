class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    	curMax = 1
    	curMin = 1
    	res = max(nums)
    	for n in nums:
    		tmp = curMax * n
    		curMax = max(n * curMax, n * curMin, n)
    		curMin = min(tmp, n * curMin, n)
    		res = Max(res,curMax)
    	return res

