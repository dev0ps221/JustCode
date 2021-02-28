#!/usr/bin/env python3

class Pos():
    current = None

    def set_pos(self,start=None,end=None):
        self.start = start
        self.end = end



class Number():

    def __init__(self,value):
        self.value = value
        self.pos = Pos()
        self.pos.set_pos()
        self.pos.current = self.pos.start

    def plus(self,other):
        if isinstance(other,Number):
            return Number(self.value + other.value)

    def moins(self,other):
        if isinstance(other,Number):
            return Number(self.value - other.value)

    def fois(self,other):
        if isinstance(other,Number):
            return Number(self.value * other.value)

    def divi(self,other):
        if isinstance(other,Number):
            return Number(self.value / other.value)

    def modu(self,other):
        if isinstance(other,Number):
            return Number(self.value % other.value)

    def repr__(self):
        return f'{str(self.value)}'

class Interpreter():

    def visit(self,node):
        type_ = f'{type(node).__name__}'
        if type_ == "Token":
            type_ = type_
        elif type_ == 'str' :
            type_ = node
        type_ = "Check" + type_
        method = getattr(self,type_,self.defaultVisitMethod)
        return method(node)

    def CheckBinOp(self,node):
        result = node
        l = self.visit(node.left)
        r = self.visit(node.right)

        if node.operator.value == '+':
            result = l.plus(r)
        if node.operator.value == '-':
            result = l.moins(r)
        if node.operator.value == '*':
            result = l.fois(r)
        if node.operator.value == '/':
            result = l.divi(r)
        if node.operator.value == '%':
            result = l.modu(r)
        return result
        
    def CheckUnOp(self,node):
        o = node.operator
        n = self.visit(node.node)
        result = n
        if o.value == '+':
            result = n
        if o.value == '-':
            result = n.fois(-1)

        return result
        
    def CheckNAME(self,node):
        return (node)

    def CheckNumberNode(self,node):
        return Number(node.value)

    def CheckCHR(self,node):
        return (node)

    def CheckToken(self,node):
        ret = node
        if (node.type) == "TEXT_KW":
            ret = self.ProcessKeyWord(node)
        else :
            ret = self.visit(node.type)        
        return ret

    def ProcessKeyWord(self,node):
        return (node)

    def defaultVisitMethod(self,node):
        (node)

