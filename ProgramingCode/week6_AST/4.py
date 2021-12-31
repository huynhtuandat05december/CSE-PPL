class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        vardecls = self.visit(ctx.vardecls())
        return Program(vardecls)

    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        vardecl = self.visit(ctx.vardecl())
        vardecltail = self.visit(ctx.vardecltail())
        if vardecltail is None:
            return vardecl
        return vardecl + vardecltail

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 
        if ctx.vardecltail() is None:
            return None
        vardecl = self.visit(ctx.vardecl())
        vardecltail = self.visit(ctx.vardecltail())
        if vardecltail is None:
            return vardecl
        return vardecl + vardecltail

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
        if ctx.ids() is None:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.ids())

