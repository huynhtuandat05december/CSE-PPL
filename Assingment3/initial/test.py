from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from os import truncate
from typing import List, Tuple
from main.csel.utils.AST import *
from main.csel.utils.Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta


class NumberType(Prim):
    def __str__(self) -> str:
        return "NumberType"


class StringType(Prim):
    def __str__(self) -> str:
        return "StringType"


class BoolType(Prim):
    def __str__(self) -> str:
        return "BoolType"


class VoidType(Type):
    def __str__(self) -> str:
        return "VoidType"


class Unknown(Type):
    def __str__(self) -> str:
        return "Unknown !!!"


class JSONType(Type):
    def __str__(self) -> str:
        return "JSONType"


class ValidType(Type):
    pass


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type

    def __str__(self) -> str:
        return printlist(lst=self.dimen, start="[",) + " Of " + str(self.eletype)


@dataclass
class FType:
    ptype: List[Type]
    rtype: Type

    def __str__(self) -> str:
        if self.ptype != None:
            return "--> "+str(self.rtype).ljust(20) + printlist(lst=self.ptype, start="Param : [")
        else:
            return "--> "+str(self.rtype).ljust(20) + "Param : None"


@dataclass
class Symbol:
    name: str
    mtype: Type

    @staticmethod
    def VarDeclSymbol(ast: VarDecl, inittyp):
        # Let var : Type = Init
        # Let arr[dimen] : Type = Init

        id = ast.variable.name
        # Get type
        if str(ast.typ) == "NoneType":
            vtyp = Unknown()
        elif str(ast.typ) == "StringType":
            vtyp = StringType()
        elif str(ast.typ) == "NumberType":
            vtyp = NumberType()
        elif str(ast.typ) == "JSONType":
            vtyp = JSONType()
        else:
            vtyp = BoolType()

        # Get dimen
        if ast.varDimen != None:
            dimen = []
            for d in ast.varDimen:
                if type(d) is not NumberLiteral:
                    raise TypeMismatchInStatement(ast)
                else:
                    dimen += [int(d.value)]
            vtyp = ArrayType(dimen, vtyp)

        # Compare Init type
        if inittyp != None:
            if type(inittyp) is FType:
                raise TypeCannotBeInferred(ast)
            elif type(vtyp) is Unknown:
                if type(inittyp) is Unknown or type(inittyp) is ArrayType:
                    raise TypeCannotBeInferred(ast)
                else:
                    vtyp = inittyp
            elif type(inittyp) is not Unknown:
                if type(vtyp) != type(inittyp):
                    raise TypeMismatchInStatement(ast)
                elif type(vtyp) is ArrayType:
                    if vtyp.dimen != inittyp.dimen:
                        raise TypeMismatchInStatement(ast)
                    if type(vtyp.eletype) is Unknown:
                        if type(inittyp.eletype) is Unknown:
                            raise TypeCannotBeInferred(ast)
                        else:
                            vtyp.eletype = inittyp.eletype
                    elif type(vtyp.eletype) != type(inittyp.eletype):
                        raise TypeMismatchInStatement(ast)

        return Symbol(id, vtyp)

    @staticmethod
    def ConstDeclSymbol(ast: ConstDecl, inittyp):
        id = ast.constant.name
        # Get type
        if str(ast.typ) == "NoneType":
            ctyp = Unknown()
        elif str(ast.typ) == "StringType":
            ctyp = StringType()
        elif str(ast.typ) == "NumberType":
            ctyp = NumberType()
        elif str(ast.typ) == "JSONType":
            ctyp = JSONType()
        else:
            ctyp = BoolType()

        # Get dimen
        if ast.constDimen != None:
            dimen = []
            for d in ast.constDimen:
                if type(d) is not NumberLiteral:
                    raise TypeMismatchInStatement(ast)
                else:
                    dimen += [int(d.value)]
            ctyp = ArrayType(dimen, ctyp)

        # Compare Init type
        if inittyp != None:
            if type(inittyp) is FType:
                raise TypeCannotBeInferred(ast)
            elif type(ctyp) is Unknown:
                if type(inittyp) is Unknown or type(inittyp) is ArrayType:
                    raise TypeCannotBeInferred(ast)
                else:
                    ctyp = inittyp
            elif type(inittyp) is not Unknown:
                if type(ctyp) != type(inittyp):
                    raise TypeMismatchInStatement(ast)
                elif type(ctyp) is ArrayType:
                    if ctyp.dimen != inittyp.dimen:
                        raise TypeMismatchInStatement(ast)
                    if type(ctyp.eletype) is Unknown:
                        if type(inittyp.eletype) is Unknown:
                            raise TypeCannotBeInferred(ast)
                        else:
                            ctyp.eletype = inittyp.eletype
                    elif (type(inittyp.eletype) is not Unknown) and (type(ctyp.eletype) != type(inittyp.eletype)):
                        raise TypeMismatchInStatement(ast)

        return Symbol(id, ctyp)

    @staticmethod
    def FuncDeclSymbol(name, typ):
        return Symbol(name, typ)

    def __str__(self) -> str:
        return self.name.ljust(20) + str(self.mtype)


