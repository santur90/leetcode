#************************************************
# File Name: valid_parenthess.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-03-25 14:42:17
# Last modified: 2016-03-25 14:50:25
#!/usr/bin/env python
# -*- coding: utf-8 -*-

dic = {'l':['(','{','['],'r':[')','}',']']}
inp = []
s = '()[]]'

for i in s:
    print i
    if i in dic['l']:
        inp.append(i)
        print inp
    elif i in dic['r']:
        if inp == []:
            print False
        else:
            x = inp.pop()
        print x
        print dic['l'].index(x),dic['r'].index(i)
        if dic['l'].index(x) != dic['r'].index(i):
            print False
print True
