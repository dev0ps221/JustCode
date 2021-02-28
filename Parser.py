from Classes import Position,NumberNode
from Operands import *

class Parser():

    def __init__(self,tokens):
        self.tokens = tokens
        self.pos = Position(tokens)
        
    def GetTokens(self):
        return self.tokens

    def Parse(self):
        return self.Expression()


    def Factor(self):
        tok = self.unOpFunction()
        ret = tok
        elem = tok.type if hasattr(tok,'type') else tok
        if elem in ['INT',"DEC"]:
            ret =  NumberNode(elem,int (tok.value) if elem == "INT" else float (tok.value))
        self.pos.Next()
        return ret

    def Parse(self):
        return self.Expression()

    def Term(self):

        l = self.Factor()

        #we get the three for prior binOp Operations
        l = self.binOpFunction(self.Factor,['/','*'],l)
        return l



    def Expression(self):
        a = self.Factor()

        #we get the three for prior binOp Operations
        a = self.binOpFunction(self.Factor,['/','*'],a)

        #we get the three for simple binOp Operations
        a = self.binOpFunction(self.Term,['+','-'],a)

        return a

    def binOpFunction(self,func,opts,a = 'null'):
        if a == 'null' : a = self.Factor()
        while self.pos.current != None and self.pos.current.value in opts:
            operator = self.pos.current
            self.pos.Next()
            if self.pos.current == None:
                break
            a = BinOp(a,operator,func())
        return a
        
    def unOpFunction(self):
        val = self.pos.current
        if val.value in '-+':
            self.pos.Next()
            if self.pos.current != None:
                if self.pos.current.type in ['INT','DEC']:
                    val = UnOp(val,NumberNode(self.pos.current.type,self.pos.current.value))
        return val