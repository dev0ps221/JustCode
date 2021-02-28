#!/usr/bin/env python3

class  BinOp():

    def __init__(self,l,o,r):
        self.left= l
        self.operator = o
        self.right = r
    
    def __repr__(self):
        return f"( {self.left}|{self.operator.type}|{self.right} )"



class  UnOp():

    def __init__(self,o,n):
        self.operator = o
        self.node = n
    
    def __repr__(self):
        return f"( {self.operator.type}|{self.node} )"