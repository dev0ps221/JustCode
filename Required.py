from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

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
                parser = Parser(tokens)
                # print(tokens)
                ast = parser.Parse()
                # print(ast)
                Num = (JCI.visit(ast))
                print(Num.value)
                # (JCI.visit(ast))
    return {
        "start":start
    } 