#!/usr/bin/env python3
from Required import *

JCI = Interpreter()
while(True):
    lexer = Lexer(input("JC>"))
    tokens,errs = lexer.Tokenize()
    if len(errs.show()) > 1:
        print(errs.show()[0]) 
    # parser = Parser(tokens)
    # print(tokens)
    # ast = parser.Parse()
    # print(ast)
    # print(JCI.visit(ast))
    # (JCI.visit(ast))