# Function :

class Check:
    @ staticmethod
    def SetType(name, typ, envi):
        if type(envi) is list:
            return Check.SetTypeInScope(name, typ, envi)
        else:
            inscope, outscope = envi
            if Check.SetTypeInScope(name, typ, inscope) == False:
                return Check.SetType(name, typ, outscope)
            else:
                return True

    @ staticmethod
    def SetTypeInScope(name, typ, scope: List[Symbol]):
        for sb in scope:
            if sb.name == name:
                if type(sb.mtype) is ArrayType:
                    sb.mtype.eletype = typ
                else:
                    sb.mtype = typ
                return True
        return False

    @ staticmethod
    def GetType(name, envi):
        if type(envi) is list:
            return Check.GetTypeInScope(name, envi)
        else:
            inscope, outscope = envi
            if Check.GetTypeInScope(name, inscope) == None:
                return Check.GetType(name, outscope)
            else:
                return Check.GetTypeInScope(name, inscope)

    @ staticmethod
    def GetTypeInScope(name, scope: List[Symbol]):
        for sb in scope:
            if sb.name == name:
                return sb.mtype
        return None


class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("read", FType([], StringType())),
            Symbol("print", FType([StringType()], VoidType())),
            Symbol("printSLn", FType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

# # #       Visit Program       # # #
    def visitProgram(self, ast: Program, global_envi):
        # print("\n** ---------------- Start ---------------- **\n")

        # print(ast)

        # print(printlist(lst=global_envi, start="Global Enviroment:\n\t",
        #                 sepa="\n\t", ending="\n\t\t ~~~~~~~~~~~~~~~ \n\n"))

        haveEntryPoint = False
        for decl in ast.decl:
            if type(decl) is VarDecl:
                global_envi += [self.visit(decl, (Variable(), global_envi))]
            elif type(decl) is ConstDecl:
                global_envi += [self.visit(decl, (Constant(), global_envi))]
            else:  # FuncDecl
                funcSymbol = self.visit(decl, global_envi)
                if funcSymbol.name == "main":
                    haveEntryPoint = True
                global_envi += [funcSymbol]
            # print(printlist(lst=global_envi, start="Global Enviroment:\n\t",
            #                 sepa="\n\t", ending="\n\t\t ~~~~~~~~~~~~~~~ \n\n"))

        # print("\n** ----------------  End  ---------------- **\n\n\n")

        if not haveEntryPoint:
            raise NoEntryPoint()


# # #       Visit Declared      # # #


    def visitVarDecl(self, ast: VarDecl, param):
        kind, envi = param
        # Get init type
        inittyp = None
        if ast.varInit != None:
            if type(ast.varInit) is Id:
                inittyp = self.visit(ast.varInit, (Identifier(), envi))
            else:
                try:
                    inittyp = self.visit(ast.varInit, envi)
                except TypeCannotBeInferred:
                    raise TypeCannotBeInferred(ast)

        # Create symbol
        symbol = Symbol.VarDeclSymbol(ast, inittyp)

        # Get local envi
        if type(envi) is list:
            localEnvi = envi
        else:
            localEnvi = envi[0]

        # Check redeclared
        for sb in localEnvi:
            if sb.name == symbol.name:
                raise Redeclared(kind, symbol.name)

        # If init is Id and first use
        if type(inittyp) is Unknown:
            Check.SetType(ast.varInit.name, symbol.mtype, envi)

        return symbol

    def visitConstDecl(self, ast: ConstDecl, param):
        kind, envi = param

        # Get init type
        inittyp = None
        if type(ast.constInit) is Id:
            inittyp = self.visit(ast.constInit, (Identifier(), envi))
        else:
            try:
                inittyp = self.visit(ast.constInit, envi)
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)

        # Create symbol
        symbol = Symbol.ConstDeclSymbol(ast, inittyp)

        # Get local envi
        if type(envi) is list:
            localEnvi = envi
        else:
            localEnvi = envi[0]

        # Check redeclared
        for sb in localEnvi:
            if sb.name == symbol.name:
                raise Redeclared(kind, symbol.name)

        # If init is Id and first use
        if type(inittyp) is Unknown:
            Check.SetType(ast.constInit.name, symbol.mtype, envi)

        return symbol

    def visitFuncDecl(self, ast: FuncDecl, envi: List[Symbol]):
        # Check redeclared
        funcName = ast.name.name
        for symbol in envi:
            if symbol.name == funcName:
                raise Redeclared(Function(), funcName)

        local_envi = []
        for param in ast.param:
            local_envi += [self.visit(param, (Parameter(), local_envi))]

        nParam = len(local_envi)

        rtype = VoidType()

        # print(printlist(lst=local_envi, start="\tLocal Enviroment: " + funcName + "\n\t\t",
        #                 sepa="\n\t\t", ending="\n\t\t ~~~~~~~~~~~~~~~ \n\n"))

        rtype = None
        for stmt in ast.body:
            if type(stmt) is VarDecl:
                local_envi += [self.visit(stmt,
                                          (Variable(), (local_envi, envi)))]
            elif type(stmt) is ConstDecl:
                local_envi += [self.visit(stmt,
                                          (Constant(), (local_envi, envi)))]
            else:
                rtype = self.visit(stmt, (local_envi, envi))

            # print(printlist(lst=local_envi, start="\tLocal Enviroment: " + funcName + "\n\t\t",
            #                 sepa="\n\t\t", ending="\n\t\t ~~~~~~~~~~~~~~~ \n\n"))

            # if rtype != None:
            #     break

        params = local_envi[:nParam]
        ptype = [sb.mtype for sb in params]

        return Symbol.FuncDeclSymbol(funcName, FType(ptype, rtype))

