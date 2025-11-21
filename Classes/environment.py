from value import Value
from expr import Expr

class Environment:
    def __init__(self):
        print("Created environemnt")
        
    class EnvError(Exception):
        def __init__(self, message="Could not find value in env"):
            super().__init__(message)
            self.message = message
            
        def __repr__(self) -> str:
            return f"EnvError({self.message!r})"
            
        def __str__(self):
            return f"EnvError: {self.message}"
        
    class EmptyEnv:
        def __repr__(self) -> str:
            return "EmptyEnv()"
              
    class Extend:
        __match_args__ = ("x", "v", "sigma")
        
        def __init__(self, x, v, sigma):
            if not isinstance(x, str) or not isinstance(v, Value) or not isinstance(sigma, Environment):
                raise Value.ErrorValue
            else:
                self.x = x
                self.v = v
                self.sigma = sigma
                
        def __repr__(self) -> str:
            return f"Extend({self.x!r}, {self.v!r}, {self.sigma!r})"
                
    class ExtendRec:
        __match_args__ = ("f", "x", "e", "sigma")
        
        def __init__(self, f, x, e, sigma):
            if not isinstance(f, str) or not isinstance(x, str) or not isinstance(e, Expr) or not isinstance(sigma, Environment):
                raise Value.ErrorValue
            else:
                self.f = f
                self.x = x
                self.e = e
                self.sigma = sigma
        
        def __repr__(self) -> str:
            return f"ExtendRec({self.f!r}, {self.x!r}, {self.e!r}, {self.sigma!r})"
                
    class ExtendMutualRec2:
        __match_args__ = ("f1", "x1", "e1", "f2", "x2", "e2", "sigma")
        
        def __init__(self, f1, x1, e1, f2, x2, e2, sigma):
            if not isinstance(f1, str) or not isinstance(x1, str) or not isinstance(e1, Expr) or not isinstance(f2, str) or not isinstance(x2, str) or not isinstance(e2, Expr) or not isinstance(sigma, Environment):
                raise Value.ErrorValue
            else:
                self.f1 = f1
                self.x1 = x1
                self.e1 = e1
                self.f2 = f2
                self.x2 = x2
                self.e2 = e2
                self.sigma = sigma
                
        def __repr__(self) -> str:
            return f"ExtendRec({self.f1!r}, {self.x1!r}, {self.e1!r}, {self.f2!r}, {self.x2!r}, {self.e2!r}, {self.sigma!r})"
                
# looks up val in env 
def lookupEnv(pi, x: str): 
    match pi:
        case Environment.EmptyEnv(): 
            raise Environment.EnvError(f"Value: {x} not found")
        case Environment.Extend(y, v, tail):
            if (x == y):
                return v
            else:
                return lookupEnv(tail,x)
        case Environment.ExtendRec(f,y,e,sigma):
            if (x == f):
                Value.Closure(y, e, pi)
            else:
                lookupEnv(sigma, x)
        case Environment.ExtendMutualRec2(f1,x1,e1,f2,x2,e2,sigma):
            if (x == f1):
                Value.Closure(x1,e1,pi)
            elif (x == f2):
                Value.Closure(x2,e2,pi)
            else:
                lookupEnv(sigma,x)