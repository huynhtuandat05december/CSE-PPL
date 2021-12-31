class DeclCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object):
        o = {}
        for x in ctx.decl:
            o[x.name] = {}
            self.visit(x, o[x.name])
        return o

    def visitClassDecl(self,ctx:ClassDecl,o:object):
        o['parent'] = ctx.parent # need update here to ref to the parent class
        o['fields'] = {}
        o['methods'] = {}
        for x in ctx.mem:
            self.visit(x, o)

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if o.get('fields').get(ctx.name) != None:
            RedeclaredField(ctx.name)
        o['fields'][ctx.name] = ctx.typ

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if o.get('methods').get(ctx.name) != None:
            RedeclaredMethod(ctx.name)
        o['methods'][ctx.name] = {}
        for x in ctx.param:
            if o.get('methods').get(ctx.name).get(x.name) != None:
                raise RedeclaredField(x.name)
            o['methods'][ctx.name][x.name] = x.typ
        for x in ctx.body[0]:
            if o.get('methods').get(ctx.name).get(x.name) != None:
                raise RedeclaredField(x.name)
            o['methods'][ctx.name][x.name] = x.typ
        

class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object):
        env = DeclCheck().visit(ctx, None)
        o = {}
        o['classes'] = env
        for x in ctx.decl:
            self.visit(x, o)

    def visitClassDecl(self,ctx:ClassDecl,o:object):
        o['class'] = ctx.name
        for x in ctx.mem:
            self.visit(x, o)

    def visitVarDecl(self,ctx:VarDecl,o:object): pass

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        o['method'] = ctx.name
        for x in ctx.body[1]:
            self.visit(x, o)

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitClassType(self,ctx:ClassType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        if ctx.name in o.get('classes').get(o['class']).get('methods').get(o['method']):
            return o.get('classes').get(o['class']).get('methods').get(o['method']).get(ctx.name).name
        raise UndeclaredIdentifier(ctx.name)

    def visitFieldAccess(self,ctx:FieldAccess,o:object):
        curClass = self.visit(ctx.exp, o)
        while curClass != '':
            fields = o.get('classes').get(curClass).get('fields')
            if fields.get(ctx.field) != None:
                return fields.get(ctx.field)
            curClass = o.get('classes').get(curClass).get('parent')
        
        raise UndeclaredField(ctx.field)