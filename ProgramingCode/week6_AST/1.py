class TerminalCount(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return 1 + self.visitVardecls(ctx.vardecls())


    def visitVardecls(self,ctx:MPParser.VardeclsContext):

        return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail())

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 

        return self.visitVardecl(ctx.vardecl()) + self.visitVardecltail(ctx.vardecltail()) if ctx.vardecl() else 0

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return 1 + self.visitMptype(ctx.mptype()) + self.visitIds(ctx.ids())

    def visitMptype(self,ctx:MPParser.MptypeContext):

        return 1

    def visitIds(self,ctx:MPParser.IdsContext):

         return 2 + self.visitIds(ctx.ids()) if ctx.ids() else 1