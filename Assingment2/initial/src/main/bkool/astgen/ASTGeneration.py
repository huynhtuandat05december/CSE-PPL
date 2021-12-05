from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])

    def visitClassdecl(self, ctx: BKOOLParser.ClassdeclContext):
        if ctx.EXTENDS():
            if ctx.memdecl():
                return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.memdecl()), Id(ctx.ID(1).getText()))
            return ClassDecl(Id(ctx.ID(0).getText()), [], Id(ctx.ID(1).getText()))
        if ctx.memdecl():
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.memdecl()))
        return ClassDecl(Id(ctx.ID(0).getText()), [])

    def visitMemdecl(self, ctx: BKOOLParser.MemdeclContext):
        if ctx.getChildCount() == 1:
            if ctx.attribute_declare():
                return self.visit(ctx.attribute_declare())
            return [self.visit(ctx.method_declare())]
        if ctx.attribute_declare():
            return self.visit(ctx.attribute_declare())+self.visit(ctx.memdecl())
        return [self.visit(ctx.method_declare())]+self.visit(ctx.memdecl())

    def visitAttribute_declare(self, ctx: BKOOLParser.Attribute_declareContext):
        if ctx.immutable_attribute():
            return self.visit(ctx.immutable_attribute())
        return self.visit(ctx.mutable_attribube())
        # Visit a parse tree produced by CSELParser#expr. true

    def visitImmutable_attribute(self, ctx: BKOOLParser.Immutable_attributeContext):
        listConstDecl = self.visit(ctx.const_decl())
        if ctx.STATIC():
            return [AttributeDecl(Static(), ConstDecl(id, dataType, expr)) for (dataType, id, expr) in listConstDecl]
        return [AttributeDecl(Instance(), ConstDecl(id, dataType, expr)) for (dataType, id, expr) in listConstDecl]

    def visitConst_decl(self, ctx: BKOOLParser.Const_declContext):
        attribute = self.visit(ctx.attribute_immutable())
        dataType = self.visit(ctx.data_type())
        return [(dataType, id, expr) for (id, expr) in attribute]

    def visitAttribute_immutable(self, ctx: BKOOLParser.Attribute_immutableContext):
        if ctx.getChildCount() == 1:
            return [(Id(ctx.ID().getText()), None)]
        if ctx.getChildCount() == 2:
            return [(Id(ctx.ID().getText()), self.visit(ctx.declare_assign()))]
        if ctx.getChildCount() == 3:
            return [(Id(ctx.ID().getText()), None)]+self.visit(ctx.attribute_immutable())
        return [(Id(ctx.ID().getText()), self.visit(ctx.declare_assign()))]+self.visit(ctx.attribute_immutable())

    def visitMutable_attribube(self, ctx: BKOOLParser.Mutable_attribubeContext):
        listVarDecl = self.visit(ctx.var_decl())
        if ctx.STATIC():
            return [AttributeDecl(Static(), VarDecl(id, dataType, expr)) for (dataType, id, expr) in listVarDecl]
        return [AttributeDecl(Instance(), VarDecl(id, dataType, expr)) for (dataType, id, expr) in listVarDecl]

    def visitVar_decl(self, ctx: BKOOLParser.Var_declContext):
        attribute = self.visit(ctx.attribute_mutable())
        dataType = self.visit(ctx.data_type())
        return [(dataType, id, expr) for (id, expr) in attribute]

    def visitAttribute_mutable(self, ctx: BKOOLParser.Attribute_mutableContext):
        if ctx.getChildCount() == 1:
            return [(Id(ctx.ID().getText()), None)]
        if ctx.getChildCount() == 2:
            return [(Id(ctx.ID().getText()), self.visit(ctx.declare_assign()))]
        if ctx.getChildCount() == 3:
            return [(Id(ctx.ID().getText()), None)]+self.visit(ctx.attribute_mutable())
        return [(Id(ctx.ID().getText()), self.visit(ctx.declare_assign()))]+self.visit(ctx.attribute_mutable())

    def visitDeclare_assign(self, ctx: BKOOLParser.Declare_assignContext):
        return self.visit(ctx.expr())
    #------------------------------------------------------------#
    # --------------------------Method------------------------#

    def visitMethod_declare(self, ctx: BKOOLParser.Method_declareContext):
        # print(ctx.parameter_list)
        if ctx.STATIC():
            if ctx.parameter_list():
                return MethodDecl(Static(), Id(ctx.ID().getText()), self.visit(ctx.parameter_list()), self.visit(ctx.function_type()), self.visit(ctx.block_statement()))
            return MethodDecl(Static(), Id(ctx.ID().getText()), [], self.visit(ctx.function_type()), self.visit(ctx.block_statement()))
        if ctx.function_type():
            if ctx.parameter_list():
                return MethodDecl(Instance(), Id(ctx.ID().getText()), self.visit(ctx.parameter_list()), self.visit(ctx.function_type()), self.visit(ctx.block_statement()))
            return MethodDecl(Instance(), Id(ctx.ID().getText()), [], self.visit(ctx.function_type()), self.visit(ctx.block_statement()))
        if ctx.parameter_list():
            return MethodDecl(Instance(), Id("<init>"), self.visit(ctx.parameter_list()), None, self.visit(ctx.block_statement()))
        return MethodDecl(Instance(), Id("<init>"), [], None, self.visit(ctx.block_statement()))

    def visitParameter_list(self, ctx: BKOOLParser.Parameter_listContext):
        if ctx.getChildCount() == 1:
            return [VarDecl(id, dataType) for (id, dataType) in self.visit(ctx.parameter())]
        return [VarDecl(id, dataType) for (id, dataType) in self.visit(ctx.parameter())]+self.visit(ctx.parameter_list())

    def visitParameter(self, ctx: BKOOLParser.ParameterContext):
        ids_list = self.visit(ctx.ids_list())
        dataType = self.visit(ctx.data_type())
        return [(id, dataType) for id in ids_list]

    def visitIds_list(self, ctx: BKOOLParser.Ids_listContext):
        if ctx.getChildCount() == 3:
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids_list())
        return [Id(ctx.ID().getText())]
    #--------------------------------------------------------#
    # --------------------------Expr------------------------#

    def visitExpr(self, ctx: BKOOLParser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))

    def visitExpr1(self, ctx: BKOOLParser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))
    # Visit a parse tree produced by CSELParser#expr2.

    def visitExpr2(self, ctx: BKOOLParser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))
    # Visit a parse tree produced by CSELParser#expr3.

    def visitExpr3(self, ctx: BKOOLParser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))
    # Visit a parse tree produced by CSELParser#expr4.

    def visitExpr4(self, ctx: BKOOLParser.Expr4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))
    # Visit a parse tree produced by CSELParser#expr5.

    def visitExpr5(self, ctx: BKOOLParser.Expr5Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))
    # Visit a parse tree produced by CSELParser#expr6.

    def visitExpr6(self, ctx: BKOOLParser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.getChild(0))
    # Visit a parse tree produced by CSELParser#expr6.

    def visitExpr7(self, ctx: BKOOLParser.Expr7Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(),  self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.getChild(0))

    def visitExpr8(self, ctx: BKOOLParser.Expr8Context):
        if ctx.expr():
            return ArrayCell(self.visit(ctx.expr9()), self.visit(ctx.expr()))
        else:
            return self.visit(ctx.expr9())

    def visitExpr9(self, ctx: BKOOLParser.Expr9Context):
        if ctx.getChildCount() == 3:
            if ctx.expr9():
                return FieldAccess(self.visit(ctx.expr9()), Id(ctx.ID(0).getText()))
            return FieldAccess(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()))
        if ctx.getChildCount() == 5:
            if ctx.expr9():
                return CallExpr(self.visit(ctx.expr9()), Id(ctx.ID(0).getText()), [])
            return CallExpr(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), [])
        if ctx.getChildCount() == 6:
            if ctx.expr9():
                return CallExpr(self.visit(ctx.expr9()), Id(ctx.ID(0).getText()), self.visit(ctx.list_of_expr()))
            return CallExpr(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), self.visit(ctx.list_of_expr()))
        return self.visit(ctx.expr10())

    def visitExpr10(self, ctx: BKOOLParser.Expr10Context):
        if ctx.NEW():
            if ctx.list_of_expr():
                return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.list_of_expr()))
            return NewExpr(Id(ctx.ID().getText()), [])
        return self.visit(ctx.getChild(0))

    def visitList_of_expr(self, ctx: BKOOLParser.List_of_exprContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitExpr11(self, ctx: BKOOLParser.Expr11Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        return self.visit(ctx.operands())

    def visitOperands(self, ctx: BKOOLParser.OperandsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.THIS():
            return SelfLiteral()
        if ctx. NIL():
            return NullLiteral()

    #-------------------------------------------------------------------------------#
    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx: BKOOLParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitBlock_statement(self, ctx: BKOOLParser.Block_statementContext):
        list_member_block = self.visit(ctx.member_block())
        return Block(list_member_block[0], list_member_block[1])

    def visitMember_block(self, ctx: BKOOLParser.Member_blockContext):
        listStmt = []
        if ctx.statement():
            for stmt in ctx.statement():
                listStmt.append(self.visit(stmt))
        return [self.visit(ctx.var_mem()), listStmt]

    def visitVar_mem(self, ctx: BKOOLParser.Var_memContext):
        if ctx.getChildCount() == 1:
            if ctx.const_member_block():
                return self.visit(ctx.const_member_block())
            if ctx.var_member_block():
                return self.visit(ctx.var_member_block())
        if ctx.getChildCount() == 2:
            if ctx.const_member_block():
                return self.visit(ctx.const_member_block()) + self.visit(ctx.var_mem())
            if ctx.var_member_block():
                return self.visit(ctx.var_member_block()) + self.visit(ctx.var_mem())
        return []

    def visitConst_member_block(self, ctx: BKOOLParser.Const_member_blockContext):
        listConstDecl = self.visit(ctx.const_decl())
        return [ConstDecl(id, dataType, expr)for (dataType, id, expr) in listConstDecl]

    def visitVar_member_block(self, ctx: BKOOLParser.Var_member_blockContext):
        listVarDecl = self.visit(ctx.var_decl())
        return [VarDecl(id, dataType, expr)for (dataType, id, expr) in listVarDecl]

    def visitAssignment_statement(self, ctx: BKOOLParser.Assignment_statementContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))

    def visitArray_cell(self, ctx: BKOOLParser.Array_cellContext):
        return ArrayCell(self.visit(ctx.expr9()), self.visit(ctx.expr()))

    def visitField_access(self, ctx: BKOOLParser.Field_accessContext):
        if ctx.expr():
            return FieldAccess(self.visit(ctx.expr()), Id(ctx.ID(0).getText()))
        return FieldAccess(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()))

    def visitIf_statement(self, ctx: BKOOLParser.If_statementContext):
        if ctx.ELSE():
            return If(self.visit(ctx.expr()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1)))
        return If(self.visit(ctx.expr()), self.visit(ctx.statement(0)))

    def visitFor_statement(self, ctx: BKOOLParser.For_statementContext):
        if ctx.TO():
            return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), True, self.visit(ctx.statement()))
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), False, self.visit(ctx.statement()))

    def visitBreak_statement(self, ctx: BKOOLParser.Break_statementContext):
        return Break()

    def visitContinue_statement(self, ctx: BKOOLParser.Continue_statementContext):
        return Continue()

    def visitReturn_statement(self, ctx: BKOOLParser.Return_statementContext):
        return Return(self.visit(ctx.expr()))

    def visitMethod_invocation_statement(self, ctx: BKOOLParser.Method_invocation_statementContext):
        return self.visit(ctx.member_access())

    def visitMember_access(self, ctx: BKOOLParser.Member_accessContext):
        if ctx.getChildCount() == 5:
            if ctx.expr():
                return CallStmt(self.visit(ctx.expr()), Id(ctx.ID(0).getText()), [])
            return CallStmt(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), [])
        if ctx.getChildCount() == 6:
            if ctx.expr():
                return CallStmt(self.visit(ctx.expr()), Id(ctx.ID(0).getText()), self.visit(ctx.list_of_expr()))
            return CallStmt(Id(ctx.ID(0).getText()), Id(ctx.ID(1).getText()), self.visit(ctx.list_of_expr()))
    #------------------------type-----------------------------------#

    def visitData_type(self, ctx: BKOOLParser.Data_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.BOOLEAN():
            return BoolType()
        return self.visit(ctx.getChild(0))

    def visitFunction_type(self, ctx: BKOOLParser.Function_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.VOID():
            return VoidType()
        return self.visit(ctx.getChild(0))

    def visitArray_type(self, ctx: BKOOLParser.Array_typeContext):
        if ctx.INT():
            type = IntType()
        if ctx.FLOAT():
            type = FloatType()
        if ctx.BOOLEAN():
            type = BoolType()
        if ctx.STRING():
            type = StringType()
        if ctx.class_type():
            type = self.visit(ctx.class_type())
        return ArrayType(int(ctx.INTLIT().getText()), type)

    def visitClass_type(self, ctx: BKOOLParser.Class_typeContext):
        return ClassType(Id(ctx.ID().getText()))
    #----------------LITERALS-----------------#

    def visitLiteral(self, ctx: BKOOLParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.BOOLLIT():
            if ctx.BOOLLIT().getText() == "true":
                return BooleanLiteral(True)
            return BooleanLiteral(False)
        return self.visit(ctx.array_lit())

    def visitArray_lit(self, ctx: BKOOLParser.Array_litContext):
        return ArrayLiteral(self.visit(ctx.array_list()))

    def visitArray_list(self, ctx: BKOOLParser.Array_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.literal())]
        return [self.visit(ctx.literal())]+self.visit(ctx.array_list())
