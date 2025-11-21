class Expr:
    def __init__(self):
        print("Expr initialized")
        
    class ExprError(Exception):
        def __init__(self, message="Expr uses invalid var"):
            super().__init__(message)
            self.message = message
            
        def __repr__(self) -> str:
            return f"ExprError({self.message!r})"
            
        def __str__(self):
            return f"ExprError: {self.message}"
        
    class Const:
        __match_args__ = ("v",)
        
        def __init__(self, v):
            if not isinstance(v, (int, float)):
                raise ValueError
            else:
                self.v = v          # initializes float or int
                
        def __repr__(self) -> str:
            return f"Const({self.v!r})"
        
        def __str__(self):
            return f"{self.v}"
        
    class Ident:
        __match_args__ = ("s",)
        
        def __init__(self, s):
            if not isinstance(s, str):
                raise ValueError
            else:
                self.s = s          # initializes as str
                
        def __repr__(self) -> str:
            return f"Ident({self.s!r})"
        
        def __str__(self):
            return f"{self.s}"
    
    # algebraic
    class Plus:
        __match_args__ = ("e1","e2")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.e1 = e1        # expression 1
                self.e2 = e2        # expression 2
                
        def __repr__(self) -> str:
            return f"Plus({self.e1!r},{self.e2!r})"
        
        def __str__(self):
            return f"{self.e1} + {self.e2}"
    
    class Minus:
        __match_args__ = ("e1","e2")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.e1 = e1        # expression 1
                self.e2 = e2        # expression 2
                
        def __repr__(self) -> str:
            return f"Minus({self.e1!r},{self.e2!r})"
        
        def __str__(self):
            return f"{self.e1} - {self.e2}"
            
    class Mult:
        __match_args__ = ("e1","e2")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.e1 = e1        # expression 1
                self.e2 = e2        # expression 2
                
        def __repr__(self) -> str:
            return f"Mult({self.e1!r},{self.e2!r})"
        
        def __str__(self):
            return f"{self.e1} * {self.e2}"
            
    class Div:
        __match_args__ = ("e1","e2")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.e1 = e1        # expression 1
                self.e2 = e2        # expression 2
                
        def __repr__(self) -> str:
            return f"Div({self.e1!r},{self.e2!r})"
        
        def __str__(self):
            return f"{self.e1} / {self.e2}"
                
    class Log:
        __match_args__ = ("x","base")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.x = e1      # number for log
                self.base = e2    # base for log, default base 10  
                
        def __repr__(self) -> str:
            return f"Log({self.x!r},{self.base!r})"
        
        def __str__(self):
            return f"Log({self.x}) base {self.base}"
        
    class Exp:
        __match_args__ = ("x","e")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.x = e1      # number for log
                self.e = e2      # base for log, default base 10  
                
        def __repr__(self) -> str:
            return f"Exp({self.x!r},{self.e!r})"
        
        def __str__(self):
            return f"{self.x} ^ {self.e}"
        
    # trig functions
    class Sine:
        __match_args__ = ("e",)
        
        def __init__(self, e):
            if not isinstance(e, Expr):
                raise ValueError
            else:
                self.e = e         # initializes as expr
                
        def __repr__(self) -> str:
            return f"Sine({self.e!r})"
        
        def __str__(self):
            return f"sine({self.e})"
        
    class Cos:
        __match_args__ = ("e",)
        
        def __init__(self, e):
            if not isinstance(e, Expr):
                raise ValueError
            else:
                self.e = e         # initializes as expr
                
        def __repr__(self) -> str:
            return f"Cos({self.e!r})"
        
        def __str__(self):
            return f"cosine({self.e})"
        
    class Tan:
        __match_args__ = ("e",)
        
        def __init__(self, e):
            if not isinstance(e, Expr):
                raise ValueError
            else:
                self.e = e         # initializes as expr
                
        def __repr__(self) -> str:
            return f"Tan({self.e!r})"
        
        def __str__(self):
            return f"tangent({self.e})"
    
    # conditionals
    # greater than equal to
    class Geq:
        __match_args__ = ("e1","e2")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.e1 = e1      # number for log
                self.e2 = e2    # base for log, default base 10  
                
        def __repr__(self) -> str:
            return f"Geq({self.e1!r},{self.e2!r})"
        
        def __str__(self):
            return f"{self.e1} >= {self.e2}"
        
    # greater than
    class Great:
        __match_args__ = ("e1","e2")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.e1 = e1      # number for log
                self.e2 = e2    # base for log, default base 10  
                
        def __repr__(self) -> str:
            return f"Great({self.e1!r},{self.e2!r})"
        
        def __str__(self):
            return f"{self.e1} > {self.e2}"
    
    # less than equal to
    class Leq:
        __match_args__ = ("e1","e2")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.e1 = e1      # number for log
                self.e2 = e2    # base for log, default base 10  
                
        def __repr__(self) -> str:
            return f"Leq({self.e1!r},{self.e2!r})"
        
        def __str__(self):
            return f"{self.e1} <= {self.e2}"
    
    # less than    
    class Less:
        __match_args__ = ("e1","e2")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.e1 = e1      # number for log
                self.e2 = e2    # base for log, default base 10  
                
        def __repr__(self) -> str:
            return f"Great({self.e1!r},{self.e2!r})"
        
        def __str__(self):
            return f"{self.e1} < {self.e2}"
    
    class Eq:
        __match_args__ = ("e1","e2")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.e1 = e1      # number for log
                self.e2 = e2    # base for log, default base 10  
                
        def __repr__(self) -> str:
            return f"Eq({self.e1!r},{self.e2!r})"
        
        def __str__(self):
            return f"{self.e1} == {self.e2}"
        
    # not equal to
    class Neq:
        __match_args__ = ("e1","e2")
        
        def __init__(self, e1, e2):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr):
                raise ValueError
            else:
                self.e1 = e1        # expr 1
                self.e2 = e2        # expr 2
                
        def __repr__(self) -> str:
            return f"Neq({self.e1!r},{self.e2!r})"
        
        def __str__(self):
            return f"{self.e1} != {self.e2}"
    
    # if then else
    class IfThenElse:
        __match_args__ = ("e1","e2","e3")
        
        def __init__(self, e1, e2, e3):
            if not isinstance(e1, Expr) or not isinstance(e2, Expr) or not isinstance(e3, Expr):
                raise ValueError
            else:
                self.e1 = e1        # expr 1
                self.e2 = e2        # expr 2
                self.e3 = e3        # expr 3
                
        def __repr__(self) -> str:
            return f"IfThenElse({self.e1!r},{self.e2!r},{self.e3!r})"
        
        def __str__(self):
            return f"If ({self.e1}):\n\t{self.e2}\nelse\n\t{self.e3}"
            
    # function
    class FunDef:
        pass
    
    class FunCall:
        pass
    
    # reference
    class NewRef:
        pass
    
    class AssignRef:
        pass
    
    class DeRef:
        pass
    
    # let
    class Let:
        pass
    
    class LetRec:
        pass

