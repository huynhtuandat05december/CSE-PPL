
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class GetEnv(BaseVisitor, Utils):

    def __init__(self):
        self.globalEnv = {}

    def visitProgram(self, ctx: Program, o: object):
        o = self.globalEnv
        for x in ctx.decl:
            self.visit(x, o)
        return o

    def visitClassDecl(self, ast: ClassDecl, o: object):
        name = ast.classname.name
        if o.get(name) is not None:
            raise Redeclared(Class(), name)
        o[name] = {}
        for x in ast.memlist:
            self.visit(x, o[name])

    def visitAttributeDecl(self, ast: AttributeDecl, o: object):
        if type(ast.kind) is Instance:
            self.visit(ast.decl, ('instance', o))
        if type(ast.kind) is Static:
            self.visit(ast.decl, ('static', o))

    def visitVarDecl(self, ctx: VarDecl, o: object):
        kind, env = o
        name = ctx.variable.name
        if env.get(name) is not None:
            raise Redeclared(Attribute(), name)
        env[name] = ('mutable', self.visit(ctx.varType, env), kind)
        return('mutable', self.visit(ctx.varType, env), kind)

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        kind, env = o
        name = ctx.constant.name
        if env.get(name) is not None:
            raise Redeclared(Attribute(), name)
        env[name] = ('immutable', self.visit(ctx.constType, env), kind)

    def visitMethodDecl(self, ctx: MethodDecl, o: object):
        if type(ctx.kind) is Instance:
            kind = 'instance'
        if type(ctx.kind) is Static:
            kind = 'static'
        if o.get(ctx.name.name) is not None:
            raise Redeclared(Method(), ctx.name.name)
        params = ctx.param
        if ctx.returnType is not None:
            param = list(map(lambda x: self.visit(x, (None, {})), params))
            o[ctx.name.name] = ('method', self.visit(
                ctx.returnType, o), kind, param)
        else:
            param = list(map(lambda x: self.visit(x, (None, {})), params))
            o[ctx.name.name] = ('method', None, kind, param)

    def visitIntType(self, ast, param):
        return IntType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitArrayType(self, ast, param):
        return ast

    def visitClassType(self, ast, param):
        env = self.globalEnv
        if ast.classname.name in env:
            return ClassType(ast.classname)
        raise Undeclared(Class(), ast.classname.name)