# # #         Visit Exp         # # #

    def visitBinaryOp(self, ast: BinaryOp, param):
        if type(ast.left) is Id:
            op1 = self.visit(ast.left, (Identifier(), param))
        else:
            op1 = self.visit(ast.left, param)
        if type(ast.right) is Id:
            op2 = self.visit(ast.right, (Identifier(), param))
        else:
            op2 = self.visit(ast.right, param)

        op = ast.op

        if op in ["&&", "||"]:
            rtype = BoolType()
            if type(op1) is Unknown:  # -> Id
                op1 = BoolType()
                Check.SetType(ast.left.name, BoolType(), param)
            if type(op2) is Unknown:  # -> Id
                op2 = BoolType()
                Check.SetType(ast.right.name, BoolType(), param)
            if not (type(op1) is BoolType and type(op2) is BoolType):
                raise TypeMismatchInExpression(ast)

        elif op in ["-", "+", "*", "%", "/"]:
            rtype = NumberType()
            if type(op1) is Unknown:  # -> Id
                op1 = NumberType()
                Check.SetType(ast.left.name, NumberType(), param)
            if type(op2) is Unknown:  # -> Id
                op2 = NumberType()
                Check.SetType(ast.right.name, NumberType(), param)
            if not (type(op1) is NumberType and type(op2) is NumberType):
                raise TypeMismatchInExpression(ast)

        elif op in ["+.", "==."]:
            if op == "+.":
                rtype = StringType()
            else:
                rtype = BoolType()
            if type(op1) is Unknown:  # -> Id
                op1 = StringType()
                Check.SetType(ast.left.name, StringType(), param)
            if type(op2) is Unknown:  # -> Id
                op2 = StringType()
                Check.SetType(ast.right.name, StringType(), param)
            if not (type(op1) is StringType and type(op2) is StringType):
                raise TypeMismatchInExpression(ast)

        elif op in ["==", "!=", "<", "<=", ">", ">="]:
            rtype = BoolType()
            if type(op1) is Unknown:  # -> Id
                op1 = NumberType()
                Check.SetType(ast.left.name, NumberType(), param)
            if type(op2) is Unknown:  # -> Id
                op2 = NumberType()
                Check.SetType(ast.right.name, NumberType(), param)
            if not (type(op1) is NumberType and type(op2) is NumberType):
                raise TypeMismatchInExpression(ast)

        return rtype

    def visitUnaryOp(self, ast: UnaryOp, param):
        op = ast.op
        if type(ast.body) is Id:
            operand = self.visit(ast.body, (Identifier(), param))
        else:
            operand = self.visit(ast.body, param)

        if op == "-":
            rtype = NumberType()
            if type(operand) is Unknown:  # -> Id
                operand = NumberType()
                Check.SetType(ast.body.name, NumberType(), param)
            if type(operand) is not NumberType:
                raise TypeMismatchInExpression(ast)

        elif op == "!":
            rtype = BoolType()
            if type(operand) is Unknown:  # -> Id
                operand = BoolType()
                Check.SetType(ast.body.name, BoolType(), param)
            if type(operand) is not BoolType:
                raise TypeMismatchInExpression(ast)

        return rtype

    def visitCallExpr(self, ast: CallExpr, param):
        functype = self.visit(ast.method, (Function(), param))
        if type(functype) is not FType:
            raise TypeMismatchInExpression(ast)

        if len(ast.param) != len(functype.ptype):
            raise TypeMismatchInExpression(ast)

        for i in range(len(ast.param)):
            # Get param type
            if type(ast.param[i]) is Id:
                paramtype = self.visit(ast.param[i], (Identifier(), param))
            else:
                paramtype = self.visit(ast.param[i], param)

            # paramtype = Unknown
            if type(paramtype) is Unknown:
                if type(functype.ptype[i]) is Unknown:
                    # throw out and catch again
                    raise TypeCannotBeInferred(ast)
                else:
                    Check.SetType(ast.param[i].name, functype.ptype[i], param)
            # function.ptype[i] = Unknown
            elif type(functype.ptype[i]) is Unknown:
                functype.ptype[i] = paramtype
            # paramtype != function.ptype[i]
            elif type(paramtype) != type(functype.ptype[i]):
                raise TypeMismatchInExpression(ast)
            # Check for ArrayType
            elif type(paramtype) is ArrayType:
                if paramtype.dimen != functype.ptype[i].dimen:
                    raise TypeMismatchInExpression(ast)
                if type(functype.ptype[i].eletype) is Unknown:
                    if type(paramtype.eletype) is Unknown:
                        # throw out and catch again
                        raise TypeCannotBeInferred(ast)
                    else:
                        functype.ptype[i].eletype = paramtype.eletype
                elif type(paramtype.eletype) != type(functype.ptype[i].eletype):
                    raise TypeMismatchInExpression(ast)

        return functype.rtype

    def visitId(self, ast: Id, param):
        kind, envi = param
        idtype = Check.GetType(ast.name, envi)
        if idtype != None:
            return idtype
        else:
            raise Undeclared(kind, ast.name)

    def visitArrayAccess(self, ast: ArrayAccess, param):
        if type(ast.arr) is Id:
            arr = self.visit(ast.arr, (Identifier(), param))
        else:
            arr = self.visit(ast.arr, param)

        if type(arr) is ValidType:
            for idx in ast.idx:
                if type(idx) is Id:
                    idxtype = self.visit(idx, (Identifier(), param))
                else:
                    idxtype = self.visit(idx, param)
                if (type(idxtype) is not NumberType) and (type(idxtype) is not ValidType):
                    raise TypeMismatchInExpression(ast)
            return ValidType()
        else:
            if type(arr) is not ArrayType:
                raise TypeMismatchInExpression(ast)

            dimen = arr.dimen
            if len(ast.idx) > len(dimen):
                raise TypeMismatchInExpression(ast)

            for idx in ast.idx:
                if type(idx) is Id:
                    idxtype = self.visit(idx, (Identifier(), param))
                else:
                    idxtype = self.visit(idx, param)
                if (type(idxtype) is not NumberType) and (type(idxtype) is not ValidType):
                    raise TypeMismatchInExpression(ast)
                dimen = dimen[1:]

            if dimen == []:
                return arr.eletype
            else:
                return ArrayType(dimen, arr.eletype)

    def visitJSONAccess(self, ast: JSONAccess, param):
        json = self.visit(ast.json, param)
        if (type(json) is not JSONType) and (type(json) is not ValidType):
            raise TypeMismatchInExpression(ast)

        for idx in ast.idx:
            if type(idx) is Id:
                idxtype = self.visit(idx, (Identifier(), param))
            else:
                idxtype = self.visit(idx, param)
            if (type(idxtype) is not StringType) and (type(idxtype) is not ValidType):
                raise TypeMismatchInExpression(ast)

        return ValidType()

