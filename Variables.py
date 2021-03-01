#!/usr/bin/env python3


class Variable():

    def __init__(self,name=None,value=None,type=None):
        self.name=name
        self.value=value
        self.type=type

    def setAttr(self,name,value):
        if name == 'type':
            self.type = value
        if name == 'name':
            self.name = value
        if name == 'value':
            self.value = value

    def __repr__(self):
        return f"{''} variable {self.name} at {hex(id(self))}"