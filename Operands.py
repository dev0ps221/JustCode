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



class  NnOp():

    def __init__(self,n,v,t,o="getVal"):
        self.name = n
        self.value = v
        self.type = t
        self.operation = o
    
    def __repr__(self):
        return f"( {self.operation} on {self.name} )"

class VarOp(NnOp):
    def __init__(self,n,v,t,o):
        super().__init__(n,v,t,o)
        
class ConstOp(NnOp):
    def __init__(self,n,v,t,o):
        super().__init__(n,v,t,o)
        