class ExpUtils:
    @ staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    @ staticmethod
    def isNotConst(expType):
        return type(expType) in [CallExpr, NewExpr, ArrayCell, ArrayType]

    @ staticmethod
    def isNotAccess(expType):
        return type(expType) not in [CallExpr, FieldAccess, CallStmt]


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        env = GetEnv().visit(ast, None)
        return [self.visit(x, env) for x in ast.decl]

    def visitClassDecl(self, ast: ClassDecl, o):
        env = {}
        env['current'] = ast.classname.name
        env['global'] = o
        # env['local'] = [{}]
        if ast.parentname is not None:
            if env['global'].get(ast.parentname.name) is not None:
                env['parent'] = ast.parentname.name
            else:
                raise Undeclared(Class(), ast.parentname.name)
        else:
            env['parent'] = None
        for x in ast.memlist:
            self.visit(x, env)

    def visitAttributeDecl(self, ast: AttributeDecl, o: object):
        env = o
        if type(ast.decl) is VarDecl:
            self.visit(ast.decl, (Variable(), env))
        if type(ast.decl) is ConstDecl:
            self.visit(ast.decl, (Constant(), env))

    def visitMethodDecl(self, ast: MethodDecl, o):
        env = {}
        env['global'] = o['global']
        env['local'] = [{}]
        env['current'] = o['current']
        env['parent'] = o['parent']
        [self.visit(param, (Parameter(), env))
         for param in ast.param]
        decls = ast.body.decl
        stmts = ast.body.stmt
        for decl in decls:
            if type(decl) is VarDecl:
                self.visit(decl, (Variable(), env))
            if type(decl) is ConstDecl:
                self.visit(decl, (Constant(), env))
        for stmt in stmts:
            if type(stmt) is not Return:
                self.visit(stmt, (False, env))
            else:
                typeMethod = self.visit(ast.returnType, o)
                self.visit(stmt, (typeMethod, env))

    def visitBlock(self, ast: Block, o):
        inLoop, env1 = o
        env = {}
        env['global'] = env1['global']
        env['local'] = [{}]+env1['local']
        env['current'] = env1['current']
        env['parent'] = env1['parent']
        decls = ast.decl
        stmts = ast.stmt
        for decl in decls:
            if type(decl) is VarDecl:
                self.visit(decl, (Variable(), env))
            if type(decl) is ConstDecl:
                self.visit(decl, (Constant(), env))
        [self.visit(stmt, (inLoop, env)) for stmt in stmts]

    def visitVarDecl(self, ast: VarDecl, o: object):
        kind, env = o
        name = ast.variable.name
        typeOfVar = self.visit(ast.varType, env)
        if ast.varInit is not None:
            value = self.visit(ast.varInit, env)
            if value[0] == 'mutable' or value[0] == 'immutable' or value[0] == 'method':
                if ExpUtils.isNotAccess(ast.varInit):
                    raise Undeclared(Identifier(), ast.varInit.name)
        if env.get('local') is not None:
            if env['local'][0].get(name) is not None:
                raise Redeclared(kind, name)
            env['local'][0][name] = ('var', typeOfVar, None)

    def visitConstDecl(self, ast: ConstDecl, o: object):
        kind, env = o
        name = ast.constant.name
        if ast.value is None:
            raise IllegalConstantExpression(ast.value)
        if ExpUtils.isNotConst(ast.value):
            raise IllegalConstantExpression(ast.value)

        valueCheck = self.visit(ast.value, (True, env))
        if valueCheck[0] == 'mutable' or valueCheck[0] == 'immutable' or valueCheck[0] == 'method':
            if ExpUtils.isNotAccess(ast.value):
                raise Undeclared(Identifier(), ast.value.name)
        if valueCheck[0] == 'var' or valueCheck[0] == 'mutable':
            raise IllegalConstantExpression(ast.value)
        value = self.visit(ast.value, env)[1]
        typeOfConst = self.visit(ast.constType, o)
        if env.get('local') is not None:
            if env['local'][0].get(name) is not None:
                raise Redeclared(kind, name)
        if type(typeOfConst) is ArrayType and type(value) is ArrayType:
            if typeOfConst.size != value.size:
                raise TypeMismatchInConstant(ast)
            if type(typeOfConst.eleType) is not type(value.eleType):
                if not (type(typeOfConst.eleType) is FloatType and type(value.eleType) is IntType):
                    raise TypeMismatchInConstant(ast)
        if type(value) is not type(typeOfConst):
            if not (type(typeOfConst) is FloatType and type(value) is IntType):
                raise TypeMismatchInConstant(ast)
        if env.get('local') is not None:
            env['local'][0][name] = ('const', typeOfConst, None)

    def visitId(self, ast: Id, o):
        if type(o) is tuple:
            checkConst, env = o
        else:
            env = o
        if env.get('local') is not None:
            for local in env['local']:
                if ast.name in local:
                    return local[ast.name]
        if ast.name in env['global'][env['current']]:
            return env['global'][env['current']][ast.name]
        if env['parent'] is not None:
            if ast.name in env['global'][env['parent']]:
                return env['global'][env['parent']][ast.name]
        raise Undeclared(Identifier(), ast.name)

    def visitAssign(self, ast, o):
        inLoop, env = o
        lhs = self.visit(ast.lhs, env)
        exp = self.visit(ast.exp, env)

        kindlhs = lhs[0]
        typeLhs = lhs[1]
        typeExp = exp[1]
        if kindlhs == 'const' or kindlhs == 'immutable':
            raise CannotAssignToConstant(ast)
        if lhs[0] == 'mutable' or lhs[0] == 'immutable' or lhs[0] == 'method':
            if ExpUtils.isNotAccess(ast.lhs):
                raise Undeclared(Identifier(), ast.lhs.name)
        if exp[0] == 'mutable' or exp[0] == 'immutable' or exp[0] == 'method':
            if ExpUtils.isNotAccess(ast.exp):
                raise Undeclared(Identifier(), ast.exp.name)
        if type(typeLhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(typeLhs) is ArrayType and type(typeExp) is ArrayType:
            if typeLhs.size != typeExp.size:
                raise TypeMismatchInStatement(ast)
            if type(typeLhs.eleType) is not type(typeExp.eleType):
                if not (type(typeLhs.eleType) is FloatType and type(typeExp.eleType) is IntType):
                    raise TypeMismatchInStatement(ast)
        if not ((type(typeLhs) is type(typeExp)) or (type(typeLhs) is FloatType and type(typeExp) is IntType)):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast: If, o):
        inLoop, env = o
        condType = self.visit(ast.expr, env)
        if condType[0] == 'mutable' or condType[0] == 'immutable' or condType[0] == 'method':
            if ExpUtils.isNotAccess(ast.expr):
                raise Undeclared(Identifier(), ast.expr.name)
        if type(condType[1]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, (inLoop, env))
        self.visit(ast.elseStmt, (inLoop, env))

    def visitFor(self, ast: For, o):
        inLoop, env = o

        idType = self.visit(ast.id, env)
        # Check Type Expression
        exp1Type = self.visit(ast.expr1, env)
        exp2Type = self.visit(ast.expr2, env)

        if idType[0] == 'mutable' or idType[0] == 'immutable' or idType[0] == 'method':
            if ExpUtils.isNotAccess(ast.id):
                raise Undeclared(Identifier(), ast.id.name)
        if exp1Type[0] == 'mutable' or exp1Type[0] == 'immutable' or exp1Type[0] == 'method':
            if ExpUtils.isNotAccess(ast.expr1):
                raise Undeclared(Identifier(), ast.expr1.name)
        if exp2Type[0] == 'mutable' or exp2Type[0] == 'immutable' or exp2Type[0] == 'method':
            if ExpUtils.isNotAccess(ast.expr2):
                raise Undeclared(Identifier(), ast.expr2.name)
        if idType[0] == 'const' or idType[0] == 'immutable':
            raise CannotAssignToConstant(ast.expr1)
        if False in [type(x) is IntType for x in [exp1Type[1], exp2Type[1]]]:
            raise TypeMismatchInStatement(ast)
        if ExpUtils.isNaNType(idType[1]):
            raise TypeMismatchInStatement(ast)
        # Visit statements
        self.visit(ast.loop, (True, env))

    def visitContinue(self, ast, o):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ast)

    def visitBreak(self, ast, o):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ast)

    def visitReturn(self, ast, o):
        typeMethod, env = o
        typeReturn = self.visit(ast.expr, o)
        if typeReturn[0] == 'mutable' or typeReturn[0] == 'immutable' or typeReturn[0] == 'method':
            if ExpUtils.isNotAccess(ast.expr):
                raise Undeclared(Identifier(), ast.expr.name)
        if type(typeMethod) is not type(typeReturn[1]):
            if not (type(typeMethod) is FloatType and type(typeReturn[1]) is IntType):
                raise TypeMismatchInStatement(ast)

    def visitBinaryOp(self, ast: BinaryOp, o):
        if type(o) is tuple:
            if ExpUtils.isNotConst(ast.left):
                raise IllegalConstantExpression(ast)
            if ExpUtils.isNotConst(ast.right):
                raise IllegalConstantExpression(ast)
            lType = self.visit(ast.left, o)
            rType = self.visit(ast.right, o)
            if lType[0] == 'var' or lType[0] == 'mutable':
                raise IllegalConstantExpression(ast)
            if rType[0] == 'var' or rType[0] == 'mutable':
                raise IllegalConstantExpression(ast)
        else:
            lType = self.visit(ast.left, o)
            rType = self.visit(ast.right, o)
        if lType[0] == 'mutable' or lType[0] == 'immutable' or lType[0] == 'method':
            if ExpUtils.isNotAccess(ast.left):
                raise Undeclared(Identifier(), ast.left.name)
        if rType[0] == 'mutable' or rType[0] == 'immutable' or rType[0] == 'method':
            if ExpUtils.isNotAccess(ast.right):
                raise Undeclared(Identifier(), ast.right.name)
        op = str(ast.op)
        if op in ["+", "-", "*"]:
            if ExpUtils.isNaNType(lType[1]) or ExpUtils.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ast)
            if type(lType[1]) is FloatType or type(rType[1]) is FloatType:
                return (None, FloatType(), None)
            return (None, IntType(), None)
        if op in ["/"]:
            if ExpUtils.isNaNType(lType[1]) or ExpUtils.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ast)
            return (None, FloatType(), None)
        if op in ["\\", "%"]:
            if not (type(lType[1]) is IntType) or not (type(rType[1]) is IntType):
                raise TypeMismatchInExpression(ast)
            return (None, IntType(), None)
        if op in ["==", "!="]:
            if type(lType[1]) is type(rType[1]):
                if (type(lType[1]) is IntType) or (type(rType[1]) is BoolType):
                    return (None, BoolType(), None)
            raise TypeMismatchInExpression(ast)
        if op in [">", "<", ">=", "<="]:
            if ExpUtils.isNaNType(lType[1]) or ExpUtils.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ast)
            return (None, BoolType(), None)
        if op in ["&&", "||"]:
            if type(lType[1]) is type(rType[1]):
                if type(lType[1]) is BoolType:
                    return (None, BoolType(), None)
            raise TypeMismatchInExpression(ast)
        if op in ["^"]:
            if type(lType[1]) is type(rType[1]):
                if type(lType[1]) is StringType:
                    return (None, StringType(), None)
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, o):
        if type(o) is tuple:
            if ExpUtils.isNotConst(ast.body):
                raise IllegalConstantExpression(ast.body)
            exp = self.visit(ast.body, o)
            if exp[0] == 'var' or exp[0] == "mutable":
                raise IllegalConstantExpression(ast.body)
            expType = exp
        else:
            expType = self.visit(ast.body, o)
        if expType[0] == 'mutable' or expType[0] == 'immutable' or expType[0] == 'method':
            if ExpUtils.isNotAccess(ast.body):
                raise Undeclared(Identifier(), ast.body.name)
        op = str(ast.op)
        if (op == '-' and ExpUtils.isNaNType(expType[1])) or (op == '!' and type(expType[1]) is not BoolType):
            raise TypeMismatchInExpression(ast)
        return (None, expType[1], None)

    def visitArrayCell(self, ast, o):
        arrType = self.visit(ast.arr, o)
        idxType = self.visit(ast.idx, o)
        if type(idxType[1]) is not IntType or type(arrType[1]) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        return (None, arrType[1], None)

    def visitCallExpr(self, ast, o):
        if type(ast.obj) is SelfLiteral:
            method = self.handleAccess(
                ast.method, (Method(), o, o['current']))
            if fieldname[2] == 'static':
                raise IllegalMemberAccess(ast)
        else:
            try:
                nameClass = self.visit(ast.obj,  o)
            except:
                if ast.obj.name in o['global']:
                    nameClass = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInExpression(ast)
                method = self.handleAccess(
                    ast.method, (Method(), o, nameClass[1].classname.name))
                if method[2] == 'static':
                    raise IllegalMemberAccess(ast)
                if type(method[1]) is VoidType:
                    raise TypeMismatchInExpression(ast)
                if method[0] != 'method':
                    raise TypeMismatchInExpression(ast)
            if type(nameClass) is str:
                method = self.handleAccess(
                    ast.method, (Method(), o, nameClass))
                if method[2] == 'instance':
                    raise IllegalMemberAccess(ast)
                if type(method[1]) is VoidType:
                    raise TypeMismatchInExpression(ast)
                if method[0] != 'method':
                    raise TypeMismatchInExpression(ast)
            paramCall = list(map(lambda x: self.visit(x, env), ast.param))
            if len(paramCall) != len(method[3]):
                raise TypeMismatchInExpression(ast)
            for i in range(len(paramCall)):
                if type(paramCall[i][1]) is not type(method[3][i][1]):
                    if not (type(method[3][i][1]) is FloatType and type(paramCall[i][1]) is IntType):
                        raise TypeMismatchInExpression(ast)
        return (None, method[1], None)

    def visitCallStmt(self, ast, o):
        inLoop, env = o
        if type(ast.obj) is SelfLiteral:
            method = self.handleAccess(
                ast.method, (Method(), o, env['current']))
            if method[2] == 'static':
                raise IllegalMemberAccess(ast)
            paramCall = list(map(lambda x: self.visit(x, env), ast.param))
        else:
            try:
                nameClass = self.visit(ast.obj,  env)
            except:
                if ast.obj.name in env['global']:
                    nameClass = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInStatement(ast)
                method = self.handleAccess(
                    ast.method, (Method(), env, nameClass[1].classname.name))
                if method[2] == 'static':
                    raise IllegalMemberAccess(ast)
                if type(method[1]) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                if method[0] != 'method':
                    raise TypeMismatchInStatement(ast)
            if type(nameClass) is str:
                method = self.handleAccess(
                    ast.method, (Method(), env, nameClass))
                if method[2] == 'instance':
                    raise IllegalMemberAccess(ast)
                if type(method[1]) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                if method[0] != 'method':
                    raise TypeMismatchInStatement(ast)
            paramCall = list(map(lambda x: self.visit(x, env), ast.param))
            if len(paramCall) != len(method[3]):
                raise TypeMismatchInStatement(ast)
            for i in range(len(paramCall)):
                if type(paramCall[i][1]) is not type(method[3][i][1]):
                    if not (type(method[3][i][1]) is FloatType and type(paramCall[i][1]) is IntType):
                        raise TypeMismatchInStatement(ast)

    def visitFieldAccess(self, ast, o):
        if type(o) is tuple:
            checkConst, env = o
        else:
            env = o
        if type(ast.obj) is SelfLiteral:
            fieldname = self.handleAccess(
                ast.fieldname, (Attribute(), env, env['current']))
            if fieldname[2] == 'static':
                raise IllegalMemberAccess(ast)
        else:
            try:
                nameClass = self.visit(ast.obj,  env)
            except:
                if ast.obj.name in env['global']:
                    nameClass = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInExpression(ast)
                fieldname = self.handleAccess(
                    ast.fieldname, (Attribute(), env, nameClass[1].classname.name))
                if fieldname[2] == 'static':
                    raise IllegalMemberAccess(ast)
                if fieldname[0] == 'method':
                    raise TypeMismatchInExpression(ast)
            if type(nameClass) is str:
                fieldname = self.handleAccess(
                    ast.fieldname, (Attribute(), env, nameClass))

                if fieldname[2] == 'instance':
                    raise IllegalMemberAccess(ast)
                if fieldname[0] == 'method':
                    raise TypeMismatchInExpression(ast)
        return (fieldname[0], fieldname[1], None)

    def handleAccess(self, ast, o):
        kind, env, name = o
        if ast.name in env['global'][name]:
            return env['global'][name][ast.name]
        if env['parent'] is not None:
            if ast.name in env['global'][env['parent']]:
                return env['global'][env['parent']][ast.name]
        raise Undeclared(kind, ast.name)

    def visitNewExpr(self, ast, o):
        env = o
        if ast.classname.name in env['global']:
            classType = (None, ClassType(ast.classname), None)
        else:
            raise Undeclared(Class(), ast.classname.name)
        if (len(ast.param) != 0):
            if "<init>" in env['global'][ast.classname.name]:
                constructor = env['global'][ast.classname.name]["<init>"]
            else:
                raise Undeclared(Method(), "<init>")
            paramCall = list(map(lambda x: self.visit(x, env), ast.param))
            if len(paramCall) != len(constructor[3]):
                raise TypeMismatchInExpression(ast)
            for i in range(len(paramCall)):
                if type(paramCall[i][1]) is not type(constructor[3][i][1]):
                    if not (type(constructor[3][i][1]) is FloatType and type(paramCall[i][1]) is IntType):
                        raise TypeMismatchInExpression(ast)
        return classType

    def visitIntLiteral(self, ast, param):
        return (None, IntType(), None)

    def visitFloatLiteral(self, ast, param):
        return (None, FloatType(), None)

    def visitBooleanLiteral(self, ast, param):
        return (None, BoolType(), None)

    def visitStringLiteral(self, ast, param):
        return (None, StringType(), None)

    def visitNullLiteral(self, ast, param):
        return (None, NullLiteral(), None)

    def visitSelfLiteral(self, ast, param):
        return (None, SelfLiteral(), None)

    def visitArrayLiteral(self, ast, param):
        temp = list(map(lambda x: self.visit(x, param), ast.value))
        default = temp[0][1]
        for typeOfElement in temp:
            if type(typeOfElement[1]) is not type(default):
                raise IllegalArrayLiteral(ast)
        return (None,  ArrayType(len(temp), default), None)

    def visitIntType(self, ast, param):
        return IntType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitArrayType(self, ast, param):
        return ast

    def visitClassType(self, ast, o):
        env = o
        if ast.classname.name in env['global']:
            return ast
        raise Undeclared(Class(), ast.classname.name)
