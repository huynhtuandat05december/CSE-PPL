class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = {}
        for decl in ctx.decl:
            self.visit(decl,o)
        for stmt in ctx.stmts:
            self.visit(stmt,o)

    def visitVarDecl(self,ctx:VarDecl,o):
        o[ctx.name] = "none"

    def visitAssign(self,ctx:Assign,o):
        rhs = self.visit(ctx.rhs,o)
        lhs = self.visit(ctx.lhs, o)
        if lhs == "none":
            if rhs == "none":
                raise TypeCannotBeInferred(ctx)
            else:
                o[ctx.lhs.name] = rhs
                lhs = rhs
        if rhs == "none":
            if lhs == "none":
                raise TypeCannotBeInferred(ctx)
            o[ctx.rhs.name] = lhs
            rhs=lhs
        if lhs != rhs:
            raise TypeMismatchInStatement(ctx)


    def visitBinOp(self,ctx:BinOp,o):
        ltype = self.visit(ctx.e1,o)
        rtype = self.visit(ctx.e2,o)

        if ctx.op in ["+", "-", "*", "/"]:
            if ltype == "none":
                o[ctx.e1.name] = "int"
                ltype = "int"
            if rtype == "none":
                o[ctx.e2.name] = "int"
                rtype = "int"
            if ltype == "int" and rtype == "int":
                return "int"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ["+.", "-.", "*.", "/."]:
            if ltype == "none":
                o[ctx.e1.name] = "float"
                ltype = "float"
            if rtype == "none":
                o[ctx.e2.name] = "float"
                rtype = "float"
            if ltype == "float" and rtype == "float":
                return "float"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in [">","="]:
            if ltype == "none":
                o[ctx.e1.name] = "int"
                ltype = "int"
            if rtype == "none":
                o[ctx.e2.name] = "int"
                rtype = "int"
            if ltype == "int" and rtype == "int":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in [">.", "=."]:
            if ltype == "none":
                o[ctx.e1.name] = "float"
                ltype = "float"
            if rtype == "none":
                o[ctx.e2.name] = "float"
                rtype = "float"
            if ltype == "float" and rtype == "float":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ["&&", "||", ">b", "=b"]:
            if ltype == "none":
                o[ctx.e1.name] = "bool"
                ltype = "bool"
            if rtype == "none":
                o[ctx.e2.name] = "bool"
                rtype = "bool"
            if ltype == "bool" and rtype == "bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        typ = self.visit(ctx.e,o)
        if ctx.op == "-":
            if typ == "none":
                o[ctx.e.name] = "int"
                typ = "int"
            if typ == "int":
                return "int"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "-.":
            if typ == "none":
                o[ctx.e.name] = "float"
                typ = "float"
            if typ == "float":
                return "float"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "!":
            if typ == "none":
                o[ctx.e.name] = "bool"
                typ = "bool"
            if typ == "bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "i2f":
            if typ == "none":
                o[ctx.e.name] = "int"
                typ = "int"
            if typ == "int":
                return "float"
            raise TypeMismatchInExpression(ctx)
        if ctx.op == "floor":
            if typ == "none":
                o[ctx.e.name] = "float"
                typ = "float"
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
        if ctx.name in o:
            return o[ctx.name]
        raise UndeclaredIdentifier(ctx.name)
