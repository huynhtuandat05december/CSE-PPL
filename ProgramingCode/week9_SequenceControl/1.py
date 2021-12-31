class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        o = {}
        for i in ctx.decl:
            if o.get(i.name) is not None:
                raise RedeclaredField(i.name)
            o[i.name] = []
            self.visit(i,o[i.name])

    def visitClassDecl(self,ctx:ClassDecl,o:object):
        for i in ctx.mem:
            self.visit(i,o)

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredField(ctx.name)
        o.append(ctx.name)

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        lst = []
        if ctx.name in o:
            raise RedeclaredMethod(ctx.name)
        o.append(ctx.name)

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitClassType(self,ctx:ClassType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):pass

    def visitFieldAccess(self,ctx:FieldAccess,o:object):pass