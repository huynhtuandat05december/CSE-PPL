class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = [{}]
        for decl in ctx.decl:
            self.visit(decl,o)
        for stmt in ctx.stmts:
            self.visit(stmt,o)

    def visitVarDecl(self,ctx:VarDecl,o):
        n=ctx.name
        if n in o[0]:
            raise Redeclared(ctx)
        else:
            o[0][ctx.name] = "none"
    def visitBlock(self,ctx:Block,o):
        block=[{}]
        listDecl=ctx.decl
        listStmts=ctx.stmts
        for nameDecl in listDecl:
           self.visit(nameDecl,block+o)
        for nameStmt in listStmts:
           self.visit(nameStmt,block+o)
    def visitAssign(self,ctx:Assign,o):
        rhs = self.visit(ctx.rhs,o)
        lhs = self.visit(ctx.lhs, o)
        if lhs == "none":
            if rhs == "none":
                raise TypeCannotBeInferred(ctx)
            for a in o:
                if ctx.lhs.name in a:
                   a[ctx.lhs.name]=rhs
                   break
            lhs = rhs
        if rhs == "none":
            if lhs == "none":
                raise TypeCannotBeInferred(ctx)
            for a in o:
                if ctx.rhs.name in a:
                    a[ctx.rhs.name]=lhs
                    break
            rhs = lhs
        if lhs != rhs:
            raise TypeMismatchInStatement(ctx)


    def visitBinOp(self,ctx:BinOp,o):
        ltype = self.visit(ctx.e1,o)
        rtype = self.visit(ctx.e2,o)

        if ctx.op in ["+", "-", "*", "/"]:
            if ltype == "none":
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]="int"
                        break
                ltype == "int"
            if rtype == "none":
                for a in o:
                    if ctx.e2.name in a:
                        a[ctx.e2.name]="int"
                        break
                rtype == "int"
            if ltype == "int" and rtype == "int":
                return "int"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ["+.", "-.", "*.", "/."]:
            if ltype == "none":
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]="float"
                        break
                ltype == "float"
            if rtype == "none":
                for a in o:
                    if ctx.e2.name in a:
                        a[ctx.e2.name]="float"
                        break
                rtype == "float"
            if ltype == "float" and rtype == "float":
                return "float"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in [">","="]:
            if ltype == "none":
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]="int"
                        break
                ltype == "int"
            if rtype == "none":
                for a in o:
                    if ctx.e2.name in a:
                        a[ctx.e2.name]="int"
                        break
                rtype == "int"
            if ltype == "int" and rtype == "int":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in [">.", "=."]:
            if ltype == "none":
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]="float"
                        break
                ltype == "float"
            if rtype == "none":
                for a in o:
                    if ctx.e2.name in a:
                        a[ctx.e2.name]="float"
                        break
                rtype == "float"
            if ltype == "float" and rtype == "float":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ["&&", "||", ">b", "=b"]:
            if ltype == "none":
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]="bool"
                        break
                ltype == "bool"
            if rtype == "none":
                for a in o:
                    if ctx.e1.name in a:
                        a[ctx.e1.name]="bool"
                        break
                rtype == "bool"
            if ltype == "bool" and rtype == "bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        typ = self.visit(ctx.e,o)
        if ctx.op == "-":
            if typ == "none":
                for a in o:
                    if ctx.e.name in a:
                        a[ctx.e.name]="int"
                        break
                typ == "int"
            if typ == "int":
                return "int"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "-.":
            if typ == "none":
                for a in o:
                    if ctx.e.name in a:
                        a[ctx.e.name]="float"
                        break
                typ == "float"
            if typ == "float":
                return "float"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "!":
            if typ == "none":
                for a in o:
                    if ctx.e.name in a:
                        a[ctx.e.name]="bool"
                        break
                typ == "bool"
            if typ == "bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "i2f":
            if typ == "none":
                for a in o:
                    if ctx.e.name in a:
                        a[ctx.e.name]="int"
                        break
                typ == "int"
            if typ == "int":
                return "float"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "floor":
            if typ == "none":
                for a in o:
                    if ctx.e.name in a:
                        a[ctx.e.name]="float"
                        break
                typ == "float"
            if typ == "float":
                return "int"
            raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return "int"

    def visitFloatLit(self,ctx,o):
        return "float"

    def visitBoolLit(self,ctx,o):
        return "bool"

    def visitId(self,ctx,o):
        n = ctx.name
        for a in o:
            if n in a:
                return a[n]
        raise UndeclaredIdentifier(n)