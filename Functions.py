#!/usr/bin/env python3

from Classes import Token

def RunFunction(func,args=[Token("STRING","''")]):
    ret = 1
    for elem in func.actionBuff:
        if elem.type == 'NAME':
            if elem.value == "print":
                toShow = ""
                for lm in args:
                    if lm.type == "STRING" or lm.type == "DEC" or lm.type == "INT":
                        toShow += str(lm.value)
                print(toShow)
                ret = 0
    return (ret)

class Function():

    def __init__(self,name=None,arguments=None,actions=None,type_="FUNC"):
        self.name=name
        self.arguments=arguments
        self.actionBuff=actions
        self.type=type_

    def setAttr(self,name,value):
        if name == 'name':
            self.name = name
        if name == 'actions':
            self.actionBuff = actions
        if name == 'arguments':
            self.arguments = arguments

    def __repr__(self):
        return f"{'=F'} :{self.name}  ({self.arguments}) at {hex(id(self))}"


class FunctionArg():

    def __init__(self,name=None,type=None):
        self.name = name
        self.type = type