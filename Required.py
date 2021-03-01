from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter
from Variables import *
variables = {}
functions = {}
stack = []


def shell (JCI):
    def start():
        while(True):
            lexer = Lexer(input("JC>"))
            tokens,errs = lexer.Tokenize()
            if len(errs.show()) != 0:
                print(errs.getLast())
            else:
                Set = []
                for token in tokens:
                    if token.type == "ENDTOKEN":
                        stack.append(Set)
                        Set = []
                    elif token.type == "VarOp":
                        Set.append(token)
                        if token.operation == "setVal":
                            variable = Variable()
                            if type(token.value) == str:
                                val = token.value
                                type_ = token.value
                            else :
                                type_ = token.value.type
                                val = token.value.value
                                Set.pop()
                            variable.setAttr("type",type_)
                            variable.setAttr("name",token.name)
                            variable.setAttr("value",val)
                            variables[token.name] = variable
                    else:
                        Set.append(token)
                print("variables =>",variables)
                for Set in stack:
                    print("stack elem =>",Set)
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

