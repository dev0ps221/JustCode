from Operands import *
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
            print(f'variables {variables}')
            lexer = Lexer(input("JC>"))
            tokens,errs = lexer.Tokenize()
            if len(errs.show()) != 0:
                print(errs.getLast(),flush=1)
            else:
                Set = []
                for token in tokens:
                    if token.type == "ENDTOKEN":
                        stack.append(Set)
                        Set = []                                        
                    # elif token.type == "VarOp":
                    #     Set.append(token)
                    #     if token.operation == "setVal":
                    #         variable = Variable()
                    #         if type(token.value) == str:
                    #             val = token.value
                    #             type_ = token.value
                    #         else :
                    #             type_ = token.value.type
                    #             val = token.value.value
                    #             Set.pop()
                    #         variable.setAttr("type",type_)
                    #         variable.setAttr("name",token.name)
                    #         variable.setAttr("value",val)
                    #         variables[token.name.value] = variable
                    else:
                        Set.append(token)
                for Set in stack:
                    print("processing stack elem =>",Set)
                    action = None
                    concerned = None
                    n = 0
                    for elem in Set :
                        print("processing elem ",elem)
                        if action !=  None:

                            parser = Parser(Set[n:])
                            ast,pos = parser.Parse()
                            # Set = Set[pos.idx-1:]
                            if action  == "setVal":
                                value = JCI.visit(ast)
                                concerned.value = value
                                print(value)
                                variable = Variable()
                                variable.setAttr("type",concerned.value.type)
                                variable.setAttr("name",concerned.name.value)
                                variable.setAttr("value",concerned.value.value)
                                variables[concerned.name] = variable
                            # print(concerned)
                            # print(elem)
                            # print(n)
                            break
                        else:
                            if type(elem) == VarOp:
                                action = elem.operation
                                concerned = elem
                        n+=1
                    # parser = Parser(Set)
                    # ast,pos = parser.Parse()
                    # if (ast.type) == "VarOp" :
                    #     print(ast)
                    #     if (ast.operation) == "setVal":
                    #         # print(ast.value)
                    #         variable.setAttr("type",ast.value.type)
                    #         variable.setAttr("name",ast.name.value)
                    #         variable.setAttr("value",ast.value)
                    #         variables[ast.name] = variable
                    #     if ast.left.type == VarOp:    
                    #         print(ast.right.type)
                    #         print(ast.operator)

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

