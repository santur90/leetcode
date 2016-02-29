# -*- coding: utf-8 -*-
#************************************************
# File Name: contain_duplicate.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-02-29 19:55:59
# Last modified: 2016-02-29 19:55:59
#!/usr/bin/env python

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
