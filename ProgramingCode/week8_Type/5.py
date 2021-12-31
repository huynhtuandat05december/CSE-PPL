def infer(name,typ,o):
    for env in o:
        if name in env:
            env[name] = typ
            return
            
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = [{}]
        [self.visit(decl,o) for decl in ctx.decl ]
        [self.visit(stmt,o) for stmt in ctx.stmts]

    def visitVarDecl(self,ctx:VarDecl,o): 
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = 0

    def visitFuncDecl(self,ctx:FuncDecl,o): 
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        env = [{}] + o
        [self.visit(decl,env) for decl in ctx.param ]
        nParam = len(env[0])
        [self.visit(decl,env) for decl in ctx.local ]
        [self.visit(stmt,env) for stmt in ctx.stmts ]
        param = list(env[0].values())[:nParam]
        o[0][ctx.name] = param
        
    def visitCallStmt(self,ctx:CallStmt,o):
        param = None
        for env in o:
            if ctx.name in env:
                if type(env[ctx.name]) is list: 
                    param = env[ctx.name]                
        if param == None:
            raise UndeclaredIdentifier(ctx.name)
        args = [self.visit(arg,o) for arg in ctx.args]   
        if len(args) > len(param):
            raise TypeMismatchInStatement(ctx)
        for i in range(len(param)):
            if args[i] == 0 and param[i] == 0:
                raise TypeCannotBeInferred(ctx)
            elif args[i] == 0:
                infer(ctx.args[i].name,param[i],o)
            elif param[i] == 0:
                for env in o:
                    if ctx.name in env:
                        env[ctx.name][i] = args[i]
            elif args[i] != param[i]:
                raise TypeMismatchInStatement(ctx) 
        
    def visitAssign(self,ctx:Assign,o): 
        rhs = self.visit(ctx.rhs,o)
        lhs = self.visit(ctx.lhs,o)
        if lhs == 0 and rhs == 0:
            raise TypeCannotBeInferred(ctx)
        if lhs == 0:
            lhs = rhs
            infer(ctx.lhs.name,rhs,o)
        if rhs == 0:
            rhs = lhs
            infer(ctx.rhs.name,lhs,o)
        if lhs != rhs:
            raise TypeMismatchInStatement(ctx)

    def visitIntLit(self,ctx:IntLit,o): 
        return 1

    def visitFloatLit(self,ctx,o): 
        return 2

    def visitBoolLit(self,ctx,o): 
        return 3

    def visitId(self,ctx,o): 
        for env in o:
            if ctx.name in env:
                if type(env[ctx.name]) is not list: 
                    return env[ctx.name]
        raise UndeclaredIdentifier(ctx.name)