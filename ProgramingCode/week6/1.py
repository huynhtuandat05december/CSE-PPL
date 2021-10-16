class TerminalCount(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return None

    def visitVardecls(self,ctx:MPParser.VardeclsContext):

        return None

    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 

        return None

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return None

    def visitMptype(self,ctx:MPParser.MptypeContext):

        return None

    def visitIds(self,ctx:MPParser.IdsContext):

        return None