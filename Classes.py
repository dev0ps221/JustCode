#!/usr/bin/env python3
import string
from Error import *
from Operands import VarOp

##################################

  # $$$$$$        $%%%% ##  #    #
####TYPES

class TexType():
    def __init__(self,type_,value):
        self.type = type_
        self.value = value

    def getType(self):
        return self.type

    def __repr__(self):
        return f"{self.value}"


class KeyWord(TexType):
    def __init__(self,type_,value):
        super().__init__(type,value)
        type_="TEXT_KW"
        self.type = type_
        self.value = value


class TexTypes():

    def __init__(self):
        self.buffer = []
        self.pos = -1
        self.actual = None

    def Next(self):
        self.pos += 1
        self.actual = self.buffer[self.pos] if self.pos < len(self.buffer) else None
        return self.actual

    def Append(self,typeInfs):
        type_,value = typeInfs
        self.buffer.append(TexType(type_,value))

    def getBuffer(self):
        return self.buffer

    def __getitem__(self,x):
        return self.buffer[x]


    def __getattr__(self,y):
        ret = False
        for x in self.buffer:
            if x.value[1] == y:
                ret = x 
        if ret:
            return ret

    def __repr__(self):
        return f"{[t.type for t in self.getBuffer()]}"

    def Retrieve(self,type_):
        ret = None
        for t in self.getBuffer(): 
            if t.type.split("\n")[0] == type_ or (hasattr(t.value,'split') and t.value.split("\n")[0] == type_):
                ret = t
                break
        return ret

class KWSign(TexType):
    def __init__(self,type_,value):
        super().__init__(type_,value)
        self.type = "KWSIGN"

class KWSigns(TexTypes):
    def __init__(self):
        super().__init__()
    
    def Append(self,value):
        type_,value = ("KWSIGN",value)
        self.buffer.append(KWSign(type_,value))


class KeyWords(TexTypes):

    def __init__(self):
        super().__init__()
        self.Signs = KWSigns()

    def Append(self,typeInfs):
        type_,value = typeInfs
        self.buffer.append(KeyWord(type_,value))


##################################

  # $$$$$$        $%%%% ##  #    #
####TRACKING
class Position():

    def __init__(self,text,idx=-1,line=0,col=-1,file='<stdin>'):
        self.idx = idx
        self.line = line
        self.col = col
        self.file = file
        self.text = text
        self.current = None
        self.Next()
    def Next(self):
        self.idx += 1
        self.col += 1
        self.current = self.text[self.idx] if self.idx < len(self.text) else None
        if self.current == '\n':
            self.line+=1
            self.col=0
        return self.current

    def __repr__(self):
        return f'''|>Line {self.line}-|-Column {self.col}<|'''

class Pos():
    def __init__(self,start=None,end=None,line='None',file="<stdin>"):
        self.file = file
        self.line = line
        self.set_pos(start,end,line,file)

    def set_pos(self,start=None,end=None,line='null',file='null'):
        self.start = start
        self.end = end
        self.line = self.line if line =='null' and self.line == None else line
        self.file = self.file if file =='null' and self.file == None else file


    def __repr__(self):
        return f'''|>Line {self.line}-|-Column {self.start}-{self.end}<|'''


##################################

  # $$$$$$        $%%%% ##  #    #
####TOKENS
class Token():


    def __init__(self,type_,value,start=None,end=None,line=None,file='<stdin>'):
        if end == None : end = start
        self.type = type_
        self.value = value
        self.pos = Pos(start,end,line,file)
    def __repr__(self):
        return f"{self.type}:{self.value}"


