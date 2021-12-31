class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self, ctx: MPParser.ExpContext):
        if ctx.getChildCount() == 3:
            return Binary(ctx.ASSIGN().getText(), self.visitTerm(ctx.term()), self.visitExp(ctx.exp()))
        return self.visit(ctx.term())

    def visitTerm(self, ctx: MPParser.TermContext):
        if ctx.getChildCount() == 3:
            return Binary(ctx.COMPARE().getText(), self.visitFactor(ctx.factor(0)), self.visitFactor(ctx.factor(1)))
        return self.visit(ctx.factor(0))

    def visitFactor(self, ctx: MPParser.FactorContext):
        if ctx.getChildCount() == 3:
            return Binary(ctx.ANDOR().getText(), self.visitFactor(ctx.factor()), self.visitOperand(ctx.operand()))
        return self.visit(ctx.operand())

    def visitOperand(self, ctx: MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(True if ctx.BOOLIT().getText() == "True" else False)
        else:
            return self.visit(ctx.exp())