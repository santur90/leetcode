#************************************************
# File Name: word_search2.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-03-11 09:35:46
# Last modified: 2016-03-11 10:38:34
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dfs(x,y,board,word):
    print x, y, word
    if len(word) == 0:
        return True
    else:
        print board[x-1][y],board[x][y-1],board[x+1][y],board[x][y+1]
        if x>0 and board[x-1][y] == word[0]:
            tmp = board[x][y]
            board[x][y] = "#"
            if dfs(x-1,y,board,word[1:]):
                return True
            board[x][y] = tmp
        if y>0 and board[x][y-1] == word[0]:
            tmp = board[x][y]
            board[x][y] = "#"
            if dfs(x,y-1,board,word[1:]):
                return True
            board[x][y] = tmp
        if x<=len(board)-2 and board[x+1][y] == word[0]:
            tmp = board[x][y]
            board[x][y] = "#"
            if dfs(x+1,y,board,word[1:]):
                return True
            board[x][y] = tmp
        if y<=len(board[0])-2 and board[x][y+1] == word[0]:
            tmp = board[x][y]
            board[x][y] = "#"
            if dfs(x,y+1,board,word[1:]):
                return True
            board[x][y] = tmp
        #return False
board = ["oaan","etae","ihkr","iflv"]
words = ["oath","pea","eat","rain"]
re = []
for word in words:
    ok = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(i,j,board,word[1:]):
                    re += [word]
                    ok = True
                    break
        if ok:
            break
print re
