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
        global stack
        while(True):
            lexer = Lexer(input("JC>"))
            tokens,errs = lexer.Tokenize()
            if len(errs.show()) != 0:
                print(errs.getLast(),flush=1)
            else:
                Set = []
                t = 0
                for token in tokens:
                    if token.type == "ENDTOKEN":
                        stack.append(Set)
                        Set = []
                        
                    else:
                        if token.type == "NAME":
                            for variable in variables:
                                if variables[variable].name == token.value:
                                    token = variables[variable]
                                else:
                                    print(token.value)
                        Set.append(token)

                    t+=1
                for Set in stack:
                    action = None
                    concerned = None
                    n = 0
                    for elem in Set :
                        if action !=  None:
                            print(type(Set[n]))
                            parser = Parser(Set[n:])
                            ast,pos = parser.Parse()
                            if action  == "setVal":
                                value = JCI.visit(ast)
                                concerned.value = value
                                variable = Variable()
                                variable.setAttr("type",concerned.value.type)
                                variable.setAttr("name",concerned.name.value)
                                variable.setAttr("value",concerned.value.value)
                                variables[concerned.name] = variable
                                print(f'created {variable}')
                            break
                        else:
                            if type(elem) == VarOp:
                                action = elem.operation
                                concerned = elem
                            else:
                                if type(elem) == Variable:
                                    print(elem.value)
                        n+=1
            stack = []
            Set = []
            tokens = []
    return {
        "start":start
    } 

