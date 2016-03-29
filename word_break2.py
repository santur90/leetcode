#************************************************
# File Name: word_break2.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-03-11 12:33:31
# Last modified: 2016-03-11 14:14:25
#!/usr/bin/env python
# -*- coding: utf-8 -*-
def dfs(s,dict,re):
    print "now in ",s," we'll find ",dict,"we've found ",re
    if len(s) == 0:
        return True
    else:
        for i in range(1,len(s)+1):
            if s[:i] in dict:
                if dfs(s[i:],dict,re):
                    re += s[:i]

s = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]
re = []
x = 0
for i in range(1,len(s)+1):
    print "i is ",i
    if s[:i] in dict:
        print s[:i],"is in dict"
        re.append(s[:i])
        x += 1
        if i < len(s)-1 and dfs(s[i:],dict,re[x]):
            print re
            continue
print []

