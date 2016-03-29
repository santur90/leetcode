#************************************************
# File Name: implement_str.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-03-25 15:00:54
# Last modified: 2016-03-25 15:07:10
#!/usr/bin/env python
# -*- coding: utf-8 -*-

hay, need = 'seed','ed'
l1 = len(hay)
l2 = len(need)

for i in range(0,l1-l2+1):
    if hay[i] == need[0]:
        if hay[i+l2-1] == need[l2-1]:
            if hay[i:i+l2] == need:
                print i
