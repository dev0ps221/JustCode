#!/usr/bin/env python3
from Required import *

JCI = Interpreter()
while(True):
    lexer = Lexer(input("JC>"))
    tokens = lexer.Tokenize()
    parser = Parser(tokens)
    print(tokens)
    # ast = parser.Parse()
    # print(ast)
    # print(JCI.visit(ast))
    # (JCI.visit(ast))