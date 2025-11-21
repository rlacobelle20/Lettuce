from expr import Expr

# value class
class Value:
    def __init__(self):
        print("Type initiated")
        
    class ErrorValue(Exception):
        def __init__(self, message="Could not find value in env"):
            super().__init__(message)
            self.message = message
            
        def __repr__(self) -> str:
            return f"EnvError({self.message!r})"
            
        def __str__(self):
            return f"EnvError: {self.message}"
            
    class NumValue:
        __match_args__ = ("d",)
        
        def __init__(self, d):
            if not isinstance(d, float):
                raise Value.ErrorValue()
            else:
                self.d = d
                
        def __repr__(self) -> str:
            return f"NumValue({self.d!r})"
            
    class BoolValue:
        __match_args__ = ("b",)
        
        def __init__(self, b):
            if not isinstance(b, bool):
                raise Value.ErrorValue()
            else:
                self.b = b
                
        def __repr__(self) -> str:
            return f"BoolValue({self.b!r})"
        
    class Closure:
        __match_args__ = ("x", "e", "pi")
        
        def __init__(self, x, e, pi):
            if not isinstance(x, str) or not isinstance(e, Expr) or not isinstance(pi, dict):
                raise Value.ErrorValue()
            else:
                for k, v in pi.items():
                    if not isinstance(k, str):
                        raise TypeError("keys must be str")
                    if not isinstance(v, Value):
                        raise TypeError("values must be Value")
                    
                self.x = x
                self.e = e
                self.pi = pi

        def __repr__(self) -> str:
            return f"Closure({self.x!r}, {self.e!r}, {self.pi!r})"
            
    class Reference:
        __match_args__ = ("j",)
        
        def __init__(self, j):
            if not isinstance(j, int):
                raise Value.ErrorValue()
            else:
                self.j = j
                
        def __repr__(self) -> str:
            return f"Reference({self.j!r})"
                
# check values                
                
def valueToNum(v):
    match v:
        case Value.NumValue(d): 
            return d
        case _:
            raise Value.ErrorValue()
                
def valueToBool(v):
    match v:
        case Value.BoolValue(b): 
            return b
        case _:
            raise Value.ErrorValue()
        
def valueToClosure(v):
    match v:
        case Value.Closure(x,e,pi): 
            return Value.Closure(x,e,pi)
        case _:
            raise Value.ErrorValue()
        
def valueToReference(v):
    match v:
        case Value.Reference(f): 
            return f
        case _:
            raise Value.ErrorValue()
            
