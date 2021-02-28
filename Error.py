#!/usr/bin/env python3



class JCError():
    def __init__(self,pos,message,cause):
        self.type = 'JCError'
        self.pos = pos
        self.message = message
        self.cause = cause

    def __repr__(self):
        return f'{self.type}:{self.message} at {pos.line}>>{pos.start} : {self.cause.value[pos.start]}'

    
class JCSyntaxError(JCError):
    def __init__(self,pos,message,cause):
        super().__init__(pos,message,cause)
        self.type = "JCSyntaxError"
    
class JCKeywordError(JCError):
    def __init__(self,pos,message,cause):
        super().__init__(pos,message,cause)
        self.type = "JCSyntaxError"


Errs = {
    "JCError":JCError
    ,"JCSyntaxError":JCSyntaxError
    ,"JCKeywordError":JCKeywordError
}

class ErrorResponse():


    def register(self,errName,errPos,errCause,errMessage):
        self.Errs.append(getattr(Errs,errCause,self.JCError)(errPos,errCause,errMessage))
    
    def show(self):
        return self.Errs

    def getLast(self):
        return self.Errs[-1]

    def __init__(self):
        self.Errs = [None]
