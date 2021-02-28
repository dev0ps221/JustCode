#!/usr/bin/env python3
from Classes import *

class Lexer():

    def __init__(self,text,tfiles="TT",kwfiles="TKW"):
        self.text = text
        self.Types = TexTypes()
        self.KeyWords = KeyWords()
        self.Tokenizer = Tokenizer(self.Types,self.KeyWords)
        with open(tfiles,'r')  as f:
            for line in [str(l) for l in f.readlines()]:
                self.Types.Append((line.split(" ")[0],line.split(" ")[1]))
        with open(kwfiles,'r')  as f:
            for line in [str(l) for l in f.readlines()]:
                if "SIGN" in line.split(" ")[0]:
                    self.KeyWords.Signs.Append(("",line.split(" ")[1].replace('\n','')))
                else:
                    self.KeyWords.Append((line.split(" ")[0],line.split(" ")[1]))
    def Tokenize(self):
        self.tokens = self.Tokenizer.Tokenize(self.text)
        return self.tokens

    def __repr__(self):
        return f"{self.text}"

