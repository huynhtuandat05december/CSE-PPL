class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        o = [[]]
        for decl in ctx.decl:
            o[0] += [self.visit(decl,o)]

    def visitVarDecl(self,ctx:VarDecl,o:object):
        n = ctx.name
        if n in o[0]:
            raise RedeclaredVariable(n)
        return n

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        n = ctx.name
        if n in o[0]:
            raise RedeclaredConstant(n)
        return n
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        n=ctx.name
        listVar=ctx.param
        listbody=ctx.body[0]
        listId=ctx.body[1]
        name=[[]]
        if n in o[0]:
            raise RedeclaredFunction(n)
        else:
            o[0].append(n)
        for nameVar in listVar:
            name[0]+=[self.visit(nameVar,name)]
        for nameBody in listbody:
            name[0]+=[self.visit(nameBody,name+o)]
        for id in listId:
            self.visit(id,name+o)
        



    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        n = ctx.name
        for a in o:
            if n in a:
                return True
        raise UndeclaredIdentifier(n)

