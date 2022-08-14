class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = set()
        for i in range(len(nums)):
            if nums[i] in t:
                return True
            t.add(nums[i])
        return False
