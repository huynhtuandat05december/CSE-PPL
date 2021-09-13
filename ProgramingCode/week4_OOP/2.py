
class Exp:
    def eval():
        pass


class UnExp:
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


class BinExp():
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


class IntLit:
    def __init__(self, number):
        self.value = number

    def eval(self):
        return self.value

    def printPrefix(self):
        return str(self.value)


class FloatLit:
    def __init__(self, number):
        self.value = number

    def eval(self):
        return self.value

    def printPrefix(self):
        return str(self.value)
