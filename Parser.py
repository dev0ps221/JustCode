from Classes import Position,NumberNode
from Operands import *

class Parser():
    ###CLASS PARSER###

    def __init__(self,tokens):
        # on stocke le set de tokens fournis a l instanciation du parseur (cela permettras d'avoir plusieurs operations de parsing en meme temps)
        self.tokens = tokens
        self.pos = Position(tokens)
        
    def GetTokens(self):
        return self.tokens

    # def Parse(self):
    #     return (self.Expression(),self.pos)


    def Factor(self):
        tok = self.unOpFunction()
        ret = tok
        elem = tok.type if hasattr(tok,'type') else tok
        if elem in ['INT',"DEC"]:
            ret =  NumberNode(elem,int (tok.value) if elem == "INT" else float (tok.value))
        elif elem == 'VarOp':
            if tok.operation == "setVal":
                if (tok.value) == "NEXTOP":
                    ret = self.pos.current
                    self.pos.Next()
                    # print(self.tokens)
                    # print (self.tokens[self.pos.idx:])
                    parser = Parser(self.tokens[self.pos.idx:])
                    val,pos = parser.Parse()
                    
                    ret.value = val
                    self.pos.idx = pos.idx+self.pos.idx
                    self.pos.col = pos.col
                    self.pos.line = pos.line
                    
        self.pos.Next()
        return ret

    def Parse(self):
        if len(self.tokens) > 1:
            start = self.tokens[0].pos.start
            end = self.tokens[-1].pos.end + 1
            # print(start,end)
            return self.Expression(),self.pos
        else:
            return self.Factor(),self.pos
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
        # if a.type != "NUMBERNODE":
        while self.pos.current != None and self.pos.current.value in opts:
            operator = self.pos.current
            self.pos.Next()
            if self.pos.current == None:
                break
            a = BinOp(a,operator,func())
        # else:
        #     print(a.type)
        return a
        
    def unOpFunction(self):
        val = self.pos.current
        if type(val.value) != NumberNode:
            if val.value in '-+':
                self.pos.Next()
                if self.pos.current != None:
                    if self.pos.current.type in ['INT','DEC']:
                        val = UnOp(val,NumberNode(self.pos.current.type,self.pos.current.value))
        return val