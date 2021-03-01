#!/usr/bin/env python3
from Required import *
from sys import argv
        
JCI = Interpreter()
if len(argv) > 1:
    with open (argv[1],'r') as f:
        lexer = Lexer(f.read())
        tokens,errs = lexer.Tokenize()
        if len(errs.show()) != 0:
            print(errs.getLast())
        else:
            # pass
            parser = Parser(tokens)
            # print(tokens)
            ast = parser.Parse()
            # print(ast)
            Num = (JCI.visit(ast))
            print(Num.value)
            # (JCI.visit(ast))
else:
    Shell = shell(JCI)
    Shell['start']()