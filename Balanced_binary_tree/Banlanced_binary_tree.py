# -*- coding: utf-8 -*-
#************************************************
# File Name: Banlanced_binary_tree.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-02-29 14:18:52
# Last modified: 2016-02-29 14:18:52
#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        depl = depr = 0
        if root == None or (root != None and root.left == None and root.right == None):
            return True
        if root.left != None:
            depl = 1 + self.isBalanced(root.left)
        if root.right != None:
            depr = 1 + self.isBalanced(root.right)
        if depl - depr > 2 or depl - depr < -2:
            return False
        dep = max(depl, depr)
        return dep
