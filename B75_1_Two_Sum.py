class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            to_find = target - nums[i]

            if to_find in hash_table:
                return print([hash_table[to_find],i])
            hash_table[nums[i]] = i 


sol = Solution()
sol.twoSum([3,2,4],6)