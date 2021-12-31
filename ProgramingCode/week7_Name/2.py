class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        o = []
        for decl in ctx.decl:
            o += [self.visit(decl,o)]

    def visitVarDecl(self,ctx:VarDecl,o:object):
        n = ctx.name
        if n in o:
            raise RedeclaredVariable(n)
        return n

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        n = ctx.name
        if n in o:
            raise RedeclaredConstant(n)
        return n

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass