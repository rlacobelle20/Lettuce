from Classes.expr import Expr
from Classes.value import Value
from Classes.environment import Environment
import math

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
                
# helper functs for eval
# check values                
def valueToNum(v):
    match v:
        case Value.NumValue(f): 
            return f
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
    

# evaluate expr based on env
def evalExpr(e: Expr, env: Environment):
    # helper functions
    def applyAlg2(e1,e2,fun):
        v1 = valueToNum(evalExpr(e1,env))
        v2 = valueToNum(evalExpr(e2,env))
        v3 = fun(v1,v2)
        return Value.NumValue(v3)
        
    match e:
        case Expr.Const(n):
            match n:
                case Value.NumValue(f):
                    return f
                case _:
                    return Value.ErrorValue()
                
        case Expr.Ident(s):
            return lookupEnv(env,s)
        
        # algebraic and artithmetic
        case Expr.Plus(e1,e2):
            v1 = evalExpr(e1, env)
            v2 = evalExpr(e2, env)
            return v1 + v2
        
        case Expr.Minus(e1,e2):
            v1 = evalExpr(e1, env)
            v2 = evalExpr(e2, env)
            return v1 - v2
        
        case Expr.Mult(e1,e2):
            v1 = evalExpr(e1, env)
            v2 = evalExpr(e2, env)
            return v1 * v2

        case Expr.Div(e1,e2):
            v1 = evalExpr(e1, env)
            if (v1 == 0.0):
                raise Expr.ExprError(f"e1 cannot be 0")
            v2 = evalExpr(e2, env)
            return v1 / v2
        
        case Expr.Log(x,base):
            if (base <= 0.0):
                raise Expr.ExprError(f"{base} is an invalid base")
            else:
                v1 = evalExpr(x, env)
                v2 = evalExpr(base, env)
                return math.log(v1,v2)
            
        case Expr.Exp(e1,e2):
            v1 = evalExpr(e1, env)
            v2 = evalExpr(e2, env)
            return v1 ** v2
        
        # trig
        case Expr.Sine(e1):
            v1 = evalExpr(e1, env)
            return math.sin(v1)
        
        case Expr.Cos(e1):
            v1 = evalExpr(e1, env)
            return math.cos(v1)
        
        case Expr.Tan(e1):
            v1 = evalExpr(e1, env)
            return math.tan(v1)
            
        # conditionals
        case Expr.Geq(e1,e2):
            v1 = evalExpr(e1, env)
            v2 = evalExpr(e2, env)
            return v1 >= v2 
        
        case Expr.Great(e1,e2):
            v1 = evalExpr(e1, env)
            v2 = evalExpr(e2, env)
            return v1 > v2 
        
        case Expr.Leq(e1,e2):
            v1 = evalExpr(e1, env)
            v2 = evalExpr(e2, env)
            return v1 <= v2 
        
        case Expr.Less(e1,e2):
            v1 = evalExpr(e1, env)
            v2 = evalExpr(e2, env)
            return v1 < v2 
        
        case Expr.Eq(e1,e2):
            v1 = evalExpr(e1, env)
            v2 = evalExpr(e2, env)
            return v1 == v2 
        
        case Expr.Neq(e1,e2):
            v1 = evalExpr(e1, env)
            v2 = evalExpr(e2, env)
            return v1 != v2 