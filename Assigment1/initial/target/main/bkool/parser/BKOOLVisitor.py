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


    # Visit a parse tree produced by BKOOLParser#class_declare.
    def visitClass_declare(self, ctx:BKOOLParser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#members.
    def visitMembers(self, ctx:BKOOLParser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_declare.
    def visitAttribute_declare(self, ctx:BKOOLParser.Attribute_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl.
    def visitVar_decl(self, ctx:BKOOLParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutable_attribute.
    def visitImmutable_attribute(self, ctx:BKOOLParser.Immutable_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutable_attribute.
    def visitMutable_attribute(self, ctx:BKOOLParser.Mutable_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_declare.
    def visitMethod_declare(self, ctx:BKOOLParser.Method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr6.
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr7.
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr8.
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr9.
    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr10.
    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr11.
    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_of_expr.
    def visitList_of_expr(self, ctx:BKOOLParser.List_of_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_statement.
    def visitBlock_statement(self, ctx:BKOOLParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member_block.
    def visitMember_block(self, ctx:BKOOLParser.Member_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignment_statement.
    def visitAssignment_statement(self, ctx:BKOOLParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_statement.
    def visitIf_statement(self, ctx:BKOOLParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_statement.
    def visitFor_statement(self, ctx:BKOOLParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_statement.
    def visitBreak_statement(self, ctx:BKOOLParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_statement.
    def visitContinue_statement(self, ctx:BKOOLParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_statement.
    def visitReturn_statement(self, ctx:BKOOLParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member_access.
    def visitMember_access(self, ctx:BKOOLParser.Member_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invocation_statement.
    def visitMethod_invocation_statement(self, ctx:BKOOLParser.Method_invocation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#data_type.
    def visitData_type(self, ctx:BKOOLParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#type_not_void.
    def visitType_not_void(self, ctx:BKOOLParser.Type_not_voidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx:BKOOLParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute.
    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter.
    def visitParameter(self, ctx:BKOOLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter_list.
    def visitParameter_list(self, ctx:BKOOLParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_lit.
    def visitArray_lit(self, ctx:BKOOLParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_declare.
    def visitArray_declare(self, ctx:BKOOLParser.Array_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_list.
    def visitArray_list(self, ctx:BKOOLParser.Array_listContext):
        return self.visitChildren(ctx)



del BKOOLParser