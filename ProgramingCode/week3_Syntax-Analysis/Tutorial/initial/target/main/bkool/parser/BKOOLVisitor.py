# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decllist.
    def visitDecllist(self, ctx:BKOOLParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl.
    def visitDecl(self, ctx:BKOOLParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varlist.
    def visitVarlist(self, ctx:BKOOLParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcdecl.
    def visitFuncdecl(self, ctx:BKOOLParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprdecl.
    def visitExprdecl(self, ctx:BKOOLParser.ExprdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_expr.
    def visitList_expr(self, ctx:BKOOLParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignment_statement.
    def visitAssignment_statement(self, ctx:BKOOLParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#call_statement.
    def visitCall_statement(self, ctx:BKOOLParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_statement.
    def visitReturn_statement(self, ctx:BKOOLParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#func_call.
    def visitFunc_call(self, ctx:BKOOLParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx:BKOOLParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mc_type.
    def visitMc_type(self, ctx:BKOOLParser.Mc_typeContext):
        return self.visitChildren(ctx)



del BKOOLParser