# # #         Visit Stmt        # # #

    def visitAssign(self, ast: Assign, param):
        if type(ast.lhs) is Id:
            lhstype = self.visit(ast.lhs, (Identifier(), param))
            if type(ast.rhs) is Id:
                rhstype = self.visit(ast.rhs, (Identifier(), param))
            else:
                try:
                    rhstype = self.visit(ast.rhs, param)
                except TypeCannotBeInferred:
                    raise TypeCannotBeInferred(ast)
            if type(lhstype) is Unknown and type(rhstype) is Unknown:
                raise TypeCannotBeInferred(ast)
            elif type(lhstype) is Unknown:
                if type(rhstype) is ArrayType:
                    raise TypeCannotBeInferred(ast)
                lhstype = rhstype
                Check.SetType(ast.lhs.name, rhstype, param)
            elif type(rhstype) is Unknown:
                if type(lhstype) is ArrayType:
                    raise TypeCannotBeInferred(ast)
                rhstype = lhstype
                Check.SetType(ast.rhs.name, lhstype, param)
            elif type(lhstype) != type(rhstype):
                raise TypeMismatchInStatement(ast)
            # Assign array = array
            elif type(lhstype) is ArrayType:
                if lhstype.dimen != rhstype.dimen:
                    raise TypeMismatchInStatement(ast)
                if type(lhstype.eletype) is Unknown:
                    if type(rhstype.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    else:
                        lhstype = rhstype
                        Check.SetType(ast.lhs.name, rhstype.eletype, param)
                elif type(rhstype.eletype) is Unknown:
                    rhstype = lhstype
                    Check.SetType(ast.rhs.name, lhstype.eletype, param)
                elif type(lhstype.eletype) != type(rhstype.eletype):
                    raise TypeMismatchInStatement(ast)

            if type(lhstype) is VoidType or type(lhstype) is FType:
                raise TypeMismatchInStatement(ast)

        elif type(ast.lhs) is ArrayAccess:
            lhstype = self.visit(ast.lhs, param)
            if type(ast.rhs) is Id:
                rhstype = self.visit(ast.rhs, (Identifier(), param))
            else:
                try:
                    rhstype = self.visit(ast.rhs, param)
                except TypeCannotBeInferred:
                    raise TypeCannotBeInferred(ast)
            if type(lhstype) is Unknown:
                if type(rhstype) is Unknown:
                    raise TypeCannotBeInferred(ast)
                elif type(rhstype) is ArrayType:
                    raise TypeMismatchInStatement(ast)
                else:
                    Check.SetType(ast.lhs.arr.name, rhstype, param)
            elif type(lhstype) != type(rhstype):
                raise TypeMismatchInStatement(ast)
            elif type(lhstype) is ArrayType:
                if lhstype.dimen != rhstype.dimen:
                    raise TypeMismatchInStatement(ast)
                elif type(lhstype.eletype) is Unknown:
                    if type(rhstype.eletype) is Unknown:
                        raise TypeCannotBeInferred(ast)
                    else:
                        Check.SetType(ast.lhs.arr.name, rhstype.eletype, param)
                elif type(rhstype.eletype) is Unknown:
                    Check.SetType(ast.rhs.arr.name, lhstype.eletype, param)

        elif type(ast.lhs) is JSONAccess:
            pass

        return None

    def visitIf(self, ast: If, param):
        rtype = None
        for ifstmt in ast.ifthenStmt:
            condition = ifstmt[0]
            if type(condition) is Id:
                conditiontype = self.visit(condition, (Identifier(), param))
            else:
                try:
                    conditiontype = self.visit(condition, param)
                except TypeCannotBeInferred:
                    raise TypeCannotBeInferred(ast)
            if type(conditiontype) is Unknown:
                conditiontype = BoolType()
                Check.SetType(condition.name, BoolType(), param)
            elif type(conditiontype) is not BoolType:
                raise TypeMismatchInStatement(ast)

            local_envi = []
            rtype = None
            for stmt in ifstmt[1]:
                if type(stmt) is VarDecl:
                    local_envi += [self.visit(stmt,
                                              (Variable(), (local_envi, param)))]
                elif type(stmt) is ConstDecl:
                    local_envi += [self.visit(stmt,
                                              (Constant(), (local_envi, param)))]
                else:
                    rtype = self.visit(stmt, (local_envi, param))
                if rtype != None:
                    break

        if ast.elseStmt != None:
            local_envi = []
            for stmt in ast.elseStmt:
                if type(stmt) is VarDecl:
                    local_envi += [self.visit(stmt,
                                              (Variable(), (local_envi, param)))]
                elif type(stmt) is ConstDecl:
                    local_envi += [self.visit(stmt,
                                              (Constant(), (local_envi, param)))]
                else:
                    rtype = self.visit(stmt, (local_envi, param))
                if rtype != None:
                    break

        return rtype

    def visitForIn(self, ast: ForIn, param):
        rtype = None
        arr = ast.expr
        if type(arr) is Id:
            arrtype = self.visit(arr, (Identifier(), param))
        else:
            try:
                arrtype = self.visit(arr, param)
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)
        if type(arrtype) is not ArrayType:
            raise TypeMismatchInStatement(ast)

        if type(arrtype.eletype) is Unknown:
            raise TypeCannotBeInferred(ast)

        if len(arrtype.dimen) == 1:
            itype = arrtype.eletype
        else:
            itype = ArrayType(arrtype.dimen[1:], arrtype.eletype)
        local_envi = [Symbol(ast.idx1.name, itype)]

        for stmt in ast.body:
            if type(stmt) is VarDecl:
                local_envi += [self.visit(stmt,
                                          (Variable(), (local_envi, param)))]
            elif type(stmt) is ConstDecl:
                local_envi += [self.visit(stmt,
                                          (Constant(), (local_envi, param)))]
            else:
                rtype = self.visit(stmt, (local_envi, param))
            if rtype != None:
                break

        return rtype

    def visitForOf(self, ast: ForOf, param):
        rtype = None
        json = ast.expr
        if type(json) is Id:
            jsontype = self.visit(json, (Identifier(), param))
        else:
            try:
                jsontype = self.visit(json, param)
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)
        if type(jsontype) is not JSONType:
            raise TypeMismatchInStatement(ast)

        local_envi = [Symbol(ast.idx1, ValidType())]
        for stmt in ast.body:
            if type(stmt) is VarDecl:
                local_envi += [self.visit(stmt,
                                          (Variable(), (local_envi, param)))]
            elif type(stmt) is ConstDecl:
                local_envi += [self.visit(stmt,
                                          (Constant(), (local_envi, param)))]
            else:
                rtype = self.visit(stmt, (local_envi, param))
            if rtype != None:
                break

        return rtype

    def visitContinue(self, ast: Continue, param):
        return None

    def visitBreak(self, ast: Break, param):
        return None

    def visitReturn(self, ast: Return, param):
        rtype = None
        if ast.expr == None:
            rtype = VoidType()
        else:
            if type(ast.expr) is Id:
                rtype = self.visit(ast.expr, (Identifier(), param))
            else:
                try:
                    rtype = self.visit(ast.expr, param)
                except TypeCannotBeInferred:
                    raise TypeCannotBeInferred(ast)

        if type(rtype) is Unknown:
            raise TypeCannotBeInferred(ast)

        if type(rtype) is ArrayType:
            if type(rtype.eletype) is Unknown:
                raise TypeCannotBeInferred(ast)

        return rtype

    def visitWhile(self, ast: While, param):
        condition = ast.exp
        if type(condition) is Id:
            conditiontype = self.visit(condition, (Identifier(), param))
        else:
            try:
                conditiontype = self.visit(condition, param)
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)

        if type(conditiontype) is Unknown:
            conditiontype = BoolType()
            Check.SetType(condition.name, BoolType(), param)
        elif type(conditiontype) is not BoolType:
            raise TypeMismatchInStatement(ast)

        local_envi = []
        rtype = None
        for stmt in ast.sl:
            if type(stmt) is VarDecl:
                local_envi += [self.visit(stmt,
                                          (Variable(), (local_envi, param)))]
            elif type(stmt) is ConstDecl:
                local_envi += [self.visit(stmt,
                                          (Constant(), (local_envi, param)))]
            else:
                rtype = self.visit(stmt, (local_envi, param))
            if rtype != None:
                break

        return rtype

    def visitCallStmt(self, ast: CallStmt, param):
        functype = self.visit(ast.method, (Function(), param))
        if type(functype) is not FType:
            raise TypeMismatchInExpression(ast)

        if type(functype.rtype) is not VoidType:
            raise TypeMismatchInStatement(ast)

        if len(ast.param) != len(functype.ptype):
            raise TypeMismatchInExpression(ast)

        for i in range(len(ast.param)):
            # Get param type
            if type(ast.param[i]) is Id:
                paramtype = self.visit(ast.param[i], (Identifier(), param))
            else:
                try:
                    paramtype = self.visit(ast.param[i], param)
                except TypeCannotBeInferred:
                    raise TypeCannotBeInferred(ast)

            # paramtype = Unknown
            if type(paramtype) is Unknown:
                if type(functype.ptype[i]) is Unknown:
                    # throw out and catch again
                    raise TypeCannotBeInferred(ast)
                else:
                    Check.SetType(ast.param[i].name, functype.ptype[i], param)
            # function.ptype[i] = Unknown
            elif type(functype.ptype[i]) is Unknown:
                functype.ptype[i] = paramtype
            # paramtype != function.ptype[i]
            elif type(paramtype) != type(functype.ptype[i]):
                raise TypeMismatchInExpression(ast)
            # Check for ArrayType
            elif type(paramtype) is ArrayType:
                if paramtype.dimen != functype.ptype[i].dimen:
                    raise TypeMismatchInExpression(ast)
                if type(functype.ptype[i].eletype) is Unknown:
                    if type(paramtype.eletype) is Unknown:
                        # throw out and catch again
                        raise TypeCannotBeInferred(ast)
                    else:
                        functype.ptype[i].eletype = paramtype.eletype
                elif type(paramtype.eletype) != type(functype.ptype[i].eletype):
                    raise TypeMismatchInExpression(ast)

        return None

# # #       Visit Literal       # # #

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    # Let x = [ [ 1 , 2] , [ 4 , 6 ] ] => ArrayType( [2,2] , Num )
    def visitArrayLiteral(self, ast, param):
        dimen = []
        dimen += [len(ast.value)]
        if dimen[0] != 0:
            typ = self.visit(ast.value[0], param)
            for lit in ast.value:
                littyp = self.visit(lit, param)
                if type(littyp) != type(typ):
                    raise InvalidArrayLiteral(ast)
                if type(littyp) is ArrayType and littyp.dimen != typ.dimen:
                    raise InvalidArrayLiteral(ast)
            if type(typ) is ArrayType:
                dimen += typ.dimen
                typ = typ.eletype
        else:
            typ = Unknown()
        return ArrayType(dimen, typ)

    def visitJSONLiteral(self, ast: JSONLiteral, param):
        return JSONType()
