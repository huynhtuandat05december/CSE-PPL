class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        body = []
        for decl in ctx.vardecl():
            body = body + self.visit(decl)
        return Program(body)

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        typ = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        list_var = []
        for i in ids:
            list_var.append(VarDecl(i,typ))
        return list_var


    def visitMptype(self,ctx:MPParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):
        list_id=ctx.ID()
        result = []
        for i in list_id:
            result.append(Id(i.getText()))
        return result

