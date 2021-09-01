from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):
    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program([FuncDecl(Id("main"),
                        [],
                        self.visit(ctx.mptype()),
                        Block([],[self.visit(ctx.body())] if ctx.body() else []))])

    def visitMptype(self,ctx:BKOOLParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        else:
            return VoidType()

    def visitBody(self,ctx:BKOOLParser.BodyContext):
        return self.visit(ctx.funcall())
  
  	
    def visitFuncall(self,ctx:BKOOLParser.FuncallContext):
        return CallExpr(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])

    def visitExp(self,ctx:BKOOLParser.ExpContext):
        if (ctx.funcall()):
            return self.visit(ctx.funcall())
        else:
            return IntLiteral(int(ctx.INTLIT().getText()))
        

