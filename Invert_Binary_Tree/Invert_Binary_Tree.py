# -*- coding: utf-8 -*-
#************************************************
# File Name: Invert_Binary_Tree.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-02-29 11:40:10
# Last modified: 2016-02-29 11:40:10
#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None:
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root
