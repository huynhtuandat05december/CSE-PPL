from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from Utils import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None, sKind=None, kind=None):
        self.name = name
        self.sKind = sKind
        self.kind = kind
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+","+str(self.value.value)+")"


class ClassData:
    def __init__(self, cname, pname, mem):
        self.cname = cname
        self.pname = pname
        self.mem = mem


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("readInt",  MType(list(), IntType()),
                   CName(self.libName), "Static", "Method",),
            Symbol("writeInt", MType([IntType()],
                   VoidType()), CName(self.libName), "Static", "Method"),
            Symbol("writeIntLn", MType([IntType()],
                   VoidType()), CName(self.libName), "Static", "Method"),
            Symbol("readFloat",  MType(list(), FloatType()),
                   CName(self.libName), "Static", "Method"),
            Symbol("writeFloat", MType([FloatType()], VoidType()), CName(
                self.libName), "Static", "Method"),
            Symbol("writeFloatLn", MType([FloatType()], VoidType()), CName(
                self.libName), "Static", "Method"),
            Symbol("readBool", MType(list(), BoolType()),
                   CName(self.libName), "Static", "Method"),
            Symbol("writeBool", MType([BoolType()], VoidType()), CName(
                self.libName), "Static", "Method"),
            Symbol("writeBoolLn", MType([BoolType()], VoidType()), CName(
                self.libName), "Static", "Method"),
            Symbol("readStr", MType(list(), StringType()),
                   CName(self.libName), "Static", "Method"),
            Symbol("writeStr",  MType([StringType()], VoidType()), CName(
                self.libName), "Static", "Method"),
            Symbol("writeStrLn",  MType([StringType()], VoidType()), CName(
                self.libName), "Static", "Method"),
        ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        globalEnv = GlobalEnv().visit(ast, None)
        gl = [ClassData("io", "", self.init())]
        gc = CodeGenVisitor(ast, gl+globalEnv, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class Const(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class GlobalEnv(BaseVisitor):
    def visitProgram(self, ast, c):
        env = list(map(lambda i: self.visit(i, c), ast.decl))
        return env

    def visitClassDecl(self, ast, c):
        self.classname = ast.classname.name
        memlist = list(map(lambda i: self.visit(i, c), ast.memlist))
        if ast.parentname is None:
            parentName = ""
        else:
            parentName = ast.parentname.name
        return ClassData(ast.classname.name, parentName, memlist)

    def visitAttributeDecl(self, ast, c):
        decl = ast.decl
        if type(ast.kind) is Static:
            sKind = "Static"
        else:
            sKind = "Instance"
        if type(decl) is VarDecl:
            if decl.varInit is None:
                value = None
            else:
                value = Index(decl.varInit)
            return Symbol(decl.variable.name, decl.varType, value, sKind, "Attribute")
        if type(decl) is ConstDecl:
            return Symbol(decl.constant.name, decl.constType, Const(decl.value), sKind, "Attribute")

    def visitMethodDecl(self, ast, c):
        if type(ast.kind) is Static:
            sKind = "Static"
        else:
            sKind = "Instance"
        return Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.classname), sKind, "Method")


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast, c):
        [self.visit(i, c)for i in ast.decl]
        return c

    def visitClassDecl(self, ast, c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        if ast.parentname == None:
            self.emit.printout(self.emit.emitPROLOG(
                self.className, "java.lang.Object"))
        else:
            self.emit.printout(self.emit.emitPROLOG(
                self.className, ast.parentname.name))
        [self.visit(ele, SubBody(None, []))
         for ele in ast.memlist if type(ele) == MethodDecl]
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), None, Block([], [])), c, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(
            consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayType(0, StringType())] if isMain else list(
            map(lambda x: x.varType, consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), consdecl.param, SubBody(frame, []))
            glenv = local.sym+glenv

        body = consdecl.body
        if len(body.decl) > 0:
            variable = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), body.decl, SubBody(frame, []))
            glenv = variable.sym+glenv
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        for x in body.decl:
            if type(x) is VarDecl and x.varInit is not None:
                self.visit(Assign(x.variable, x.varInit), SubBody(frame, glenv))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        if type(ast.kind) is Static:
            sKind = "Static"
        else:
            sKind = "Instance"
        return Symbol(ast.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.className), sKind, "Method")

    def visitAttributeDecl(self, ast, o):
        pass

    def visitVarDecl(self, ast, o):
        frame = o.frame
        env = o.sym
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            idx, ast.variable.name, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
        # if ast.varInit == None:
        #     return Symbol(ast.variable.name, ast.varType, Index(idx), None, None)
        # return Symbol(ast.variable.name, ast.varType, Index(ast.varInit), None, None)
        return Symbol(ast.variable.name, ast.varType, Index(idx), None, None)

    def visitConstDecl(self, ast, o):
        frame = o.frame
        env = o.sym
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            idx, ast.constant.name, ast.constType, frame.getStartLabel(), frame.getEndLabel(), frame))
        return Symbol(ast.constant.name, ast.constType, Const(ast.value), None, None)

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        if type(ast.obj) is SelfLiteral:
            sym = self.handleAccess(ast, o, self.className)
        else:
            obj = self.visit(ast.obj, o)
            sym = self.handleAccess(ast, o, obj[0])
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value), o.frame), BoolType()

    # def visitArrayLiteral(self, ast, o):
    #     return self.emit.emitPUSHICONST(str(ast.value), o.frame), BoolType()

    def visitArrayCell(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst

        if isLeft and ctxt.checkArrayType:
            return True, None

        arrCode, arrType = self.visit(
            ast.arr, Access(frame, symbols, True, True))
        idxCode, idxType = self.visit(
            ast.idx, Access(frame, symbols, False, True))
        # Steps: aload(address index) -> iconst(access index) -> iaload
        if isLeft:
            return [arrCode + idxCode, self.emit.emitASTORE(arrType.eleType, frame)], arrType.eleType
        return arrCode + idxCode + self.emit.emitALOAD(arrType.eleType, frame), arrType.eleType

    def visitUnaryOp(self, ast, o):
        body = self.visit(ast.body, o)
        frame = o.frame
        if str(ast.op) == '+':
            return body
        if str(ast.op) == '-':
            return body[0] + self.emit.emitNEGOP(body[1], frame), body[1]
        if str(ast.op) == '!':
            return body[0] + self.emit.emitNOT(body[1], frame), body[1]

    def visitBinaryOp(self, ast, o):
        frame = o.frame
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        op = str(ast.op)
        typeop = e2t
        if (e1t == FloatType or e2t == FloatType or op == "/"):
            typeop = FloatType
            if e1t == IntType:
                e1c = e1c + self.emit.emitI2F(frame)
            if e2t == IntType:
                e2c = e2c + self.emit.emitI2F(frame)
        if op == '+':
            return e1c + e2c + self.emit.emitADDOP(ast.op, typeop, frame), typeop
        if op == '-':
            return e1c + e2c + self.emit.emitADDOP(ast.op, typeop, frame), typeop
        if op == '*':
            return e1c + e2c + self.emit.emitMULOP(ast.op, typeop, frame), typeop
        if op == '\\':
            return e1c + e2c + self.emit.emitMULOP(ast.op, typeop, frame), typeop
        if op == '/':
            return e1c + e2c + self.emit.emitMULOP(ast.op, typeop, frame), typeop
        if op == '%':
            return e1c + e2c + self.emit.emitMOD(frame), typeop
        if op == '^':
            left_str = e1c
            right_str = e2c
            return self.emit.emitConcat("\""+left_str[6:len(left_str)-2] +
                                        right_str[6:len(right_str)-2]+"\"", frame), StringType
        if op == '&&':
            return e1c + e2c + self.emit.emitANDOP(frame), typeop
        if op == '||':
            return e1c + e2c + self.emit.emitOROP(frame), typeop
        if op in [">", ">=", "<", "<=", "!=", "=="]:
            return e1c + e2c + self.emit.emitREOP(ast.op, typeop, frame), typeop

    def visitBlock(self, ast, o):
        env = o.sym
        frame = o.frame

        frame.enterScope(False)

        nenv = reduce(lambda env, ele: SubBody(
            frame, [self.visit(ele, env)]+env.sym), ast.decl, SubBody(frame, []))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        map(lambda x: self.visit(x, SubBody(frame, nenv+env)),ast.stmt)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

    def visitIf(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        expCode, expType = self.visit(
            ast.expr, Access(frame, nenv, False, True))
        self.emit.printout(expCode)
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(label1, frame))
        self.visit(ast.thenStmt, ctxt)
        self.emit.printout(self.emit.emitGOTO(label2, frame))
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, SubBody(frame, nenv))
        self.emit.printout(self.emit.emitLABEL(label2, frame))
    def visitFor(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        exp1Code, _ = self.visit(ast.expr1, Access(frame, nenv, False, True))
        exp2Code, _ = self.visit(ast.expr2, Access(frame, nenv, False, True))
        lhsWCode, _ = self.visit(ast.id, Access(frame, nenv, True, True)) # Write code
        lhsRCode, _ = self.visit(ast.id, Access(frame, nenv, False, False)) # Read code
        
        labelS = frame.getNewLabel() # label start
        labelE = frame.getNewLabel() # label end

        # Init value
        self.emit.printout(exp1Code)
        self.emit.printout(lhsWCode)
        frame.enterLoop()
        # Loop
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        # 1. Condition
        self.emit.printout(lhsRCode)
        self.emit.printout(exp2Code)
        if ast.up:
            self.emit.printout(self.emit.emitIFICMPGT(labelE, frame))
        else:
            self.emit.printout(self.emit.emitIFICMPLT(labelE, frame))
        # 2. Statements
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        # 3. Update index
        self.emit.printout(lhsRCode)
        self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(self.emit.emitADDOP('+' if ast.up else '-', IntType(), frame))
        self.emit.printout(lhsWCode)

        self.emit.printout(self.emit.emitGOTO(labelS, frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()
    def visitContinue(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitBreak(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitAssign(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        right = self.visit(ast.exp, Access(frame, nenv, False, True))
        left = self.visit(ast.lhs, Access(frame, nenv, True, True))
        if (type(right[1]) is IntType and type(left[1]) == FloatType):
            self.emit.printout(right[0] + self.emit.emitI2F(frame))
        else:
            self.emit.printout(right[0])
        self.emit.printout(left[0])
        

    def visitReturn(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        retType = frame.returnType
        if not type(retType) is VoidType:
            expCode, expType = self.visit(
                ast.expr, Access(frame, nenv, False, True))
            if type(retType) is FloatType and type(expType) is IntType:
                expCode = expCode + self.emit.emitI2F(frame)
            self.emit.printout(expCode)
        # self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(retType, frame))
        return True

    def visitFieldAccess(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        if type(ast.obj) is SelfLiteral:
            sym = self.handleAccess(ast, o, self.className)
        else:
            obj = self.visit(ast.obj, Access(frame, ctxt.sym, True, False))
            sym = self.handleAccess(ast, o, obj[0])
        if sym is not None:
            if(ctxt.isLeft == True):
                return (self.emit.emitPUTSTATIC(obj[0]+"."+sym.name, sym.mtype, frame), sym.mtype)
            if sym.value is not None:
                return (self.emit.emitPUSHCONST(self.emit.emitExpr(sym.value, sym.mtype), sym.mtype, frame), sym.mtype)
            return (self.emit.emitGETSTATIC(obj[0]+"."+sym.name, sym.mtype, frame), sym.mtype)

    
    def visitId(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.name, nenv, lambda x: x.name)
        if sym is None:
            currentClass = self.lookup(
                self.className, self.env, lambda x: x.cname)
            sym = self.lookup(ast.name, currentClass.mem, lambda x: x.name)
        if sym is None:
            if currentClass.pname != "":
                parentClass = self.lookup(
                    currentClass.pname, self.env, lambda x: x.cname)
                sym = self.lookup(
                    ast.method, parentClass.mem, lambda x: x.name)
        if sym is not None:
            if type(sym.value) is Index or type(sym.value) is Const:
                if ctxt.isLeft == True:
                    if ctxt.isFirst == True:
                        return (self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype)
                    else:
                        if type(sym.mtype) is ClassType:
                            return (sym.mtype.classname.name, sym.mtype)
                        return (ast.name, sym.mtype)
                else:
                    if ctxt.isFirst == True:
                        if type(sym.value) is Index:
                            # if type(sym.value.value) is int:
                            return (self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype)
                            # return (self.emit.emitREADCONST(sym.value.value, sym.mtype, frame), sym.mtype)
                        if type(sym.value) is Const:
                            return (self.emit.emitREADCONST(sym.value.value, sym.mtype, frame), sym.mtype)
                    else:
                        return (ast.name, sym.mtype)
            else:
                return (ast.name, sym.mtype)
        sym = self.lookup(ast.name, self.env, lambda x: x.cname)
        if sym is not None:
            return (ast.name, ClassType(ast.name))

    def handleAccess(self, ast, o, name):
        if type(ast) is FieldAccess:
            nameField = ast.fieldname.name
        else:
            nameField = ast.method.name
        currentClass = self.lookup(name, self.env, lambda x: x.cname)
        method = self.lookup(
            nameField, currentClass.mem, lambda x: x.name)
        if method is not None:
            return method
        if currentClass.pname != "":
            return self.handleAccess(ast, o, currentClass.pname)

    def visitNewExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        new = self.emit.emitNEW(ast.classname.name, ast.param, frame)
        dup = self.emit.emitDUP(frame)
        invo = self.emit.emitINVOKESPECIAL(
            frame, ast.classname.name, MType(list(), VoidType()))
        return (new+dup+invo, MType(list(), VoidType()))