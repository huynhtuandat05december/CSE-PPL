from functools import reduce
class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):

        return self.visit(ctx.exp())

    def visitExp(self, ctx: MPParser.ExpContext):
        if len(ctx.ASSIGN()) == 0: return self.visit(ctx.term(0))
        assigns = ctx.ASSIGN()
        terms = ctx.term()
        lst = list(zip(assigns, terms[:-1]))[::-1] # zip and reverse
        return reduce(lambda x,y: Binary(y[0].getText(), self.visit(y[1]), x), lst, self.visit(terms[-1]))


    def visitTerm(self, ctx: MPParser.TermContext):
        if ctx.getChildCount() == 3:
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        return self.visit(ctx.factor(0))

    def visitFactor(self, ctx: MPParser.FactorContext):
        df = list(zip(ctx.ANDOR(), ctx.operand()[1:]))
        return reduce(lambda x, y: Binary(y[0].getText(), x, self.visit(y[1])), df, self.visit(ctx.operand(0)))

    def visitOperand(self, ctx: MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(True if ctx.BOOLIT().getText() == "True" else False)
        else:
            return self.visit(ctx.exp())
