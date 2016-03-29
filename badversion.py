#************************************************
# File Name: badversion.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-03-25 16:29:38
# Last modified: 2016-03-25 16:29:38
#!/usr/bin/env python
# -*- coding: utf-8 -*-

l,r = 1,n
while 1:
    m = (l+r)/2
    if m==l:
        return r
    if isbad(m):
        r = m
    else:
        l = m
