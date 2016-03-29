#************************************************
# File Name: water.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-03-27 15:30:20
# Last modified: 2016-03-27 15:30:20
#!/usr/bin/env python
# -*- coding: utf-8 -*-

height = [0,1,0,2,1,0,1,3,2,1,2,1]
water = 0
l = h = 0
dic = {}
for i in height:
    if water == 0:
        if height[l] != 0:
            l = i
            dic[l] = 0
            h = height[l]
            water = 1
    if height[i] < h:
        water += h-height[i]
    else:
        dic[l] = 1
        l = i
        dic[l] = 0
        h = height[l]
