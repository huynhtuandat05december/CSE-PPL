class TerminalCount(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        if(self.visitVardecls(ctx.vardecls())):
            return 1+self.visitVardecls(ctx.vardecls())
        return 1

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        if (self.visitVardecl(ctx.vardecl()) >= self.visitVardecltail(ctx.vardecltail())):
            return self.visitVardecl(ctx.vardecl())+1
        return self.visitVardecltail(ctx.vardecltail())+1

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if (ctx.getChildCount() == 2 and self.visitVardecl(ctx.vardecl()) >= self.visitVardecltail(ctx.vardecltail())):
            return self.visitVardecl(ctx.vardecl())+1
        if (ctx.getChildCount() == 2 and self.visitVardecl(ctx.vardecl()) < self.visitVardecltail(ctx.vardecltail())):
            return self.visitVardecl(ctx.vardecl())+1
        return 0

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        if (self.visitMptype(ctx.mptype()) and self.visitMptype(ctx.mptype()) >= self.visitIds(ctx.ids())):
            return self.visitMptype(ctx.mptype())+1
        if (self.visitIds(ctx.ids()) and self.visitMptype(ctx.mptype()) < self.visitIds(ctx.ids())):
            return self.visitIds(ctx.ids())+1
        return 1

    def visitMptype(self, ctx: MPParser.MptypeContext):

        return 1

    def visitIds(self, ctx: MPParser.IdsContext):
        if (ctx.ids()):
            return self.visitIds(ctx.ids())+1
        return 1