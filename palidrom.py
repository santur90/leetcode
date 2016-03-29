# -*- coding: utf-8 -*-
# File Name: palidrom.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-03-12 13:29:35
# Last modified: 2016-03-12 15:38:42
#!/usr/bin/env python
#****************************************

s = "aabacdc"
def isp(s):
    i,j=0,len(s)-1
    while j>i:
        if s[i] != s[j]:
            return False
        else: 
            i+=1
            j-=1
    return True
def dfs(depth, s, dic, tmp, re):
    print "now in depth",depth,"string is",s,"dic is",dic,"tmp is",tmp,"re is",re
    if len(s) == 0:
        print "now len(s)==0,re from",re
        re.append(tmp)
        print "changed to ",re
        return True
    else:
        if s in dic:
            #print "string",s,"is in dic",dic,"so re from",re
            re.append(tmp+[dic[s]])
            #print "changed to ",re
            return True
        else:
            #have = False
            ss = s
            print "ss is before",ss
            if ss not in dic:
                dic[ss] = []
            for i in range(1,len(s)+1):
                tre = []
                if isp(s[:i]):
                    #print "before s is",s,"tmp is",tmp,"re is",re
                    print s[:i],"is a palidrom"
                    #have = True
                    if dfs(depth + 1,s[i:],dic,tmp+[s[:i]],re) and len(s)>1:
                        print "s is now",s,"re is now",re
                        tre = re[-1][len(re[-1])-len(s):]
                if tre:
                    dic[ss].append(tre)
                    print "dic is",dic
            return True
            #if not have:
                #print "can't find substring for",s
                #return False
dic,re={},[]
print "T" if dfs(0,s,dic,[],re) else "F"
print dic
