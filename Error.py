#!/usr/bin/env python3



class JCError():
    def __init__(self,pos,message,cause):
        self.type = 'JCError'
        self.pos = pos
        self.message = message
        self.cause = cause

    def __repr__(self):
        return f'{self.type}:{self.message} -- at {self.pos.line}>>{self.pos.start} : {self.cause.value}'

    
class JCSyntaxError(JCError):
    def __init__(self,pos,message,cause):
        super().__init__(pos,message,cause)
        self.type = "JCSyntaxError"
    
class JCKeywordError(JCError):
    def __init__(self,pos,message,cause):
        super().__init__(pos,message,cause)
        self.type = "JCSyntaxError"

    def __repr__(self):
        return f'{self.type}:{self.message}\n\t<at column {self.pos.start} in {self.pos.file} >\n\tin line {self.pos.line} :\n\tat ={self.cause.value}'


TErrs = {
    "JCError":JCError
    ,"JCSyntaxError":JCSyntaxError
    ,"JCKeyWordError":JCKeywordError
}

class ErrorResponse():

    def flush(self):
        self.Errs = []

    def register(self,errName,errPos,errCause,errMessage):
        self.Errs.append(TErrs[errName](errPos,errMessage,errCause))
        
    def show(self):
        return self.Errs

    def getLast(self):
        return self.Errs[-1]

    def __init__(self):
        self.Errs = []
