from Operands import *
from Lexer import Lexer
from Classes import Token
from Parser import Parser
from Interpreter import Interpreter
from Variables import *
from Functions import *
variables = {}
functions = {
    "show":Function("show",[FunctionArg("data","buff")],[Token("NAME","print"),Token("REF","data"),Token("ENDTOKEN","END")])
}
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
                            found = 0
                            for variable in variables:
                                
                                if variables[variable].name == token.value:
                                    found = 1
                                    token = variables[variable]
                            
                            for function in functions:
                                if functions[function].name == token.value:
                                    token = functions[function]
                            
                            found = 0
                        Set.append(token)

                    t+=1
                for Set in stack:
                    action = None
                    concerned = None
                    actual = 0
                    limit = 0
                    n = 0
                    passYourWay = 0
                    for elem in Set :
                        # print("setelem ", elem)
                        if action !=  None:
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
                                if not passYourWay:
                                    if type(elem) == Variable:
                                        print(elem.value)
                                        pass
                                    if type(elem) == Function:
                                        if len(elem.arguments) > 0 :
                                            args = []
                                            actual = n
                                            while n < len(Set) and Set[n] != None:
                                                args.append(Set[n])
                                                n+=1
                                            limit = n
                                        if len(elem.arguments) > 0 :
                                            RunFunction(elem,args)
                                            passYourWay = 1
                                        else:
                                            RunFunction(elem)
                        if passYourWay:
                            # print(actual)
                            # print(limit)
                            if actual < limit :
                                actual+=1
                            else:
                                passYourWay = 0
                                actual = 0
                                limit = 0
                            continue
                        n+=1
            stack = []
            Set = []
            tokens = []
    return {
        "start":start
    } 

