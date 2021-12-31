from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import * 
from AST import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"

from Emitter import Emitter

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("writeInt", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("writeIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
                Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("writeFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("readStr", MType(list(), StringType()), CName(self.libName)),
                Symbol("writeStr", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("writeStrLn", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("readBool", MType(list(), BoolType()), CName(self.libName)),
                Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("writeBoolLn", MType([BoolType()], VoidType()), CName(self.libName))
                ]

    def gen(self, ast,path):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl,path)
        gc.visit(ast, None)

class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        self.value = value

class CName(Val):
    def __init__(self, value):
        self.value = value

class GetEnvi(BaseVisitor):
    """
        use to get global environment of program
    """
    def visitProgram(self,ast,o):
        envi = []
        checkAttri = []
        for i in ast.decl: envi += self.visit(i,checkAttri)
        return envi,checkAttri

    def visitClassDecl(self,ast,o):
        self.className = ast.classname.name
        envi = []

        have_constructor = False
        for ele in ast.memlist:
            if type(ele) is MethodDecl:
                if ele.name.name == "<init>": have_constructor = True
            envi += [self.visit(ele,o)]

        if not have_constructor:
            envi += [Symbol("<init>",MType([],None),CName(self.className))]
        return envi

    def visitMethodDecl(self,ast,o):
        return Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.className))

    def visitAttributeDecl(self,ast,o):
        if type(ast.decl) is VarDecl:
            name = ast.decl.variable.name
            typ = ast.decl.varType
            value = ast.decl.varInit
        else:
            name = ast.decl.constant.name
            typ = ast.decl.constType
            value = ast.decl.value
        if value:
            if type(ast.kind) is Static:
                o += [{'name':name,'type':typ,'cname':self.className,'value':value, 'kind':"static"}]
            else:
                o += [{'name':name,'type':typ,'cname':self.className,'value':value, 'kind':"instance"}]
        elif type(typ) is ArrayType:
            if type(ast.kind) is Static:
                o += [{'name':name,'type':typ,'cname':self.className,'value':None, 'kind':"static"}]
            else:
                o += [{'name':name,'type':typ,'cname':self.className,'value':None, 'kind':"instance"}]
        elif type(typ) is ClassType:
            if type(ast.kind) is Static:
                o += [{'name':name,'type':typ,'cname':self.className,'value':NullLiteral(), 'kind':"static"}]
            else:
                o += [{'name':name,'type':typ,'cname':self.className,'value':NullLiteral(), 'kind':"instance"}]
        return Symbol(name, typ, CName(self.className))


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env,path):
        self.astTree = astTree
        self.env = env
        self.path = path
    """
                SUPPORT FUNCTION
    """
    def getParent(self,ast,child):
        """
            return list contains classname and its parent name
        """
        for decl in ast.decl:
            if decl.classname.name == child:
                if decl.parentname: return [child] + self.getParent(ast,decl.parentname.name)
                else: return [child]

    def getClassParent(self,ast,o):
        """
            return list list parent of all class in program
        """
        return [self.getParent(ast,decl.classname.name) for decl in ast.decl] + [["io"]]

    def findListParent(self,name):
        """
            return list parent of class name input
        """
        for l in self.classList:
            if l[0] == name: return l

    def matchType(self,in_,param_):
        """
            return True if type of input is match with param
        """
        for i in range(len(in_)):
            if type(in_[i]) != type(param_[i]):
                if type(in_[i]) is IntType and type(param_[i]) is FloatType: continue
                return False
        return True

    def countMatch(self,in_,param_):
        """
            return num of type that input same as param
        """
        return len([i for i in range(len(in_)) if type(in_[i]) == type(param_[i])])

    def findCtype(self,ctype_list,in_):
        """
            return best ctype of list input
        """
        max_c = -1
        type_max = None
        for ctype in ctype_list:
            c = self.countMatch(in_,ctype.partype)
            if c > max_c:
                max_c = c
                type_max = ctype
        return type_max
    """
                ALL DECLARATION
    """
    def visitProgram(self, ast, c):
        envi, self.initAttribute = GetEnvi().visitProgram(ast,c)
        self.classList = self.getClassParent(ast,c)
        self.env += envi
        [self.visit(i,c) for i in ast.decl]
        return c

    def visitClassDecl(self,ast,c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        parent_class = "java/lang/Object"
        if ast.parentname: parent_class = ast.parentname.name
        self.emit.printout(self.emit.emitPROLOG(self.className, parent_class))

        local = SubBody(None,self.env)
        self.visit(AttributeDecl(Static(),VarDecl(Id("initStaticVar"),IntType())),local)

        have_constructor = False
        for ele in ast.memlist:
            if type(ele) is MethodDecl:
                if ele.name.name == "<init>": have_constructor = True
            self.visit(ele,local)
        # generate default constructor
        if not have_constructor:
            self.genMETHOD(MethodDecl(Instance(),Id("<init>"), list(), None,Block([],[])), local.sym, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return c

    def genInit(self,ast,sym,frame,haveInstance):
        """
            create assign stmt to init static attribute at main method
            create assign stmt to init instance attribute at <init> method
        """
        static_field = []
        instance_field = []
        for x in self.initAttribute:
            if x['kind'] == "static": static_field += [x]
            elif x['cname'] == self.className: instance_field += [x]
        if haveInstance:
            for x in instance_field: 
                if x['value']:
                    self.visit(Assign(FieldAccess(SelfLiteral(),Id(x['name'])),x['value']),SubBody(frame,sym))
                else:
                    self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
                    self.emit.printout(self.emit.emitNEWARRAY(x['type'].size,x['type'].eleType,0,frame))
                    self.emit.printout(self.emit.emitPUTFIELD(self.className+'/'+x['name'],x['type'],frame))
        else:
            end_label = frame.getNewLabel()
            self.emit.printout(self.emit.emitGETSTATIC(self.className+'/'+"initStaticVar",IntType(),frame))
            self.emit.printout(self.emit.emitPUSHICONST(1121,frame))
            self.emit.printout(self.emit.emitREOP("!=",IntType(),frame))
            self.emit.printout(self.emit.emitIFFALSE(end_label,frame))
            self.emit.printout(self.emit.emitPUSHICONST(1121,frame))
            self.emit.printout(self.emit.emitPUTSTATIC(self.className+'/'+"initStaticVar",IntType(),frame))
            for x in static_field:    
                if x['value']:
                    self.visit(Assign(FieldAccess(Id(x['cname']),Id(x['name'])),x['value']),SubBody(frame,sym))
                else:
                    self.emit.printout(self.emit.emitNEWARRAY(x['type'].size,x['type'].eleType,0,frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(x['cname']+'/'+x['name'],x['type'],frame))
            self.emit.printout(self.emit.emitLABEL(end_label,frame))    

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType

        intype = [ArrayType(0,StringType())] if isMain else list(map(lambda x: x.varType,consdecl.param))
        mtype = MType(intype, returnType)

        isStatic = (type(consdecl.kind) is Static) or isMain

        self.emit.printout(self.emit.emitMETHOD(consdecl.name.name, mtype, isStatic,frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if type(consdecl.kind) is Instance:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.className)), frame.getStartLabel(), frame.getEndLabel(),frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0,StringType()), frame.getStartLabel(), frame.getEndLabel(),frame))
        else:
            # local = reduce(lambda env,ele: SubBody(frame,[self.visit(ele,env)]+env.sym),consdecl.param,SubBody(frame,[]))
            local = SubBody(frame,[])
            for decl in consdecl.param:
                name = decl.variable.name
                typ = decl.varType
                idx = frame.getNewIndex()
                # print declare
                self.emit.printout(self.emit.emitVAR(idx,name,typ,frame.getStartLabel(),frame.getEndLabel(),frame))
                local = SubBody(frame,[Symbol(name,typ,Index(idx))]+local.sym)
            if len(local.sym) != 0: glenv = local.sym + glenv
        
        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
            listParent = self.findListParent(self.className)
            if len(listParent) == 1:
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            else:
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame,ClassType(Id(listParent[1])),MType([],VoidType())))
            self.genInit(consdecl,glenv,frame,True)
        if isMain:
            self.genInit(consdecl,glenv,frame,False)

        self.visit(body,SubBody(frame, glenv))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(returnType, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)

    def visitAttributeDecl(self,ast,o):
        # get parameter for attribute decl
        if type(ast.decl) is VarDecl:
            name = ast.decl.variable.name
            typ = ast.decl.varType
            value = ast.decl.varInit
            isFinal = False
        else:
            name = ast.decl.constant.name
            typ = ast.decl.constType
            value = ast.decl.value
            isFinal = True
        # call declare
        self.emit.printout(self.emit.emitATTRIBUTE(name, typ, isFinal, value, (type(ast.kind) is Static)))

    def visitVarDecl(self, ast, o):
        name = ast.variable.name
        typ = ast.varType
        idx = o.frame.getNewIndex()
        # print declare
        code = self.emit.emitVAR(idx,name,typ,o.frame.getStartLabel(),o.frame.getEndLabel(),o.frame)
        # assign init value
        if ast.varInit:
            initc, initt = self.visit(ast.varInit, Access(o.frame, o.sym, False))
            if type(initt) is ArrayType:
                if type(initt.eleType) is IntType and type(typ.eleType) is FloatType:
                    initc += self.change_IntArray_to_FloatArray(typ.size,Access(o.frame, o.sym, False))
            code += initc + self.emit.emitWRITEVAR(name, typ, idx, o.frame)
        elif type(typ) is ArrayType:
            code += self.emit.emitNEWARRAY(typ.size, typ.eleType, idx, o.frame)
            code += self.emit.emitWRITEVAR(name, typ, idx, o.frame)
        elif type(typ) is ClassType:
            code += self.emit.emitPUSHNULL(o.frame)
            code += self.emit.emitWRITEVAR(name, typ, idx, o.frame)
        self.emit.printout(code)
        return Symbol(name, typ, Index(idx))

    def visitConstDecl(self, ast, o):
        name = ast.constant.name
        typ = ast.constType
        idx = o.frame.getNewIndex()
        # code declare constant
        code = self.emit.emitVAR(idx,name,typ,o.frame.getStartLabel(),o.frame.getEndLabel(),o.frame)
        ec, et = self.visit(ast.value, Access(o.frame, o.sym, False))
        if type(et) is ArrayType:
                if type(et.eleType) is IntType and type(typ.eleType) is FloatType:
                    ec += self.change_IntArray_to_FloatArray(typ.size,Access(o.frame, o.sym, False))
        code += ec + self.emit.emitWRITEVAR(name, typ, idx, o.frame)
        self.emit.printout(code)
        return Symbol(name, typ, Index(idx))
    """
                STMT
        print out all code
    """
    def visitCallStmt(self, ast, o):
        frame = o.frame
        sym = []
        for x in o.sym:
            if ast.method.name == x.name: sym += [x]
        # get classname, check static?
        isStatic = False
        objc, objt = self.visit(ast.obj,Access(frame, o.sym, False))
        code = ""
        if objc is None: isStatic = True
        else: code = objc
        cname = objt.classname.name
        lexeme = cname + "/" + ast.method.name
        # get parameters
        in_ = (list(), list())
        for x in range(len(ast.param)):
            str1, typ1 = self.visit(ast.param[x], Access(frame, o.sym, False, True))
            in_ = (in_[0] + [str1], in_[1] + [typ1])
        # find ctype of method
        listParent = self.findListParent(cname)
        class_name = ""
        ctype_list = []
        for classname in listParent:
            for s in sym:
                if s.value.value == classname:
                    class_name = classname 
                    if self.matchType(in_[1],s.mtype.partype):
                        ctype_list += [s.mtype]
            if class_name != "": break
        ctype = self.findCtype(ctype_list,in_[1])
        # check type if correct
        for i in range(len(in_[0])):
            if type(in_[1][i]) is IntType and type(ctype.partype[i]) is FloatType:
                in_[0][i] += self.emit.emitI2F(frame)
            if type(in_[1][i]) is ArrayType:
                if type(in_[1][i].eleType) is IntType and type(ctype.partype[i].eleType) is FloatType:
                    in_[0][i] += self.change_IntArray_to_FloatArray(in_[1][i].size,o)
        # push to buffer
        for par in in_[0]: code += par
        if isStatic: code += self.emit.emitINVOKESTATIC(lexeme, ctype, frame)
        else: code += self.emit.emitINVOKEVIRTUAL(lexeme, ctype, frame)
        self.emit.printout(code)

    def visitAssign(self,ast,o):
        rhs, rhst = self.visit(ast.exp, Access(o.frame, o.sym, False))
        lhs, lhst = self.visit(ast.lhs, Access(o.frame, o.sym, True, rhs))
        if type(rhst) is None: self.emit.printout(rhs + lhs)
        elif lhst is None: self.emit.printout(lhs)
        else:
            if type(lhst) is FloatType and type(rhst) is IntType: rhs += self.emit.emitI2F(o.frame)
            if type(lhst) is ArrayType and type(rhst) is ArrayType:
                if type(rhst.eleType) is IntType and type(lhst.eleType) is FloatType:
                    rhs += self.change_IntArray_to_FloatArray(rhst.size,o)
            self.emit.printout(rhs + lhs)

    def visitIf(self, ast, o):
        # create condition check
        ec, et = self.visit(ast.expr, o)
        else_label = o.frame.getNewLabel()
        self.emit.printout(ec + self.emit.emitIFFALSE(else_label, o.frame))
        # create thenStmt
        if type(ast.thenStmt) is Block:
            o.frame.enterScope(False)
            self.emit.printout(self.emit.emitLABEL( o.frame.getStartLabel(), o.frame))
            self.visit(ast.thenStmt, o)
            self.emit.printout(self.emit.emitLABEL( o.frame.getEndLabel(), o.frame))
            o.frame.exitScope()
        else:
            self.visit(ast.thenStmt, o)
        # create elseStmt
        if ast.elseStmt:
            end_label = o.frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(end_label, o.frame))
            self.emit.printout(self.emit.emitLABEL(else_label, o.frame))
            if type(ast.elseStmt) is Block:
                o.frame.enterScope(False)
                self.emit.printout(self.emit.emitLABEL(
                    o.frame.getStartLabel(), o.frame))
                self.visit(ast.elseStmt, o)
                self.emit.printout(self.emit.emitLABEL(
                    o.frame.getEndLabel(), o.frame))
                o.frame.exitScope()
            else:
                self.visit(ast.elseStmt, o)
            self.emit.printout(self.emit.emitLABEL(end_label, o.frame))
        else:
            self.emit.printout(self.emit.emitLABEL(else_label, o.frame))    

    def visitFor(self, ast, o):
        # assign lhs to expr1
        begin_assign = Assign(ast.id,ast.expr1)
        self.visit(begin_assign,o)
        o.frame.enterLoop()
        # get head to return from continue
        head = o.frame.getNewLabel()
        con = o.frame.getContinueLabel()
        brk = o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(head, o.frame))
        # check if
        if ast.up: if_stmt = If(BinaryOp(">",ast.id,ast.expr2),Break())
        else: if_stmt = If(BinaryOp("<",ast.id,ast.expr2),Break())
        self.visit(if_stmt,o)
        # check if block, make new block
        if type(ast.loop) is Block:
            o.frame.enterScope(False)
            self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))
            self.visit(ast.loop, o)
            self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
            o.frame.exitScope()
        else: self.visit(ast.loop,o)
        # continue loop
        self.emit.printout(self.emit.emitLABEL(con, o.frame))
        if ast.up: op = "+"
        else: op = "-"
        # make update lhs of loop
        update_lhs = Assign(ast.id,BinaryOp(op,ast.id,IntLiteral(1)))
        self.visit(update_lhs,o)
        # jump to head to loop again
        self.emit.printout(self.emit.emitGOTO(head, o.frame))
        # break loop
        self.emit.printout(self.emit.emitLABEL(brk, o.frame))
        o.frame.exitLoop()

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(),o.frame))

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(),o.frame))

    def visitReturn(self, ast, o):
        ec, et = self.visit(ast.expr,Access(o.frame,o.sym,False))
        if type(et) is ArrayType:
            if type(et.eleType) is IntType and type(o.frame.returnType.eleType) is FloatType:
                ec += self.change_IntArray_to_FloatArray(o.frame.returnType.size, Access(o.frame, o.sym, False))
        self.emit.printout(ec)
        if type(et) is IntType and type(o.frame.returnType) is FloatType:
            self.emit.printout(self.emit.emitI2F(o.frame))
        self.emit.printout(self.emit.emitGOTO(1,o.frame))

    def visitBlock(self, ast, o):
        local = SubBody(o.frame, o.sym)
        for decl in ast.decl:
            local = SubBody(local.frame, [self.visit(decl, local)] + local.sym)
        list(map(lambda x: self.visit(x, local), ast.stmt))

    """
                EXP
        -> return code, type
    """
    def visitId(self,ast,o):
        sym = next(filter(lambda x: ast.name == x.name, o.sym), None)
        if sym is None: return None,ClassType(ast) # if this name is classname
        if o.isLeft:
            return self.emit.emitWRITEVAR(sym.name,sym.mtype,sym.value.value,o.frame),sym.mtype
        return self.emit.emitREADVAR(sym.name,sym.mtype,sym.value.value,o.frame),sym.mtype

    def visitBinaryOp(self, ast, o):
        e1c,e1t = self.visit(ast.left,Access(o.frame,o.sym,False))
        e2c,e2t = self.visit(ast.right,Access(o.frame,o.sym,False))
        op = ast.op
        if op == "^":
            cname = ClassType(Id("StringBuilder"))
            mtype = MType([],VoidType())
            stringBuilder = "java/lang/StringBuilder/"
            code = self.emit.emitNEW(cname,mtype.partype,o.frame)
            code += self.emit.emitDUP(o.frame)
            code += self.emit.emitINVOKESPECIAL(o.frame,cname,mtype)
            code += e1c
            code += self.emit.emitINVOKEVIRTUAL(stringBuilder + "append",MType([StringType()],cname),o.frame)
            code += e2c
            code += self.emit.emitINVOKEVIRTUAL(stringBuilder + "append",MType([StringType()],cname),o.frame)
            code += self.emit.emitINVOKEVIRTUAL(stringBuilder + "toString", MType([], StringType()), o.frame)
            retype = StringType()
        elif op == "\\":
            code = e1c + e2c + self.emit.emitDIV(o.frame)
            retype = IntType()
        elif op == "%":
            code = e1c + e2c + self.emit.emitMOD(o.frame)
            retype = IntType()
        elif op == "/":
            if type(e1t) is IntType: e1c += self.emit.emitI2F(o.frame)
            if type(e2t) is IntType: e2c += self.emit.emitI2F(o.frame)
            code = e1c + e2c + self.emit.emitMULOP('/',FloatType(),o.frame)
            retype = FloatType()
        elif op in ['+', '-', '*']:
            if type(e1t) is FloatType or type(e2t) is FloatType:
                retype = FloatType()
                if type(e1t) is IntType: e1c += self.emit.emitI2F(o.frame)
                if type(e2t) is IntType: e2c += self.emit.emitI2F(o.frame)
            else: retype = IntType()
            if op == "*": code = e1c + e2c + self.emit.emitMULOP('*',retype,o.frame)
            else: code = e1c + e2c + self.emit.emitADDOP(op,retype,o.frame)
        elif op == '&&':
            code = e1c + e2c + self.emit.emitANDOP(o.frame)
            retype = BoolType()
        elif op == '||':
            code = e1c + e2c + self.emit.emitOROP(o.frame)
            retype = BoolType() 
        else:
            if type(e1t) is FloatType or type(e2t) is FloatType:
                if type(e1t) is IntType:
                    e1c += self.emit.emitI2F(o.frame)
                    e1t = FloatType()
                if type(e2t) is IntType:
                    e2c += self.emit.emitI2F(o.frame)
                    e2t = FloatType()
            code = e1c + e2c + self.emit.emitREOP(op,e1t,o.frame)
            retype = BoolType()
        return code, retype

    def visitUnaryOp(self,ast,o):
        ec, et = self.visit(ast.body,Access(o.frame,o.sym,False))
        op = ast.op
        if op == '!': code = ec + self.emit.emitNOT(et,o.frame)
        else:
            if type(et) is FloatType: code = self.emit.emitPUSHFCONST(0.0,o.frame)
            else: code = self.emit.emitPUSHICONST(0,o.frame)
            code += ec + self.emit.emitADDOP(op,et,o.frame)
        return code, et

    def visitCallExpr(self, ast, o):
        frame = o.frame
        sym = []
        for x in o.sym:
            if ast.method.name == x.name: sym += [x]
        # get classname, check static?
        isStatic = False
        objc, objt = self.visit(ast.obj,Access(frame, o.sym, False))
        code = ""
        if objc is None: isStatic = True
        else: code = objc
        cname = objt.classname.name
        lexeme = cname + "/" + ast.method.name
        # get parameters
        in_ = (list(), list())
        for x in range(len(ast.param)):
            str1, typ1 = self.visit(ast.param[x], Access(frame, o.sym, False, True))
            in_ = (in_[0] + [str1], in_[1] + [typ1])
        # find ctype of method
        listParent = self.findListParent(cname)
        class_name = ""
        ctype_list = []
        for classname in listParent:
            for s in sym:
                if s.value.value == classname:
                    class_name = classname 
                    if self.matchType(in_[1],s.mtype.partype):
                        ctype_list += [s.mtype]
            if class_name != "": break
        ctype = self.findCtype(ctype_list,in_[1])
        # check type if correct
        for i in range(len(in_[0])):
            if type(in_[1][i]) is IntType and type(ctype.partype[i]) is FloatType:
                in_[0][i] += self.emit.emitI2F(frame)
            if type(in_[1][i]) is ArrayType:
                if type(in_[1][i].eleType) is IntType and type(ctype.partype[i].eleType) is FloatType:
                    in_[0][i] += self.change_IntArray_to_FloatArray(in_[1][i].size,o)
        # push to buffer
        for par in in_[0]: code += par
        if isStatic: code += self.emit.emitINVOKESTATIC(lexeme, ctype, frame)
        else: code += self.emit.emitINVOKEVIRTUAL(lexeme, ctype, frame)
        return code, ctype.rettype
    
    def visitNewExpr(self,ast,o):
        sym = next(filter(lambda x: ast.classname.name == x.value.value and x.name == "<init>", o.sym), None)

        param_type = sym.mtype.partype
        in_ = ("", list())
        for x in range(len(ast.param)):
            str1, typ1 = self.visit(ast.param[x], Access(o.frame, o.sym, False, True))
            if type(typ1) is IntType and type(param_type[x]) is FloatType:
                str1 += self.emit.emitI2F(o.frame)
                typ1 = FloatType()
            if type(typ1) is ArrayType:
                if type(typ1.eleType) is IntType and type(param_type[x].eleType) is FloatType:
                    str1 += self.change_IntArray_to_FloatArray(typ1.size,o)
                    typ1 = ArrayType(typ1.size,FloatType())
            in_ = (in_[0] + str1, in_[1].append(typ1))

        code = self.emit.emitNEW(ClassType(ast.classname), ast.param, o.frame)
        code += self.emit.emitDUP(o.frame)
        code += in_[0]
        code += self.emit.emitINVOKESPECIAL(o.frame, ClassType(ast.classname), MType(param_type, VoidType()))
        return code, ClassType(Id(ast.classname.name))

    def visitArrayCell(self, ast, o):
        namec, namet = self.visit(ast.arr, Access(o.frame, o.sym, False))
        idx,idxt = self.visit(ast.idx,o)
        if o.isLeft:
            return namec + idx + o.isFirst + self.emit.emitASTORE(namet.eleType, o.frame), None
        return namec + idx + self.emit.emitALOAD(namet.eleType,o.frame), namet.eleType

    def visitFieldAccess(self, ast, o):
        frame = o.frame
        sym = []
        for x in o.sym:
            if ast.fieldname.name == x.name: sym += [x]

        isStatic = False
        objc, objt = self.visit(ast.obj,Access(o.frame, o.sym, False))
        code = ""
        if objc is None: isStatic = True
        else: code = objc
        cname = objt.classname.name
        lexeme = cname + "/" + ast.fieldname.name

        ctype = None
        listParent = self.findListParent(cname)
        for classname in listParent:
            for s in sym:
                if s.value.value == classname:
                    ctype = s.mtype
                    break

        if isStatic:
            if o.isLeft: code = self.emit.emitPUTSTATIC(lexeme, ctype, frame)
            else: code = self.emit.emitGETSTATIC(lexeme, ctype, frame)
        else:
            if o.isLeft:
                code += o.isFirst + self.emit.emitPUTFIELD(lexeme, ctype, frame)
                ctype = None
            else: code += self.emit.emitGETFIELD(lexeme, ctype, frame)
        return code, ctype
    """
                LITERAL
        -> return code, type
    """
    def visitIntLiteral(self,ast,o):
        return self.emit.emitPUSHICONST(ast.value,o.frame),IntType()

    def visitFloatLiteral(self,ast,o):
        return self.emit.emitPUSHFCONST(str(ast.value),o.frame),FloatType()

    def visitStringLiteral(self,ast,o):
        return self.emit.emitPUSHCONST(ast.value,StringType(),o.frame),StringType()

    def visitBooleanLiteral(self,ast,o):
        if ast.value: code = self.emit.emitPUSHICONST("true",o.frame)
        else: code = self.emit.emitPUSHICONST("false",o.frame)
        return code,BoolType()

    def visitNullLiteral(self, ast, o):
        return self.emit.emitPUSHNULL(o.frame),None

    def visitSelfLiteral(self, ast, o):
        return self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, o.frame), ClassType(Id(self.className))

    def visitArrayLiteral(self, ast, o):
        res = []
        ret = None
        count = len(ast.value)
        for par in ast.value:
            ec, et = self.visit(par,Access(o.frame,o.sym,False))
            res += [ec]
            ret = et

        name = "clone_array_variable"
        typ = ArrayType(count, ret)
        idx = o.frame.getNewIndex()

        code = self.emit.emitVAR(idx,name,typ,o.frame.getStartLabel(),o.frame.getEndLabel(),o.frame)
        code += self.emit.emitNEWARRAY(count, ret, idx, o.frame)
        code += self.emit.emitWRITEVAR(name, typ, idx, o.frame)
        for i in range(count):
            code += self.emit.emitREADVAR(name,typ,idx,o.frame)
            code += self.emit.emitPUSHICONST(i,o.frame)
            code += res[i]
            code += self.emit.emitASTORE(ret,o.frame)
        code += self.emit.emitREADVAR(name,typ,idx,o.frame)
        return code,ArrayType(count,ret)

    def change_IntArray_to_FloatArray(self,size,o):
        idx_int = o.frame.getNewIndex()
        idx_float = o.frame.getNewIndex()
        code = self.emit.emitVAR(idx_int,"int_array_clone",ArrayType(size,IntType()),o.frame.getStartLabel(),o.frame.getEndLabel(),o.frame)
        code += self.emit.emitWRITEVAR("int_array_clone",ArrayType(size,IntType()),idx_int,o.frame)
        code += self.emit.emitVAR(idx_float,"float_array_clone",ArrayType(size,FloatType()),o.frame.getStartLabel(),o.frame.getEndLabel(),o.frame)
        code += self.emit.emitNEWARRAY(size, FloatType(), idx_float, o.frame)
        code += self.emit.emitWRITEVAR("float_array_clone", ArrayType(size,FloatType()), idx_float, o.frame)
        for i in range(size):
            code += self.emit.emitREADVAR("float_array_clone", ArrayType(size,FloatType()), idx_float, o.frame)
            code += self.emit.emitPUSHICONST(i, o.frame)
            code += self.emit.emitREADVAR("int_array_clone",ArrayType(size,IntType()),idx_int,o.frame)
            code += self.emit.emitPUSHICONST(i, o.frame)
            code += self.emit.emitALOAD(IntType(),o.frame)
            code += self.emit.emitI2F(o.frame)
            code += self.emit.emitASTORE(FloatType(),o.frame)
        code += self.emit.emitREADVAR("float_array_clone", ArrayType(size,FloatType()), idx_float, o.frame)
        return code




