# -*- coding: utf-8 -*-
#************************************************
# File Name: qin1.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-02-29 16:44:54
# Last modified: 2016-02-29 16:44:54
#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            array = []
        else:
            array = [root[0][0]]
            for x in range(0,log2(len(root) + 1)-1):
                array.insert(0,self.add(array,x))
            array = [x for x in array if x.isdigit()]
        return array
    
    def add(root, x):
        return root[2**(x)+1:2**(x+1)+1]
