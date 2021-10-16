import unittest
from main.bkool.utils.AST import *
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"), [])]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_2(self):
        """More complex program"""
        input = """class main {
            static int numOfShape=5;
        }"""
        expect = str(Program([ClassDecl(Id("main"), [AttributeDecl(
            Static(), VarDecl(Id("numOfShape"), IntType(), IntLiteral(5)))])]))

        self.assertTrue(TestAST.test(input, expect, 301))

    def test_3(self):
        """More complex program"""
        input = """class main {
            static final int numOfShape = 0;
            final int immuAttribute = 0;
        }"""
        expect = str(Program([ClassDecl(Id("main"), [AttributeDecl(Static(), ConstDecl(Id("numOfShape"), IntType(), IntLiteral(
            0))), AttributeDecl(Instance(), ConstDecl(Id("immuAttribute"), IntType(), IntLiteral(0)))])]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_4(self):
        """More complex program"""
        input = """class Ex {
            int my1Var;
        }"""
        expect = str(Program([ClassDecl(Id("Ex"), [AttributeDecl(
            Instance(), VarDecl(Id("my1Var"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_5(self):
        """Miss ) int main( {}"""
        input = """class ABC extends DEF{ }"""
        expect = str(Program([ClassDecl(Id("ABC"), [], Id("DEF"))]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_6(self):
        """Test Complex Program """
        input = '''
        class Example1 {
            int factorial(int n){
                if n == 0 then return 1; else return n * this.factorial(n - 1);
            }
        }
            '''
        expect = str(Program([ClassDecl(Id("Example1"), [MethodDecl(Instance(), Id("factorial"), [VarDecl(Id("n"), IntType())], IntType(), Block([], [If(BinaryOp(
            "==", Id("n"), IntLiteral(0)), Return(IntLiteral(1)), Return(BinaryOp("*", Id("n"), CallExpr(SelfLiteral(), Id("factorial"), [BinaryOp("-", Id("n"), IntLiteral(1))]))))]))])]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_7(self):
        """Test Complex Program """
        input = '''
        class Example1 {
            int factorial(int n){
                if n == 0 then return 1; else return n * this.factorial(n - 1);
            }
            void main(){
                int x;
                io.writeIntLn(this.factorial(x));
            }
        }
            '''
        expect = str(Program([ClassDecl(Id("Example1"), [MethodDecl(Instance(), Id("factorial"), [VarDecl(Id("n"), IntType())], IntType(), Block([], [If(BinaryOp("==", Id("n"), IntLiteral(0)), Return(IntLiteral(1)), Return(BinaryOp(
            "*", Id("n"), CallExpr(SelfLiteral(), Id("factorial"), [BinaryOp("-", Id("n"), IntLiteral(1))]))))])), MethodDecl(Instance(), Id("main"),  [], VoidType(), Block([VarDecl(Id("x"), IntType())], [CallStmt(Id("io"), Id("writeIntLn"), [CallExpr(SelfLiteral(), Id("factorial"), [Id("x")])])]))])]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_8(self):
        """Test Complex Program """
        input = '''
        class Shape {
            float length,width;
            float getArea() {}
            Shape(float length,width){
                this.length := length;
                this.width := width;
            }
        }
            '''
        expect = str(Program([ClassDecl(Id("Shape"), [AttributeDecl(Instance(), VarDecl(Id("length"), FloatType())), AttributeDecl(Instance(), VarDecl(Id("width"), FloatType())), MethodDecl(Instance(), Id("getArea"),  [], FloatType(), Block([], [])), MethodDecl(
            Instance(), Id("<init>"), [VarDecl(Id("length"), FloatType()), VarDecl(Id("width"), FloatType())], None, Block([], [Assign(FieldAccess(SelfLiteral(), Id("length")), Id("length")), Assign(FieldAccess(SelfLiteral(), Id("width")), Id("width"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_9(self):
        """Test Complex Program """
        input = '''
        class Rectangle extends Shape {
            float getArea(){
                return this.length*this.width;
            }
        }
            '''
        expect = str(Program([ClassDecl(Id("Rectangle"), [MethodDecl(Instance(), Id("getArea"), [], FloatType(), Block(
            [], [Return(BinaryOp("*", FieldAccess(SelfLiteral(), Id("length")), FieldAccess(SelfLiteral(), Id("width"))))]))], Id("Shape"))]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_10(self):
        """Test Complex Program """
        input = '''
    class Triangle extends Shape {
        float getArea(){
            return this.length*this.width / 2;
        }
    }
            '''
        expect = str(Program([ClassDecl(Id("Triangle"), [MethodDecl(Instance(), Id("getArea"), [], FloatType(), Block([], [
                     Return(BinaryOp("/", BinaryOp("*", FieldAccess(SelfLiteral(), Id("length")), FieldAccess(SelfLiteral(), Id("width"))), IntLiteral(2)))]))], Id("Shape"))]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_11(self):
        """Test Complex Program """
        input = '''
            class Example2 {
                void main(){
                    s := new Rectangle(3,4);
                }
            }
        '''
        expect = str(Program([ClassDecl(Id("Example2"), [MethodDecl(Instance(), Id("main"), [], VoidType(), Block(
            [], [Assign(Id("s"), NewExpr(Id("Rectangle"), [IntLiteral(3), IntLiteral(4)]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_12(self):
        """Test Complex Program """
        input = '''
            class Example2 {
                float a, b, c;
                boolean x, y, z;
                int g, h, y;
                float nty(){}
                int x, y, z;
                int q, w;
                string a;
    /*
        =======================================
        Comment here
        =======================================
    */
            }
        '''
        expect = str(Program([ClassDecl(Id("Example2"), [AttributeDecl(Instance(), VarDecl(Id("a"), FloatType())), AttributeDecl(Instance(), VarDecl(Id("b"), FloatType())), AttributeDecl(Instance(), VarDecl(Id("c"), FloatType())), AttributeDecl(Instance(), VarDecl(Id("x"), BoolType())), AttributeDecl(Instance(), VarDecl(Id("y"), BoolType())), AttributeDecl(Instance(), VarDecl(Id("z"), BoolType())), AttributeDecl(Instance(), VarDecl(Id("g"), IntType())), AttributeDecl(Instance(), VarDecl(
            Id("h"), IntType())), AttributeDecl(Instance(), VarDecl(Id("y"), IntType())), MethodDecl(Instance(), Id("nty"), [], FloatType(), Block([], [])), AttributeDecl(Instance(), VarDecl(Id("x"), IntType())), AttributeDecl(Instance(), VarDecl(Id("y"), IntType())), AttributeDecl(Instance(), VarDecl(Id("z"), IntType())), AttributeDecl(Instance(), VarDecl(Id("q"), IntType())), AttributeDecl(Instance(), VarDecl(Id("w"), IntType())), AttributeDecl(Instance(), VarDecl(Id("a"), StringType()))])]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_13(self):
        """Test Complex Program """

        input = '''
class Example2 {
float nty(){
    b[3]:={1,2,3};
    a[3+x.foo(2)] := a[b[2]] +3;
}
}
        '''
        expect = str(Program([ClassDecl(Id("Example2"), [MethodDecl(Instance(), Id("nty"), [], FloatType(), Block([], [Assign(ArrayCell(Id("b"), IntLiteral(3)), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])), Assign(
            ArrayCell(Id("a"), BinaryOp("+", IntLiteral(3), CallExpr(Id("x"), Id("foo"), [IntLiteral(2)]))), BinaryOp("+", ArrayCell(Id("a"), ArrayCell(Id("b"), IntLiteral(2))), IntLiteral(3)))]))])]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_14(self):
        """Test Complex Program """
        input = '''
class Example2 {
    float nty(){
# start of declaration part
float r,s;
int[5] a,b;
# list of statements
r:=2.0;
s:=r*r*this.myPI;
a[0]:= s;
}
}
        '''
        expect = str(Program([ClassDecl(Id("Example2"), [MethodDecl(Instance(), Id("nty"), [], FloatType(), Block([VarDecl(Id("r"), FloatType()), VarDecl(Id("s"), FloatType()), VarDecl(Id("a"), ArrayType(5, IntType())), VarDecl(
            Id("b"), ArrayType(5, IntType()))], [Assign(Id("r"), FloatLiteral(2.0)), Assign(Id("s"), BinaryOp("*", BinaryOp("*", Id("r"), Id("r")), FieldAccess(SelfLiteral(), Id("myPI")))), Assign(ArrayCell(Id("a"), IntLiteral(0)), Id("s"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_15(self):
        """Test Complex Program """
        input = '''
 class Example2 {
     float nty(){
        if flag then
            r:=2.0;
        else
            a[0]:= s; }
    }
         '''
        expect = str(Program([ClassDecl(Id("Example2"), [MethodDecl(Instance(), Id("nty"), [], FloatType(), Block([], [If(
            Id("flag"), Assign(Id("r"), FloatLiteral(2.0)), Assign(ArrayCell(Id("a"), IntLiteral(0)), Id("s")))]))])]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_16(self):
        """Test Complex Program """
        input = '''
class Example2 {
    float nty(){
        for i := 1 to 100 do {
            io.writeIntLn(i);
            Intarray[i] := i + 1;
        }
        for x := 5 downto 2 do
            io.writeIntLn(x);
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Example2"), [MethodDecl(Instance(), Id("nty"), [], FloatType(), Block([], [For(Id("i"), IntLiteral(1), IntLiteral(100), True, Block([], [CallStmt(Id("io"), Id("writeIntLn"), [
                     Id("i")]), Assign(ArrayCell(Id("Intarray"), Id("i")), BinaryOp("+", Id("i"), IntLiteral(1)))])), For(Id("x"), IntLiteral(5), IntLiteral(2), False, CallStmt(Id("io"), Id("writeIntLn"), [Id("x")]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_17(self):
        """Test Complex Program """
        input = '''
class Person {
        string firstName; # property
        string lastName;  # property
        int age;          # property
        void fullname() {
        }
}
        '''
        expect = str(Program([ClassDecl(Id("Person"), [AttributeDecl(Instance(), VarDecl(Id("firstName"), StringType())), AttributeDecl(Instance(), VarDecl(
            Id("lastName"), StringType())), AttributeDecl(Instance(), VarDecl(Id("age"), IntType())), MethodDecl(Instance(), Id("fullname"), [], VoidType(), Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_18(self):
        """Test Complex Program """
        input = '''
    class Person {
        string firstName; # property
        string lastName;  # property
        int age;          # property
    }
    '''
        expect = str(Program([ClassDecl(Id("Person"), [AttributeDecl(Instance(), VarDecl(Id("firstName"), StringType())), AttributeDecl(
            Instance(), VarDecl(Id("lastName"), StringType())), AttributeDecl(Instance(), VarDecl(Id("age"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_19(self):
        """Test Complex Program """
        input = '''
     class Person {
            string firstName; # property
            string lastName;  # property
            int age;          # property
            string c(){
                s := a +b + c * d;
                d := a && b;
                e := !a;
            }
    }
            '''
        expect = str(Program([ClassDecl(Id("Person"), [AttributeDecl(Instance(), VarDecl(Id("firstName"), StringType())), AttributeDecl(Instance(), VarDecl(Id("lastName"), StringType())), AttributeDecl(Instance(), VarDecl(Id("age"), IntType())), MethodDecl(
            Instance(), Id("c"), [], StringType(), Block([], [Assign(Id("s"), BinaryOp("+", BinaryOp("+", Id("a"), Id("b")), BinaryOp("*", Id("c"), Id("d")))), Assign(Id("d"), BinaryOp("&&", Id("a"), Id("b"))), Assign(Id("e"), UnaryOp("!", Id("a")))]))])]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_20(self):
        """Test Complex Program """
        input = '''
 class Test {
        int abc(){}
        boolean abc(){}
        float[5] abc(){}
        void print(){}
        int[5] abc(){}
        string low2up(){}
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("abc"), [], IntType(), Block([], [])), MethodDecl(Instance(), Id("abc"), [], BoolType(), Block([], [])), MethodDecl(Instance(), Id("abc"), [], ArrayType(5, FloatType()), Block(
            [], [])), MethodDecl(Instance(), Id("print"), [], VoidType(), Block([], [])), MethodDecl(Instance(), Id("abc"), [], ArrayType(5, IntType()), Block([], [])), MethodDecl(Instance(), Id("low2up"), [], StringType(), Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_21(self):
        """Test Complex Program """
        input = '''
 class Test {
        boolean abc__bc_ab(int c){
        }
        void print(string a){
            a.printf("hello" + a);
        }
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("abc__bc_ab"), [VarDecl(Id("c"), IntType())], BoolType(), Block([], [])), MethodDecl(
            Instance(), Id("print"), [VarDecl(Id("a"), StringType())], VoidType(), Block([], [CallStmt(Id("a"), Id("printf"), [BinaryOp("+", StringLiteral('"hello"'), Id("a"))])]))])]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_22(self):
        """Test Complex Program """
        input = '''
 class Test {
        float square ( float x )   # function definition
{
    float p ;
    p := x * x ;
    return  p  ;
}
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("square"), [VarDecl(Id("x"), FloatType())], FloatType(), Block(
            [VarDecl(Id("p"), FloatType())], [Assign(Id("p"), BinaryOp("*", Id("x"), Id("x"))), Return(Id("p"))]))])]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_23(self):
        """Test Complex Program """
        input = '''
 class Test {
    boolean swap(int a; int b)
{


}
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("swap"), [
                     VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType())], BoolType(), Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_24(self):
        """Test Complex Program """
        input = '''
 class Test {
     int a(int abc){}
        float a(int[5] a){}
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("a"), [VarDecl(Id("abc"), IntType())], IntType(), Block(
            [], [])), MethodDecl(Instance(), Id("a"), [VarDecl(Id("a"), ArrayType(5, IntType()))], FloatType(), Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_25(self):
        """Test Complex Program """
        input = '''
 class Test {
    void a(){}
    string a(int a; int b; int c; float[1] d){}
    float a(int a, b, c){}
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("a"), [], VoidType(), Block([], [])), MethodDecl(Instance(), Id("a"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), IntType()), VarDecl(
            Id("d"), ArrayType(1, FloatType()))], StringType(), Block([], [])), MethodDecl(Instance(), Id("a"), [VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), IntType())], FloatType(), Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_26(self):
        """Test Complex Program """
        input = '''
 class Test {
    int float2int(float a){}
    int a(int[1] a; int b; string[5] c; string d){}
    float b(){}
    int c(string[7] c; int a; int b){}
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("float2int"), [VarDecl(Id("a"), FloatType())], IntType(), Block([], [])), MethodDecl(Instance(), Id("a"), [VarDecl(Id("a"), ArrayType(1, IntType())), VarDecl(Id("b"), IntType()), VarDecl(Id("c"), ArrayType(5, StringType())), VarDecl(
            Id("d"), StringType())], IntType(), Block([], [])), MethodDecl(Instance(), Id("b"), [], FloatType(), Block([], [])), MethodDecl(Instance(), Id("c"), [VarDecl(Id("c"), ArrayType(7, StringType())), VarDecl(Id("a"), IntType()), VarDecl(Id("b"), IntType())], IntType(), Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_27(self):
        """Test Complex Program """
        input = '''
    class Test {
    boolean swap(int a; int b)
    {


    }
    }
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("swap"), [VarDecl(
            Id("a"), IntType()), VarDecl(Id("b"), IntType())], BoolType(), Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_28(self):
        """Test Complex Program """
        input = '''
class Test {
        int  main()
{
    int i;
    i := 8;
    test.printf("Factorial of the number is ", i, test.factorial(i));
    return 0;
}
int factorial( int i)
{
   if(i < 2) then
   {
      return 1;
   }
   return i * Test.factorial(i - 1);
}
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block([VarDecl(Id("i"), IntType())], [Assign(Id("i"), IntLiteral(8)), CallStmt(Id("test"), Id("printf"), [StringLiteral('"Factorial of the number is "'), Id("i"), CallExpr(Id("test"), Id("factorial"), [Id("i")])]), Return(
            IntLiteral(0))])), MethodDecl(Instance(), Id("factorial"),  [VarDecl(Id("i"), IntType())], IntType(), Block([], [If(BinaryOp("<", Id("i"), IntLiteral(2)), Block([], [Return(IntLiteral(1))])), Return(BinaryOp("*", Id("i"), CallExpr(Id("Test"), Id("factorial"), [BinaryOp("-", Id("i"), IntLiteral(1))])))]))])]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_29(self):
        """Test Complex Program """
        input = '''
class Test {
        int main()
{
    if flag then
       a:=1;
    else{
        if flag then
            a:=2;
        else{
            if flag then
                a:=3;
            else{
                return 0;
            }
        }
    }
}
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [If(Id("flag"), Assign(Id("a"), IntLiteral(1)), Block(
            [], [If(Id("flag"), Assign(Id("a"), IntLiteral(2)), Block([], [If(Id("flag"), Assign(Id("a"), IntLiteral(3)), Block([], [Return(IntLiteral(0))]))]))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_30(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            a := Other.b() + Other.c() + Other.d();
            Other.print(a);
            a := a / Other.sum(a,b) + Other.sub(a,b);
        }
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [Assign(Id("a"), BinaryOp("+", BinaryOp("+", CallExpr(Id("Other"), Id("b"), []), CallExpr(Id("Other"), Id("c"), [])), CallExpr(
            Id("Other"), Id("d"), []))), CallStmt(Id("Other"), Id("print"), [Id("a")]), Assign(Id("a"), BinaryOp("+", BinaryOp("/", Id("a"), CallExpr(Id("Other"), Id("sum"), [Id("a"), Id("b")])), CallExpr(Id("Other"), Id("sub"), [Id("a"), Id("b")])))]))])]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_31(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            return 1+2;
        }
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("main"), [
        ], IntType(), Block([], [Return(BinaryOp("+", IntLiteral(1), IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_32(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            return true;
        }
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id(
            "main"), [], IntType(), Block([], [Return(BooleanLiteral(True))]))])]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_33(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            return "abc"^"cde";
        }
}
        '''
        expect = str(Program([ClassDecl(Id("Test"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block(
            [], [Return(BinaryOp("^", StringLiteral('"abc"'), StringLiteral('"cde"')))]))])]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_34(self):
        """Test Complex Program """
        input = '''
class Student {
     int id;  # truong hoac thanh vien du lieu
     float salary; # truong hoac thanh vien du lieu
     String name; #  truong hoac thanh vien du lieu
 }
        '''
        expect = str(Program([ClassDecl(Id("Student"), [AttributeDecl(Instance(), VarDecl(Id("id"), IntType())), AttributeDecl(
            Instance(), VarDecl(Id("salary"), FloatType())), AttributeDecl(Instance(), VarDecl(Id("name"), ClassType(Id("String"))))])]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_35(self):
        """Test Complex Program """
        input = '''
class Student {
        int id;
        string name;
        void insert(int i; string n) {
            id := i;
            name := n;
        }
        void display() {
            return id^name;
        }
}
        '''
        expect = str(Program([ClassDecl(Id("Student"), [AttributeDecl(Instance(), VarDecl(Id("id"), IntType())), AttributeDecl(Instance(), VarDecl(Id("name"), StringType())), MethodDecl(Instance(), Id("insert"), [VarDecl(Id("i"), IntType()), VarDecl(
            Id("n"), StringType())], VoidType(), Block([], [Assign(Id("id"), Id("i")), Assign(Id("name"), Id("n"))])), MethodDecl(Instance(), Id("display"), [], VoidType(), Block([], [Return(BinaryOp("^", Id("id"), Id("name")))]))])]))

        self.assertTrue(TestAST.test(input, expect, 334))

    def test_36(self):
        """Test Complex Program """
        input = '''
class sinhvien
{
        string masinhvien, ten, quequan;
        int tuoi;
        float diemtoan, diemly, diemhoa;
        void di(){}
        void dung(){}
        void ngoi(){}
        void hoctap(){}
}
        '''
        expect = str(Program([ClassDecl(Id("sinhvien"), [AttributeDecl(Instance(), VarDecl(Id("masinhvien"), StringType())), AttributeDecl(Instance(), VarDecl(Id("ten"), StringType())), AttributeDecl(Instance(), VarDecl(Id("quequan"), StringType())), AttributeDecl(Instance(), VarDecl(Id("tuoi"), IntType())), AttributeDecl(Instance(), VarDecl(Id("diemtoan"), FloatType())), AttributeDecl(
            Instance(), VarDecl(Id("diemly"), FloatType())), AttributeDecl(Instance(), VarDecl(Id("diemhoa"), FloatType())), MethodDecl(Instance(), Id("di"), [], VoidType(), Block([], [])), MethodDecl(Instance(), Id("dung"), [], VoidType(), Block([], [])), MethodDecl(Instance(), Id("ngoi"), [], VoidType(), Block([], [])), MethodDecl(Instance(), Id("hoctap"), [], VoidType(), Block([], []))])]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_37(self):
        """Test Complex Program """
        input = '''
class CallbackHell
{
    int main(){
        if(1)then{
            if(1)then{
                if(1)then{
                    if(1)then{
                        return 1;
                    }
                }
            }
        }
    }
}
        '''
        expect = str(Program([ClassDecl(Id("CallbackHell"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [If(IntLiteral(1), Block(
            [], [If(IntLiteral(1), Block([], [If(IntLiteral(1), Block([], [If(IntLiteral(1), Block([], [Return(IntLiteral(1))]))]))]))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_38(self):
        """Test Complex Program """
        input = '''
class CallbackHell
{
    int main(){
        for i := 1 to 100 do {
            for x := 5 downto 2 do {
                if(1)then{
                    if(1)then{
                        if(1)then{
                            if(1)then{
                                return 1;
                            }
                        }
                    }
                }
            }
        }
    }
}
        '''
        expect = str(Program([ClassDecl(Id("CallbackHell"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [For(Id("i"), IntLiteral(1), IntLiteral(100), True, Block([], [For(Id("x"), IntLiteral(
            5), IntLiteral(2), False, Block([], [If(IntLiteral(1), Block([], [If(IntLiteral(1), Block([], [If(IntLiteral(1), Block([], [If(IntLiteral(1), Block([], [Return(IntLiteral(1))]))]))]))]))]))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_39(self):
        """Test Complex Program """
        input = '''
class CallbackHell
{
    int main(){
        return "string";
    }
    int mainInt(){
        return 1;
    }
    int mainFloat(){
        return 1.0;
    }
}
        '''
        expect = str(Program([ClassDecl(Id("CallbackHell"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [Return(StringLiteral('"string"'))])), MethodDecl(Instance(
        ), Id("mainInt"), [], IntType(), Block([], [Return(IntLiteral(1))])), MethodDecl(Instance(), Id("mainFloat"), [], IntType(), Block([], [Return(FloatLiteral(1.0))]))])]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_40(self):
        """Test Complex Program """
        input = '''
class Shape {
    float length,width;
    float getArea() {}
    Shape(float length,width){
        this.length := length;
        this.width := width;
    }
}
class Rectangle extends Shape {
    float getArea(){
        return this.length*this.width;
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Shape"), [AttributeDecl(Instance(), VarDecl(Id("length"), FloatType())), AttributeDecl(Instance(), VarDecl(Id("width"), FloatType())), MethodDecl(Instance(), Id("getArea"), [], FloatType(), Block([], [])), MethodDecl(Instance(), Id("<init>"), [VarDecl(Id("length"), FloatType()), VarDecl(Id("width"), FloatType())], None, Block(
            [], [Assign(FieldAccess(SelfLiteral(), Id("length")), Id("length")), Assign(FieldAccess(SelfLiteral(), Id("width")), Id("width"))]))]), ClassDecl(Id("Rectangle"), [MethodDecl(Instance(), Id("getArea"), [], FloatType(), Block([], [Return(BinaryOp("*", FieldAccess(SelfLiteral(), Id("length")), FieldAccess(SelfLiteral(), Id("width"))))]))], Id("Shape"))]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_41(self):
        """Test Complex Program """
        input = '''
class Parent {
    int p;
}
class Child extends Parent {
    int c;
}
        '''
        expect = str(Program([ClassDecl(Id("Parent"), [AttributeDecl(Instance(), VarDecl(Id("p"), IntType()))]), ClassDecl(
            Id("Child"), [AttributeDecl(Instance(), VarDecl(Id("c"), IntType()))], Id("Parent"))]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_42(self):
        """Test Complex Program """
        input = '''
class Operator
{
    void main()
    {
        return 1/2+3/4+5/6+7/8+8/9;
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Operator"), [MethodDecl(Instance(), Id("main"), [], VoidType(), Block([], [Return(BinaryOp("+", BinaryOp("+", BinaryOp("+", BinaryOp("+", BinaryOp(
            "/", IntLiteral(1), IntLiteral(2)), BinaryOp("/", IntLiteral(3), IntLiteral(4))), BinaryOp("/", IntLiteral(5), IntLiteral(6))), BinaryOp("/", IntLiteral(7), IntLiteral(8))), BinaryOp("/", IntLiteral(8), IntLiteral(9))))]))])]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_43(self):
        """Test Complex Program """
        input = '''
class Operator
{
    void main()
    {
        return 1.1\\2.2;
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Operator"), [MethodDecl(Instance(), Id("main"), [], VoidType(
        ), Block([], [Return(BinaryOp("\\", FloatLiteral(1.1), FloatLiteral(2.2)))]))])]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_44(self):
        """Test Complex Program """
        input = '''
class Operator
{
    void main()
    {
        return 1>=2;
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Operator"), [MethodDecl(Instance(), Id("main"), [
        ], VoidType(), Block([], [Return(BinaryOp(">=", IntLiteral(1), IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_45(self):
        """Test Complex Program """
        input = '''
class Operator
{
    int main()
    {
        return -1;
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Operator"), [MethodDecl(Instance(), Id(
            "main"), [], IntType(), Block([], [Return(UnaryOp("-", IntLiteral(1)))]))])]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_46(self):
        """Test Complex Program """
        input = '''
class Operator
{
    int main()
    {
        return -1/-2;
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Operator"), [MethodDecl(Instance(), Id("main"), [], IntType(
        ), Block([], [Return(BinaryOp("/", UnaryOp("-", IntLiteral(1)), UnaryOp("-", IntLiteral(2))))]))])]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_47(self):
        """Test Complex Program """
        input = '''
class Operator
{
    int main()
    {
        return -1+-2+1.1+-1.2;
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Operator"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [Return(BinaryOp(
            "+", BinaryOp("+", BinaryOp("+", UnaryOp("-", IntLiteral(1)), UnaryOp("-", IntLiteral(2))), FloatLiteral(1.1)), UnaryOp("-", FloatLiteral(1.2))))]))])]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_48(self):
        """Test Complex Program """
        input = '''
class Operator
{
    int a=0;
    int main()
    {
        for i := 1 to 100 do {
            if i==2 then
                break;
            else
                a:=a+1;
        }
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Operator"), [AttributeDecl(Instance(), VarDecl(Id("a"), IntType(), IntLiteral(0))), MethodDecl(Instance(), Id("main"), [], IntType(), Block(
            [], [For(Id("i"), IntLiteral(1), IntLiteral(100), True, Block([], [If(BinaryOp("==", Id("i"), IntLiteral(2)), Break(), Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1))))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_49(self):
        """Test Complex Program """
        input = '''
class Operator
{
    int main()
    {
        return 1.0e10/1.2e10;
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Operator"), [MethodDecl(Instance(), Id("main"), [], IntType(), Block(
            [], [Return(BinaryOp("/", FloatLiteral(10000000000.0), FloatLiteral(12000000000.0)))]))])]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_50(self):
        """Test Complex Program """
        input = '''
class Operator
{
    void main()
    {
        a[(3+x.foo(2))/5*3-25] := a[b[2]] +3*a[4]/3;
    }
}
        '''
        expect = str(Program([ClassDecl(Id("Operator"), [MethodDecl(Instance(), Id("main"), [], VoidType(), Block([], [Assign(ArrayCell(Id("a"), BinaryOp("-", BinaryOp("*", BinaryOp("/", BinaryOp("+", IntLiteral(3), CallExpr(Id("x"), Id("foo"), [
                     IntLiteral(2)])), IntLiteral(5)), IntLiteral(3)), IntLiteral(25))), BinaryOp("+", ArrayCell(Id("a"), ArrayCell(Id("b"), IntLiteral(2))), BinaryOp("/", BinaryOp("*", IntLiteral(3), ArrayCell(Id("a"), IntLiteral(4))), IntLiteral(3))))]))])]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_51(self):
        input = """
        class Maim {
            void main(){
                string [2] a="Hello world | checker";
                a.boo()[2] := b.boo[a.boo() +3];
            }
        }
        """
        expect = str(Program([ClassDecl(Id("Maim"), [MethodDecl(Instance(), Id("main"), [], VoidType(), Block([VarDecl(Id("a"), ArrayType(2, StringType()), StringLiteral('"Hello world | checker"'))], [
                     Assign(ArrayCell(CallExpr(Id("a"), Id("boo"), []), IntLiteral(2)), ArrayCell(FieldAccess(Id("b"), Id("boo")), BinaryOp("+", CallExpr(Id("a"), Id("boo"), []), IntLiteral(3))))]))])]))

        self.assertTrue(TestAST.test(input, expect, 350))

    def test_52(self):
        input = """class main {
            int a;
        }"""
        expect = str(Program(
            [ClassDecl(Id("main"), [AttributeDecl(Instance(), VarDecl(Id("a"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_53(self):
        input = """class main {
            static int a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
                                        [AttributeDecl(Static(), VarDecl(Id("a"), IntType()))
                                         ])]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_54(self):
        input = """class main {
            static int a,b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
                                        [AttributeDecl(Static(), VarDecl(Id("a"), IntType())),
                                         AttributeDecl(Static(), VarDecl(Id("b"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_55(self):
        input = """class main {
            int a,b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
                                        [AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                                         AttributeDecl(Instance(), VarDecl(Id("b"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_56(self):
        input = """class main {
            final int a=1,b=2;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
                                        [AttributeDecl(Instance(), ConstDecl(Id("a"), IntType(), IntLiteral(1))),
                                         AttributeDecl(Instance(), ConstDecl(Id("b"), IntType(), IntLiteral(2)))])]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_57(self):
        input = """class main {
            final static int a=1,b=1;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
                                        [AttributeDecl(Static(), ConstDecl(Id("a"), IntType(), IntLiteral(1))),
                                         AttributeDecl(Static(), ConstDecl(Id("b"), IntType(), IntLiteral(1)))])]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_58(self):
        input = """
        class XXX { }
        class main {
            final static int a=1,b=1;

        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(), ConstDecl(Id("a"), IntType(), IntLiteral(1))),
                 AttributeDecl(Static(), ConstDecl(Id("b"), IntType(), IntLiteral(1)))]
            )]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_59(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(), ConstDecl(Id("a"), IntType(), IntLiteral(1))),
                 AttributeDecl(Static(), ConstDecl(
                     Id("b"), IntType(), IntLiteral(2))),
                 AttributeDecl(Instance(), ConstDecl(
                     Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                 AttributeDecl(Instance(), ConstDecl(
                     Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                 AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                 AttributeDecl(Instance(), VarDecl(
                     Id("b"), IntType(), IntLiteral(1))),
                 ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_60(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(){}
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(), ConstDecl(
                        Id("a"), IntType(), IntLiteral(1))),
                    AttributeDecl(Static(), ConstDecl(
                        Id("b"), IntType(), IntLiteral(2))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id("b"), IntType(), IntLiteral(1))),
                    MethodDecl(Static(), Id('method'), [],
                               IntType(), Block([], []))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_61(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a,b; float a){}
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(), ConstDecl(Id("a"), IntType(), IntLiteral(1))),
                 AttributeDecl(Static(), ConstDecl(
                     Id("b"), IntType(), IntLiteral(2))),
                 AttributeDecl(Instance(), ConstDecl(
                     Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                 AttributeDecl(Instance(), ConstDecl(
                     Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                 AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                 AttributeDecl(Instance(), VarDecl(
                     Id("b"), IntType(), IntLiteral(1))),
                 MethodDecl(Static(), Id('method'), [
                     VarDecl(Id('a'), IntType()),
                     VarDecl(Id('b'), IntType()),
                     VarDecl(Id('a'), FloatType()),
                 ], IntType(), Block([], []))
                 ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_62(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(), ConstDecl(
                        Id("a"), IntType(), IntLiteral(1))),
                    AttributeDecl(Static(), ConstDecl(
                        Id("b"), IntType(), IntLiteral(2))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id("b"), IntType(), IntLiteral(1))),
                    MethodDecl(Static(), Id('method'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], IntType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        ConstDecl(Id("a"), FloatType(), FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"), FloatType(), FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                    ], []))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_63(self):
        input = """
        class XXX { }
        class main extends XXX {
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
            }
            void method1(int a; float a,b){
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"),
                [AttributeDecl(Static(), ConstDecl(Id("a"), IntType(), IntLiteral(1))),
                 AttributeDecl(Static(), ConstDecl(
                     Id("b"), IntType(), IntLiteral(2))),
                 AttributeDecl(Instance(), ConstDecl(
                     Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                 AttributeDecl(Instance(), ConstDecl(
                     Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                 AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                 AttributeDecl(Instance(), VarDecl(
                     Id("b"), IntType(), IntLiteral(1))),
                 MethodDecl(Static(), Id('method'), [
                     VarDecl(Id('a'), IntType()),
                     VarDecl(Id('a'), FloatType()),
                     VarDecl(Id('b'), FloatType()),
                 ], IntType(), Block([
                     ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                     ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                     ConstDecl(Id("a"), FloatType(), FloatLiteral(1.1e+1)),
                     ConstDecl(Id("b"), FloatType(), FloatLiteral(2.2e+2)),
                     VarDecl(Id("a"), IntType()),
                     VarDecl(Id("b"), IntType()),
                 ], [])),
                    MethodDecl(Instance(), Id('method1'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], VoidType(), Block([], []))
                 ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_64(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(), ConstDecl(
                        Id("a"), IntType(), IntLiteral(1))),
                    AttributeDecl(Static(), ConstDecl(
                        Id("b"), IntType(), IntLiteral(2))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id("b"), IntType(), IntLiteral(1))),
                    MethodDecl(Static(), Id('method'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], IntType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        ConstDecl(Id("a"), FloatType(), FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"), FloatType(), FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                    ], [])),
                    MethodDecl(Instance(), Id('method1'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], VoidType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                    ], []))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_65(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(), ConstDecl(
                        Id("a"), IntType(), IntLiteral(1))),
                    AttributeDecl(Static(), ConstDecl(
                        Id("b"), IntType(), IntLiteral(2))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id("b"), IntType(), IntLiteral(1))),
                    MethodDecl(Static(), Id('method'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], IntType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        ConstDecl(Id("a"), FloatType(), FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"), FloatType(), FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                    ], [
                        Return(Id('a'))
                    ])),
                    MethodDecl(Instance(), Id('method1'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], VoidType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                    ], [
                        Return(IntLiteral(1))
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_66(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(), ConstDecl(
                        Id("a"), IntType(), IntLiteral(1))),
                    AttributeDecl(Static(), ConstDecl(
                        Id("b"), IntType(), IntLiteral(2))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id("b"), IntType(), IntLiteral(1))),
                    MethodDecl(Static(), Id('method'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], IntType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        ConstDecl(Id("a"), FloatType(), FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"), FloatType(), FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                    ], [
                        Return(Id('a'))
                    ])),
                    MethodDecl(Instance(), Id('method1'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], VoidType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        VarDecl(Id("r"), FloatType()),
                        VarDecl(Id("s"), FloatType()),
                        VarDecl(Id("a"), ArrayType(5, IntType())),
                        VarDecl(Id("b"), ArrayType(5, IntType())),
                    ], [
                        Return(IntLiteral(1))
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_67(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(), ConstDecl(
                        Id("a"), IntType(), IntLiteral(1))),
                    AttributeDecl(Static(), ConstDecl(
                        Id("b"), IntType(), IntLiteral(2))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id("b"), IntType(), IntLiteral(1))),
                    MethodDecl(Static(), Id('method'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], IntType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        ConstDecl(Id("a"), FloatType(), FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"), FloatType(), FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                    ], [
                        Return(Id('a'))
                    ])),
                    MethodDecl(Instance(), Id('method1'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], VoidType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        VarDecl(Id("r"), FloatType()),
                        VarDecl(Id("s"), FloatType()),
                        VarDecl(Id("a"), ArrayType(5, IntType())),
                        VarDecl(Id("b"), ArrayType(5, IntType())),
                    ], [
                        Assign(FieldAccess(SelfLiteral(), Id('myPI')),
                               FloatLiteral(3.14)),
                        Assign(Id('value'), CallExpr(
                            Id('x'), Id('foo'), [IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'), IntLiteral(3)),
                               BinaryOp('/', Id('value'), IntLiteral(2))),
                        Assign(Id('r'), FloatLiteral(2.0)),
                        Assign(Id('s'), BinaryOp(
                            '*', BinaryOp('*', Id('r'), Id('r')), FieldAccess(SelfLiteral(), Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_68(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then
                    a := b;
                else
                    { }
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(), ConstDecl(
                        Id("a"), IntType(), IntLiteral(1))),
                    AttributeDecl(Static(), ConstDecl(
                        Id("b"), IntType(), IntLiteral(2))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id("b"), IntType(), IntLiteral(1))),
                    MethodDecl(Static(), Id('method'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], IntType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        ConstDecl(Id("a"), FloatType(), FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"), FloatType(), FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                    ], [
                        If(Id('flag'), Assign(Id('a'), Id('b')), Block([], [])),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(), Id('method1'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], VoidType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        VarDecl(Id("r"), FloatType()),
                        VarDecl(Id("s"), FloatType()),
                        VarDecl(Id("a"), ArrayType(5, IntType())),
                        VarDecl(Id("b"), ArrayType(5, IntType())),
                    ], [
                        Assign(FieldAccess(SelfLiteral(), Id('myPI')),
                               FloatLiteral(3.14)),
                        Assign(Id('value'), CallExpr(
                            Id('x'), Id('foo'), [IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'), IntLiteral(3)),
                               BinaryOp('/', Id('value'), IntLiteral(2))),
                        Assign(Id('r'), FloatLiteral(2.0)),
                        Assign(Id('s'), BinaryOp(
                            '*', BinaryOp('*', Id('r'), Id('r')), FieldAccess(SelfLiteral(), Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_69(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then
                    a := b;
                else if a==b then
                    {}
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(), ConstDecl(
                        Id("a"), IntType(), IntLiteral(1))),
                    AttributeDecl(Static(), ConstDecl(
                        Id("b"), IntType(), IntLiteral(2))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id("b"), IntType(), IntLiteral(1))),
                    MethodDecl(Static(), Id('method'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], IntType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        ConstDecl(Id("a"), FloatType(), FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"), FloatType(), FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                    ], [
                        If(Id('flag'), Assign(Id('a'), Id('b')),
                            If(BinaryOp('==', Id('a'), Id('b')), Block([], []))
                           ),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(), Id('method1'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], VoidType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        VarDecl(Id("r"), FloatType()),
                        VarDecl(Id("s"), FloatType()),
                        VarDecl(Id("a"), ArrayType(5, IntType())),
                        VarDecl(Id("b"), ArrayType(5, IntType())),
                    ], [
                        Assign(FieldAccess(SelfLiteral(), Id('myPI')),
                               FloatLiteral(3.14)),
                        Assign(Id('value'), CallExpr(
                            Id('x'), Id('foo'), [IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'), IntLiteral(3)),
                               BinaryOp('/', Id('value'), IntLiteral(2))),
                        Assign(Id('r'), FloatLiteral(2.0)),
                        Assign(Id('s'), BinaryOp(
                            '*', BinaryOp('*', Id('r'), Id('r')), FieldAccess(SelfLiteral(), Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_70(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then
                    a := b;
                else if a==b then
                    {a := -(b+1);}
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(), ConstDecl(
                        Id("a"), IntType(), IntLiteral(1))),
                    AttributeDecl(Static(), ConstDecl(
                        Id("b"), IntType(), IntLiteral(2))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id("b"), IntType(), IntLiteral(1))),
                    MethodDecl(Static(), Id('method'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], IntType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        ConstDecl(Id("a"), FloatType(), FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"), FloatType(), FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                    ], [
                        If(Id('flag'), Assign(Id('a'), Id('b')),
                            If(BinaryOp('==', Id('a'), Id('b')),
                                Block([], [Assign(Id('a'), UnaryOp('-', BinaryOp('+', Id('b'), IntLiteral(1))))]))
                           ),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(), Id('method1'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], VoidType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        VarDecl(Id("r"), FloatType()),
                        VarDecl(Id("s"), FloatType()),
                        VarDecl(Id("a"), ArrayType(5, IntType())),
                        VarDecl(Id("b"), ArrayType(5, IntType())),
                    ], [
                        Assign(FieldAccess(SelfLiteral(), Id('myPI')),
                               FloatLiteral(3.14)),
                        Assign(Id('value'), CallExpr(
                            Id('x'), Id('foo'), [IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'), IntLiteral(3)),
                               BinaryOp('/', Id('value'), IntLiteral(2))),
                        Assign(Id('r'), FloatLiteral(2.0)),
                        Assign(Id('s'), BinaryOp(
                            '*', BinaryOp('*', Id('r'), Id('r')), FieldAccess(SelfLiteral(), Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_71(self):
        input = """
        class XXX { }
        class main extends XXX {
            # this is a line comment
            /*
                this is also a comment do nha ^^
            */
            final static int a=1,b=2;
            final float a=1.1e+1, b=2.2e+2;
            int a,b=1;
            static int method(int a; float a,b){
                final int a=1,b=2;
                final float a=1.1e+1, b=2.2e+2;
                int a,b;
                if flag then
                    a := b;
                else if a==b then
                    {a := -(b+1);}
                else
                    {}
                return a;
            }
            void method1(int a; float a,b){
                final int a=1,b=2;
                float r,s;
                int[5] a,b;
                this.myPI := 3.14;
                value := x.foo(5);
                l[3] := value / 2;
                r := 2.0;
                s := r*r*this.myPI;
                return 1;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id('XXX'), []),
            ClassDecl(
                Id("main"), [
                    AttributeDecl(Static(), ConstDecl(
                        Id("a"), IntType(), IntLiteral(1))),
                    AttributeDecl(Static(), ConstDecl(
                        Id("b"), IntType(), IntLiteral(2))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("a"), FloatType(), FloatLiteral(1.1e+1))),
                    AttributeDecl(Instance(), ConstDecl(
                        Id("b"), FloatType(), FloatLiteral(2.2e+2))),
                    AttributeDecl(Instance(), VarDecl(Id("a"), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id("b"), IntType(), IntLiteral(1))),
                    MethodDecl(Static(), Id('method'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], IntType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        ConstDecl(Id("a"), FloatType(), FloatLiteral(1.1e+1)),
                        ConstDecl(Id("b"), FloatType(), FloatLiteral(2.2e+2)),
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                    ], [
                        If(Id('flag'), Assign(Id('a'), Id('b')),
                            If(BinaryOp('==', Id('a'), Id('b')),
                                Block([], [Assign(Id('a'), UnaryOp('-', BinaryOp('+', Id('b'), IntLiteral(1))))]), Block([], []))
                           ),
                        Return(Id('a')),
                    ])),
                    MethodDecl(Instance(), Id('method1'), [
                        VarDecl(Id('a'), IntType()),
                        VarDecl(Id('a'), FloatType()),
                        VarDecl(Id('b'), FloatType()),
                    ], VoidType(), Block([
                        ConstDecl(Id("a"), IntType(), IntLiteral(1)),
                        ConstDecl(Id("b"), IntType(), IntLiteral(2)),
                        VarDecl(Id("r"), FloatType()),
                        VarDecl(Id("s"), FloatType()),
                        VarDecl(Id("a"), ArrayType(5, IntType())),
                        VarDecl(Id("b"), ArrayType(5, IntType())),
                    ], [
                        Assign(FieldAccess(SelfLiteral(), Id('myPI')),
                               FloatLiteral(3.14)),
                        Assign(Id('value'), CallExpr(
                            Id('x'), Id('foo'), [IntLiteral(5)])),
                        Assign(ArrayCell(Id('l'), IntLiteral(3)),
                               BinaryOp('/', Id('value'), IntLiteral(2))),
                        Assign(Id('r'), FloatLiteral(2.0)),
                        Assign(Id('s'), BinaryOp(
                            '*', BinaryOp('*', Id('r'), Id('r')), FieldAccess(SelfLiteral(), Id('myPI')))),
                        Return(IntLiteral(1)),
                    ]))
                ],
                Id('XXX')
            )]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_72(self):
        input = """
        class XXX {
            int method(){
                for x:=1 to 100 do { }
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], IntType(), Block([], [
                For(Id('x'), IntLiteral(1), IntLiteral(100), True, Block([], []))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_73(self):
        input = """
        class XXX {
            int method(){
                for x:=1 to 100 do x := x \\ 1;
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], IntType(), Block([], [
                For(Id('x'), IntLiteral(1), IntLiteral(100), True,
                    Assign(Id('x'), BinaryOp('\\', Id('x'), IntLiteral(1)))
                    )
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_74(self):
        input = """
        class XXX {
            int method(){
                for x:=1 to 100 do {
                    io.writeIntLn(i);
                    Intarray[i] := i + 1;
                }
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], IntType(), Block([], [
                For(Id('x'), IntLiteral(1), IntLiteral(100), True, Block([], [
                    CallStmt(Id('io'), Id('writeIntLn'), [Id('i')]),
                    Assign(ArrayCell(Id('Intarray'), Id('i')),
                           BinaryOp('+', Id('i'), IntLiteral(1)))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_75(self):
        input = """
        class XXX {
            int method(){
                for x:=1 to 100 do {
                    if a then { }
                }
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], IntType(), Block([], [
                For(Id('x'), IntLiteral(1), IntLiteral(100), True, Block([], [
                    If(Id('a'), Block([], []))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_76(self):
        input = """
        class XXX {
            int method(){
                if a then {
                    for x:=1 to 100 do { }
                }
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], IntType(), Block([], [
                If(Id('a'), Block([], [
                    For(Id('x'), IntLiteral(1), IntLiteral(
                        100), True, Block([], []))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_77(self):
        input = """
        class XXX {
            int method(){
                break;
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], IntType(), Block([], [
                Break()
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_78(self):
        input = """
        class XXX {
            int method(){
                continue;
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], IntType(), Block([], [
                Continue()
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_79(self):
        input = """
        class XXX {
            int[5] method(){
                return {1,1.1E+1};
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], ArrayType(5, IntType()), Block([], [
                Return(ArrayLiteral(
                    [IntLiteral(1), FloatLiteral(1.1e+1)])),
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_80(self):
        input = """
        class XXX {
            int[5] method(){ }
            static int[5] method(){ }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [],
                       ArrayType(5, IntType()), Block([], [])),
            MethodDecl(Static(), Id('method'), [],
                       ArrayType(5, IntType()), Block([], [])),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_81(self):
        input = """
        class XXX {
            XXX method(){ }
            static XXX method(){ }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [],
                       ClassType(Id('XXX')), Block([], [])),
            MethodDecl(Static(), Id('method'), [],
                       ClassType(Id('XXX')), Block([], [])),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_82(self):
        input = """
        class XXX {
            XXX[5] method(){ }
            static XXX[5] method(){ }
        }
        """
        expect = str(Program([ClassDecl(Id("XXX"), [
            MethodDecl(Instance(), Id('method'), [], ArrayType(
                5, ClassType(Id('XXX'))), Block([], [])),
            MethodDecl(Static(), Id('method'), [], ArrayType(
                5, ClassType(Id('XXX'))), Block([], [])),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_83(self):
        input = """
        class XXX {
            float method(){ }
            static float method(){ }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [],
                       FloatType(), Block([], [])),
            MethodDecl(Static(), Id('method'), [], FloatType(), Block([], [])),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_84(self):
        input = """
        class XXX {
            boolean method(){ }
            static boolean method(){ }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [],
                       BoolType(), Block([], [])),
            MethodDecl(Static(), Id('method'), [], BoolType(), Block([], [])),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_85(self):
        input = """
        class XXX {
            string method(){ }
            static string method(){ }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [],
                       StringType(), Block([], [])),
            MethodDecl(Static(), Id('method'), [],
                       StringType(), Block([], [])),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_86(self):
        input = """
        class XXX {
            void method(){ }
            static void method(){ }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [],
                       VoidType(), Block([], [])),
            MethodDecl(Static(), Id('method'), [], VoidType(), Block([], [])),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_87(self):
        input = """
        class XXX {
            void method(){
                int x;
                float x;
                boolean x;
                string x;
                XXX x;
                int[0] x;
                float[0] x;
                boolean[0] x;
                string[0] x;
                XXX[0] x;
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], VoidType(), Block([
                VarDecl(Id('x'), IntType()),
                VarDecl(Id('x'), FloatType()),
                VarDecl(Id('x'), BoolType()),
                VarDecl(Id('x'), StringType()),
                VarDecl(Id('x'), ClassType(Id('XXX'))),
                VarDecl(Id('x'), ArrayType(0, IntType())),
                VarDecl(Id('x'), ArrayType(0, FloatType())),
                VarDecl(Id('x'), ArrayType(0, BoolType())),
                VarDecl(Id('x'), ArrayType(0, StringType())),
                VarDecl(Id('x'), ArrayType(0, ClassType(Id('XXX')))),
            ], [])),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_88(self):
        input = """
        class XXX {
            void method(){
                a := + b;
                a := - b;
                a := a + b;
                a := a - b;
                a := a * b;
                a := a / b;
                a := a \\ b;
                a := a % b;
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], VoidType(), Block([], [
                Assign(Id('a'), UnaryOp('+', Id('b'))),
                Assign(Id('a'), UnaryOp('-', Id('b'))),
                Assign(Id('a'), BinaryOp('+', Id('a'), Id('b'))),
                Assign(Id('a'), BinaryOp('-', Id('a'), Id('b'))),
                Assign(Id('a'), BinaryOp('*', Id('a'), Id('b'))),
                Assign(Id('a'), BinaryOp('/', Id('a'), Id('b'))),
                Assign(Id('a'), BinaryOp('\\', Id('a'), Id('b'))),
                Assign(Id('a'), BinaryOp('%', Id('a'), Id('b'))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_89(self):
        input = """
        class XXX {
            void method(){
                a := + - b;
                a := -a + -b;
                a := a * -b;
                a := +a \\ b;
                a := a % --b;
            }
        }
        """
        expect = str(Program([ClassDecl(Id('XXX'), [
            MethodDecl(Instance(), Id('method'), [], VoidType(), Block([], [
                Assign(Id('a'), UnaryOp('+', UnaryOp('-', Id('b')))),
                Assign(Id('a'), BinaryOp(
                    '+', UnaryOp('-', Id('a')), UnaryOp('-', Id('b')))),
                Assign(Id('a'), BinaryOp('*', Id('a'), UnaryOp('-', Id('b')))),
                Assign(Id('a'), BinaryOp('\\', UnaryOp('+', Id('a')), Id('b'))),
                Assign(Id('a'), BinaryOp('%', Id('a'),
                       UnaryOp('-', UnaryOp('-', Id('b'))))),
            ])),
        ])]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_vardecl_block_01(self):
        input = """class A {
            int main() {
                int a = 2,b;
                final A f = new A();
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(), Id("main"), [], IntType(), Block([
                VarDecl(Id("a"), IntType(), IntLiteral(2)),
                VarDecl(Id("b"), IntType()),
                ConstDecl(Id("f"), ClassType(Id("A")), NewExpr(Id("A"), []))
            ], []))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_for_09(self):
        input = """class A {
            int main() {
                for i := 0 to 10 do {
                    if i == f then
                        return i;
                    else f := !f;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [
                For(Id("i"), IntLiteral(0), IntLiteral(10), True,
                    Block([], [If(BinaryOp("==", Id("i"), Id("f")), Return(Id("i")), Assign(Id("f"), UnaryOp("!", Id("f"))))]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_block_01(self):
        input = """class A {
            int main() {
                final int a = 2;
                float b;
                b := a/2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(), Id("main"), [], IntType(), Block([
                ConstDecl(Id("a"), IntType(), IntLiteral(2)),
                VarDecl(Id("b"), FloatType())
            ], [
                Assign(Id("b"), BinaryOp("/", Id("a"), IntLiteral(2)))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_block_02(self):
        input = """class A {
            int main() {
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(), Id("main"), [], IntType(), Block([], []))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_block_03(self):
        input = """class A {
            int main() {
                {return a;}
                {return b;}
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [
                Block([], [Return(Id("a"))]),
                Block([], [Return(Id("b"))])
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_block_04(self):
        input = """class A {
            int main() {
                if a.check() then {
                    a := f;
                    return a / 2;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(), Id("main"), [], IntType(), Block([], [
                If(CallExpr(Id("a"), Id("check"), []), Block(
                    [], [Assign(Id("a"), Id("f")), Return(BinaryOp("/", Id("a"), IntLiteral(2)))]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_mix_02(self):
        input = """class A {
            void main() {
                int[5] arr;
                for i := 0 to 5 do {
                    int v;
                    v := os.get("int");
                    if v <= 0 then {
                        os.print("Error!!");
                        break;
                    }
                    arr[i] := v;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(), Id("main"), [], VoidType(), Block([
                VarDecl(Id("arr"), ArrayType(5, IntType()))
            ], [
                For(Id("i"), IntLiteral(0), IntLiteral(5), True, Block([VarDecl(Id("v"), IntType())], [
                    Assign(Id("v"), CallExpr(Id("os"), Id(
                        "get"), [StringLiteral('''"int"''')])),
                    If(BinaryOp("<=", Id("v"), IntLiteral(0)), Block([], [
                        CallStmt(Id("os"), Id("print"), [
                                 StringLiteral('''"Error!!"''')]),
                        Break()
                    ])),
                    Assign(ArrayCell(Id("arr"), Id("i")), Id("v"))
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_mix_03(self):
        input = """class A {
            int sum(int[5] arr) {
                int s = 0;
                for i := 0 to 5 do
                    s := s + arr[i];
                return s;
            }
            void main() {
                int[5] arr;
                for i := 0 to 5 do {
                    int v;
                    v := os.get("int");
                    if v <= 0 then {
                        os.print("Error!!");
                        break;
                    }
                    arr[i] := v;
                }
                os.print(this.sum(arr));
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            MethodDecl(Instance(), Id("sum"), [VarDecl(Id("arr"), ArrayType(5, IntType()))], IntType(), Block([
                VarDecl(Id("s"), IntType(), IntLiteral(0))
            ], [
                For(Id("i"), IntLiteral(0), IntLiteral(5), True, Assign(
                    Id("s"), BinaryOp("+", Id("s"), ArrayCell(Id("arr"), Id("i"))))),
                Return(Id("s"))
            ])),
            MethodDecl(Instance(), Id("main"), [], VoidType(), Block([VarDecl(Id("arr"), ArrayType(5, IntType()))], [
                For(Id("i"), IntLiteral(0), IntLiteral(5), True, Block([VarDecl(Id("v"), IntType())], [
                    Assign(Id("v"), CallExpr(Id("os"), Id(
                        "get"), [StringLiteral('''"int"''')])),
                    If(BinaryOp("<=", Id("v"), IntLiteral(0)), Block([], [
                        CallStmt(Id("os"), Id("print"), [
                                 StringLiteral('''"Error!!"''')]),
                        Break()
                    ])),
                    Assign(ArrayCell(Id("arr"), Id("i")), Id("v"))
                ])),
                CallStmt(Id("os"), Id("print"), [CallExpr(
                    SelfLiteral(), Id("sum"), [Id("arr")])])
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_mix_04(self):
        input = """class A {
            static A instance;
            A() {
                if instance == nil then
                    instance := this;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Static(), VarDecl(
                Id("instance"), ClassType(Id("A")))),
            MethodDecl(Instance(), Id("<init>"), [], None, Block([], [If(BinaryOp(
                "==", Id("instance"), NullLiteral()), Assign(Id("instance"), SelfLiteral()))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_mix_05(self):
        input = """class A {
            static A instance;
            A() {
                if instance == nil then
                    instance := this;
            }
            Text txt;
            static void Display(string str) {
                txt.text := str;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"), [
            AttributeDecl(Static(), VarDecl(
                Id("instance"), ClassType(Id("A")))),
            MethodDecl(Instance(), Id("<init>"), [], None, Block([], [If(BinaryOp(
                "==", Id("instance"), NullLiteral()), Assign(Id("instance"), SelfLiteral()))])),
            AttributeDecl(Instance(), VarDecl(
                Id("txt"), ClassType(Id("Text")))),
            MethodDecl(Static(), Id("Display"), [VarDecl(Id("str"), StringType())], VoidType(
            ), Block([], [Assign(FieldAccess(Id("txt"), Id("text")), Id("str"))]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_mix_06(self):
        input = """
        class makeSchool {
            void main() {
                for i:=true downto z-1 do {
                    string new_class;
                    io.fflush(stdin);
                    io.getline(new_class);
                    if new_class != "-1" then
                        School.updateClass(new_class);
                    else break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("makeSchool"), [
            MethodDecl(Instance(), Id("main"), [], VoidType(), Block([], [
                For(Id("i"), BooleanLiteral(True), BinaryOp("-", Id("z"), IntLiteral(1)), False, Block([
                    VarDecl(Id("new_class"), StringType())],
                    [
                    CallStmt(Id("io"), Id("fflush"), [Id("stdin")]),
                    CallStmt(Id("io"), Id("getline"), [Id("new_class")]),
                    If(BinaryOp("!=", Id("new_class"), StringLiteral('''"-1"''')),
                        CallStmt(Id("School"), Id("updateClass"), [Id("new_class")]), Break())
                ]))
            ]))
        ])]))
        self.assertTrue(TestAST.test(input, expect, 399))
