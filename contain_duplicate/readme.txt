class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == None: return False
        else:
            dic = {i:1 for i in nums}
            return len(dic) != len(nums)
