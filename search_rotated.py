#************************************************
# File Name: search_rotated.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-03-25 17:19:43
# Last modified: 2016-03-27 13:05:37
#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = [1,1,3,1]
target = 3
l, r = 0, len(x)-1
while 1:
    m = (l+r)/2
    print l,r,m
    if m == l and x[m]!=target and x[r]!=target:
        break
    if x[m] == target or x[r]==target:
        print m if x[m] == target else r
        break
    if target > x[r]:
        if target > x[m] and x[m] > x[l]:
            l = m
        else:
            r = m
    else:
        if target < x[m] and x[m] < x[r]:
            r = m
        else:
            l = m
