#************************************************
# File Name: sudoku.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-03-25 15:20:22
# Last modified: 2016-03-25 16:08:02
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#board = [[1]*9,[2]*9,[3]*9,[4]*9,[5]*9,[6]*9,[7]*9,[8]*9,[9]*9]
import string
board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
def valid(x):
    print x
    x = [i for i in x if i.isdigit()]
    print x,set(x)
    return True if x==[] or len(set(x)) == len(x) else False
for i in range(0,9):
    print valid([board[i][j] for j in range(0,9)])
    print valid([board[j][i] for j in range(0,9)])
for i in range(0,3):
    for j in range(0,3):
        print valid([board[x][y] for y in range(3*j,3*j+3)for x in range(3*i,3*i+3)])
