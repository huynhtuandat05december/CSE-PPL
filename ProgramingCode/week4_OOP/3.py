
class Exp:
    def accept(self, visitor):
        return visitor.visit(self)


class UnExp(Exp):
    def __init__(self, operator, arg):
        self.operator = operator
        self.arg = arg

    def eval(self):
        if self.operator == '+':
            return self.arg.value
        if self.operator == '-':
            return -self.arg.value

    def printPrefix(self):
        return self.operator + '. '+self.arg.printPrefix()

    def printPostfix(self):
        return self.arg.printPrefix()+' '+self.operator + '.'


class BinExp(Exp):
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self):
        if self.operator == '*':
            return self.left.eval() * self.right.eval()
        if self.operator == '/':
            return self.left.eval() / self.right.eval()
        if self.operator == '+':
            return self.left.eval() + self.right.eval()
        if self.operator == '-':
            return self.left.eval() - self.right.eval()

    def printPrefix(self):
        return self.operator+' '+self.left.printPrefix()+' '+self.right.printPrefix()

    def printPostfix(self):
        return self.left.printPostfix()+' '+self.right.printPostfix()+' '+self.operator


class IntLit(Exp):
    def __init__(self, number):
        self.value = number

    def eval(self):
        return self.value

    def printPrefix(self):
        return str(self.value)

    def printPostfix(self):
        return str(self.value)


class FloatLit(Exp):
    def __init__(self, number):
        self.value = number

    def eval(self):
        return self.value

    def printPrefix(self):
        return str(self.value)

    def printPostfix(self):
        return str(self.value)


class Visitor:
    def visit(self, exp):
        pass


class Eval(Visitor):
    def visit(self, exp):
        return exp.eval()


class PrintPrefix(Visitor):
    def visit(self, exp):
        return exp.printPrefix()


class PrintPostfix(Visitor):
    def visit(self, exp):
        return exp.printPostfix()