class Tokenizer():

    def getRefNameAndType(self,name):
        value = ""
        type_ = ""
        for ref in self.refTypes:
            if name in ref[0] or name in ref[1]:
                value = ref[0]
                type_ = ref[1]
        
        return value,type_ if value != "" else None

    def __init__(self,Types,KeyWords):
        self.Types = Types
        self.KeyWords = KeyWords
        self.refTypes = ['INT','01234564789'],['NAME',string.ascii_letters]
        self.tokens = []
        self.errs = ErrorResponse()
        
    def ConfirmTokens(self):
        tokens = []
        stop = 0
        n = 0
        pos = 0
        group = []
        start = -1
        counter = 0
        aKeyword = 0
        fillType = ""
        for token in self.tokens:
            tok = token
            for Kw in self.KeyWords:
                if Kw.value.split('\n')[0] == token.value:
                    aKeyword = 1     
                    if token.value == "=V":
                        start = pos
                        fillType = "var"
                        pos+=1
                        break

                    if token.value == "=F":
                        start = pos
                        fillType = "func"
                        name = ""
                        mot=""
                        arguments = []
                        StackBuff = []
                        foundName = 0
                        pos+=1
                        break
                
            if start != -1:
                if fillType == "var":
                    if counter <= 1 :
                        if token.type == "NAME":
                            group.append(self.tokens[start+counter+1])
                            counter+=1
                            if counter > 1 :
                                name,value = group
                                tok.pos.start = start
                                tok = VarOp(name,value,"VarOp","setVal",token.pos)
                                counter = 0
                                start = -1
                                pos+=1
                        else:
                            counter+1
                            if counter == 1:
                                name,value = group[0],"NEXTOP"
                                tok = VarOp(name,value,"VarOp","setVal",group[0].pos)
                                tokens.append(tok)
                                tok = token
                                counter = 0
                                start = -1
                    else:
                        start = 0
                        counter = 0
                        if token.type == "NAME":
                            self.errs.register("JCSyntaxError",token.pos,token,"Unexpected Token")
                        else:
                            tok = token
                            tokens.append(tok)

                if fillType == "func":
                    n+=1
                    while n < len(self.tokens) and self.tokens[n] != None and self.tokens[n].value not in "".join([Kw.value.split('\n')[0] for Kw in self.KeyWords]):
                        if not foundName:
                            name = self.tokens[n]
                            foundName = 1
                            n+=1
                            stop = 1
                        else:
                        
                            if n < len(self.tokens) and self.tokens[n] != None:
                                while n < len(self.tokens) and self.tokens[n] != None and self.tokens[n].value not in ".=START":
                                    arg = self.tokens[n]
                                    arguments.append(arg)
                                    n+=1
                                    counter+1
                            
                    if n < len(self.tokens) and self.tokens[n] != None:
                        if self.tokens[n].value in ".=START":
                            while n < len(self.tokens) and self.tokens[n] != None and self.tokens[n].value not in "=.END":  
                                if self.tokens[n] in "; \n\t":
                                    mot = StackBuff.append(self.tokens[n]) 
                                    print(mot)
                                    n+1
                                mot+= self.tokenss[n]
                                n+=1
                                counter+1
                                stop = 1
                            # print(StackBuff)
                            # if n < len(self.tokens) and self.tokens[n] != None:
                            #     print(self.tokens[n])
                            # else:
                            #     print('diap amna deh')


            if stop :
                stop = 0
                continue

            pos+=1
            if not aKeyword:
                if start == -1 : tokens.append(tok)
            else:
                aKeyword = 0
            n+=1

        self.tokens = tokens
        return (self.tokens,self.errs)

    def Tokenize(self,text):    
        self.errs.flush()
        self.pos = Position(text)
        
        while self.pos.current != None:
            value = self.pos.current    
            if value in ' \t':
                self.pos.Next()
            elif value in ';\n' :
                self.tokens.append(Token('ENDTOKEN',"STOP",self.pos.idx,None,self.pos.line,self.pos.file))
                self.pos.Next()
            elif self.Types.Retrieve(self.pos.current) != None:
                crrnt = self.Types.Retrieve(self.pos.current)
                if crrnt.type == "TEXT_DBQUOTE":
                    tok = self.pos.current
                    start = self.pos.idx
                    type_,name,value = self.Stringify("STRING",value,value)
                    if self.pos.current == None:
                        errTok = Token(type_,value,start,self.pos.idx,self.pos.line,self.pos.file)
                        self.errs.register("JCSyntaxError",errTok.pos,errTok,"expecting '\"' after expression at")
                    else:
                        value += self.pos.current
                        end = self.pos.idx
                        self.tokens.append(Token(type_,value,start,end,self.pos.line,self.pos.file))
                        self.pos.Next()
                else:
                    self.tokens.append(Token(crrnt.type,self.pos.current,self.pos.idx,None,self.pos.line,self.pos.file))
                    self.pos.Next()
            elif self.KeyWords.Signs.__getattr__(self.pos.current) != None:
                KW = self.KeyWords.Signs.__getattr__(self.pos.current) 
                type_ = KW.type
                self.pos.Next()

                last = self.pos.current
                stop = 0
                start = self.pos.idx
                while self.pos.current!=None:
                    if stop : break
                    if self.pos.current not in " \n\t":
                        value +=self.pos.current
                        self.pos.Next()
                    else :
                        stop = 1
                
                end = self.pos.idx
                if self.KeyWords.Retrieve(value) != None:
                    type_ = self.KeyWords.Retrieve(value).type
                    self.tokens.append(Token(type_,value))
                    self.pos.Next()
                else:
                    if value not in " ;\n\t":
                        errTok = Token(type_,value,start,end,self.pos.line,self.pos.file)
                    else:
                        errTok = Token('ENDTOKEN',"STOP",self.pos.idx,None,self.pos.line,self.pos.file)
                    self.errs.register("JCKeyWordError",errTok.pos,errTok,"Undefined KEYWORD")
            else:
                hasRef = self.getRefNameAndType(self.pos.current)
                if hasRef != None:
                    type_,name = hasRef
                    if type_ == "INT":
                        type_,name,value = self.Numerize(type_,name,value)
                        self.tokens.append(Token(type_,value,self.pos.idx,None,self.pos.line,self.pos.file))
                    elif type_ == "NAME":
                        type_,name,value = self.Namify(type_,name,value)
                        self.tokens.append(Token(type_,value,self.pos.idx,None,self.pos.line,self.pos.file))
                    else:
                        self.tokens.append(Token(type_,value,self.pos.idx,None,self.pos.line,self.pos.file))
                        self.pos.Next()
                    hasRef = 0
                else:
                    self.tokens.append(value)
                    self.pos.Next()
        
        self.tokens.append(Token('ENDTOKEN',"STOP",self.pos.idx,None,self.pos.line,self.pos.file))
        return self.ConfirmTokens()
    
    def Numerize(self,type_,name,value):
        self.pos.Next()
        stop = 0
        while self.pos.current != None:
            if stop : break
            checkingDBL = 0
            if self.pos.current in ".":
                checkingDBL = 1
                value+=self.pos.current
                self.pos.Next()

            if checkingDBL :
                if self.pos.current in self.refTypes[0][1]:
                    type_ = "DEC"
                    checkingDBL = 0
            if self.pos.current in self.refTypes[0][1]:
                value+=self.pos.current
                self.pos.Next()
            else:
                stop = 1
                break
        return(type_,name,value)

    def Charify(self,type_,name,value):
        stop = 0
        self.pos.Next()
        while self.pos.current != None:
            type_ = "STR"
            if stop : break
            if self.pos.current in self.refTypes[1][0]:
                value+=self.pos.current
            else:
                stop = 1
                break
            self.pos.Next()
        return(type_,name,value)

    def Namify(self,type_,name,value):
        self.pos.Next()
        stop = 0
        while self.pos.current != None and self.pos.current not in "\n\t ;\"":
            if stop : break
            # if self.pos.curren  in self.refTypes[1][1]:
            value+=self.pos.current
            self.pos.Next()
            # else:
            #     stop = 1
            #     break
        return(type_,name,value)

    def Stringify(self,type_,name,value):
        self.pos.Next()
        stop = 0
        while self.pos.current != None and self.pos.current != '"':
            
            value+=self.pos.current
            self.pos.Next()
            
        return(type_,name,value)

##################################

  # $$$$$$        $%%%% ##  #    #
####    NODES

class NumberNode(TexType):
    def __init__(self,type_,value):
        super().__init__(type_,value)
        self.type = "NUMBERNODE"
        self.valtype = type_