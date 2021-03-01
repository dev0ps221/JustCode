from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
from Variables import *
variables = {}
functions = {}
stack = []


def shell (JCI):

    def salut():
        print("salut")

    def start():
        while(True):
            lexer = Lexer(input("JC>"))
            tokens,errs = lexer.Tokenize()
            if len(errs.show()) != 0:
                print(errs.getLast())
            else:
                # pass
                
                Set = []
                for token in tokens:
                    if token.type == "ENDTOKEN":
                        stack.append(Set)
                        Set = []
                    elif token.type == "VarOp":
                        if token.operation == "setVal":
                            if token.value.type == 'NAME':


                        Set.append(token)
                    else:
                        Set.append(token)
                # parser = Parser(tokens)
                # print(tokens)
                # ast = parser.Parse()
                # print(ast)
                # Num = (JCI.visit(ast))
                # print(Num.value)
                # (JCI.visit(ast))
    return {
        "start":start
    } 