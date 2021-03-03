#!/usr/bin/env python3

class  BinOp():

    def __init__(self,l,o,r):
        self.left= l
        self.operator = o
        self.right = r
        self.type = BinOp    
    def __repr__(self,p=0):
        if p : return f'{self.type}'
        return f"( {self.left}|{self.operator.type}|{self.right} )"



class  UnOp():

    def __init__(self,o,n):
        self.operator = o
        self.node = n
        self.type = UnOp
    
    def __repr__(self,p=0):
        if p : return f'{self.type}'
        return f"( {self.operator.type}|{self.node} )"



class  NnOp():

    def __init__(self,n,v,t,o="getVal",p=None):
        self.name = n
        self.value = v
        self.type = t
        self.operation = o
        self.pos = p
    
    def __repr__(self):
        return f"( {self.operation} on {self.name} )"

class VarOp(NnOp):
    def __init__(self,n,v,t,o,p):
        super().__init__(n,v,t,o,p)
        
class ConstOp(NnOp):
    def __init__(self,n,v,t,o,p):
        super().__init__(n,v,t,o,p)
        
