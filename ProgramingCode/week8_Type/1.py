class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o): 
        type1 = self.visit(ctx.e1,o)
        type2 = self.visit(ctx.e2,o)
        if ctx.op in ['+','-','*']:
            if type1 == 3 or type2 == 3:
                raise TypeMismatchInExpression(ctx)
            if type1 == 2 or type2 == 2:
                return 2
            else:
                return 1
                
        if ctx.op == '/':
            if type1 == 3 or type2 == 3:
                raise TypeMismatchInExpression(ctx)
            return 2
            
        if ctx.op == '&&' or ctx.op == '||':
            if type1 != 3 or type2 != 3:
                raise TypeMismatchInExpression(ctx)
            return 3
        
        if ctx.op in ['>','<','==','!=']:
            if type1 != type2:
                raise TypeMismatchInExpression(ctx)
            return 3
        
    def visitUnOp(self,ctx:UnOp,o):
        type0 = self.visit(ctx.e,o)
        if ctx.op == '-':
            if type0 == 3:
                raise TypeMismatchInExpression(ctx)
            return type0
        
        if ctx.op == '!':
            if type0 != 3:
                raise TypeMismatchInExpression(ctx)
            return type0

    def visitIntLit(self,ctx:IntLit,o): 
        return 1

    def visitFloatLit(self,ctx,o): 
        return 2

    def visitBoolLit(self,ctx,o): 
        return 3