# import unittest
# from TestUtils import TestChecker
# from AST import *
import unittest
from main.bkool.utils.AST import *
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: int main() {} """
        input = """
            class A {}
            class B{}
            class A{}

        """
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_2(self):
        """Simple program: int main() {} """
        input = """
            class A {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                int numOfShape;
            }
        """
        expect = "Redeclared Attribute: numOfShape"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_temp2(self):
        input = Program([
            ClassDecl(Id('XXX'), [
                MethodDecl(Instance(), Id('x'), [], IntType(), Block([
                    ConstDecl(Id('x'), ArrayType(3, IntType()), ArrayLiteral(
                        [IntLiteral(1), IntLiteral(1), IntLiteral(1)]))
                ], [
                    Assign(Id('x'), ArrayLiteral(
                        [IntLiteral(1), IntLiteral(1), IntLiteral(1)]))
                ]))
            ], None)
        ])
        expect = "Cannot Assign To Constant: AssignStmt(Id(x),[IntLit(1),IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        """Simple program: int main() {} """
        input = """
            class A {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                int numOfShape(){}
            }
        """
        expect = "Redeclared Method: numOfShape"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        """Simple program: int main() {} """
        input = """
            class A {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                int test(int n; float n){}
            }
        """
        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5(self):
        """Simple program: int main() {} """
        input = """
            class A {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                int test(int n){
                    final int n = 5;
                }
            }
        """
        expect = "Redeclared Constant: n"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_6(self):
        """Simple program: int main() {} """
        input = """
            class A {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                int test(int n){
                    int n;
                }
            }
        """
        expect = "Redeclared Variable: n"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_7(self):
        """Simple program: int main() {} """
        input = """
            class A {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                int test(int n){
                    int a;
                    {
                        final int a = 5;
                        int a=6;
                    }
                }
            }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        """Simple program: int main() {} """
        input = """
            class B{}
            class A {
                C a ;

            }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_9(self):
        """Simple program: int main() {} """
        input = """
            class B{}
            class A {
                int foo(){
                    C test;
                }

            }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_10(self):
        """Simple program: int main() {} """
        input = """
            class B{}
            class A {
                int foo(){
                    {
                        {
                            {
                                {
                                    C test;
                                }
                            }
                        }
                    }
                }

            }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        """Simple program: int main() {} """
        input = """
            class B{}
            class A {
                int foo(){
                    final int a = 0;
                    a:=1;
                }

            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        """Simple program: int main() {} """
        input = """
            class B{}
            class A {
                int foo(){
                    B test;
                    test.access();
                }

            }
        """
        expect = "Undeclared Method: access"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        """Simple program: int main() {} """
        input = """
            class B{}
            class A {
                int foo(){
                    float a;
                    a:=5;
                }

            }
        """
        expect = "[None, None]"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_14(self):
        """Simple program: int main() {} """
        input = """
            class B{}
            class A {
                int foo(){
                    int a;
                    a:=5.1;
                }

            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),FloatLit(5.1))"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        """Simple program: int main() {} """
        input = """
            class B{}
            class A {
                final int a;
            }
        """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_16(self):
        """Simple program: int main() {} """
        input = """class A {} class A {}"""
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        """Simple program: int main() {} """
        input = """
            class B{
                int b;
            }
            class A extends B{
                int a;
                int foo(){
                    b:=1;
                }
            }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("a"), [], Id("b"))])
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Ex"), [AttributeDecl(
            Instance(), ConstDecl(Id("x"), IntType(), FloatLiteral(10.0)))])])
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,FloatLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Ex"), [AttributeDecl(Instance(), VarDecl(Id("x"), ArrayType(
            3, IntType()), ArrayLiteral([IntLiteral(2), FloatLiteral(1.2), NullLiteral()])))])])
        expect = "Illegal Array Literal: [IntLit(2),FloatLit(1.2),NullLiteral()]"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        """Simple program: int main() {} """
        input = """class A extends B{} class B{} class C extends A{} class C{}"""
        expect = "Redeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id("Ex"), [AttributeDecl(Static(), VarDecl(Id("a"), IntType())), AttributeDecl(
            Instance(), ConstDecl(Id("x"), IntType(), FieldAccess(Id("Ex"), Id("a"))))])])
        expect = "Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        """Simple program: int main() {} """
        input = """
            class B{}
            class A {
                int a;
                final int b = a+1;
            }
         """
        expect = "Illegal Constant Expression: BinaryOp(+,Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        """Simple program: int main() {} """
        input = """
            class B{
                string b="b";
            }
            class A extends B{
                final string a="test";
                string foo(){
                    string b=this.c;
                }
            }
         """
        expect = "Undeclared Attribute: c"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        """Simple program: int main() {} """
        input = """
            class B{
                final static string a="test";
            }
            class A extends B{
                string foo(){
                    B obj;
                    string a=obj.a;
                }
            }
         """
        expect = "Illegal Member Access: FieldAccess(Id(obj),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        """Simple program: int main() {} """
        input = """
            class A {
                int get(int a; float b) {}
            }
            class B extends A{
                B (){}
                int get;
            }
            class C {
                B b = new B();
                int get = b.get(1,1.5);
            }
         """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(get),[IntLit(1),FloatLit(1.5)])"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        """Simple program: int main() {} """
        input = """
            class a {
            int foo(){
                int x =y;
                int y;
            }
        }
         """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        """Simple program: int main() {} """
        input = """
            class A {
                int foo(){
                    return 1;
                }
            }
            class B extends A{
                A a = new A();
                int test(){
                    a.foo();
                }
            }
         """
        expect = "Type Mismatch In Statement: Call(Id(a),Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_28(self):
        """Simple program: int main() {} """
        input = """
            class A {
                int foo(){
                    return 7.8;
                }
            }
            class B extends A{
                A a = new A();
                int test(){
                    a.foo();
                }
            }
         """
        expect = "Type Mismatch In Statement: Return(FloatLit(7.8))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        """Simple program: int main() {} """
        input = """
            class A {

            }
            class B extends A{
                A a = new A();
                int test(){
                    int a;
                    int b=1;
                    if b then
                        a:=1;
                    else
                        a:=2;
                }
            }
         """
        expect = "Type Mismatch In Statement: If(Id(b),AssignStmt(Id(a),IntLit(1)),AssignStmt(Id(a),IntLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        """Simple program: int main() {} """
        input = """
            class A {
            }
            class B extends A{
                A a = new A();
                int test(){
                    int a=0;
                    A i;
                    for i := 1 to 100 do {
                        a:=a+1;
                    }
                }
            }
         """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),IntLit(100),True,Block([],[AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))])])"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        """Simple program: int main() {} """
        input = """
            class A {

            }
            class B extends A{
                int test(){
                    string[2] a;
                    a:={1,2};
                }
            }
         """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        """Simple program: int main() {} """
        input = """
            class A {

            }
            class B extends A{
                int test(){
                    float[2] a;
                    a:={1,2,3};
                }
            }
         """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        """Simple program: int main() {} """
        input = """
            class A {

            }
            class B extends A{
                int test(){
                    float[4] a={1,2,3,4};
                    int sum = 0;
                    int i;
                    for i := 0 to 3 do {
                        sum:=sum+a[i];
                    }
                    

                }
            }
         """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(sum),ArrayCell(Id(a),Id(i)))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_34(self):
        """Simple program: int main() {} """
        input = """
            class A {

            }
            class B extends A{
                int test(){
                    float[4] a={1.1,2.1,3.1,4.1};
                    float sum = 0;
                    int i;
                    for i := 0 to 3 do {
                        sum:="5"+a[i];
                    }
                }
            }
         """
        expect = """Type Mismatch In Expression: BinaryOp(+,StringLit("5"),ArrayCell(Id(a),Id(i)))"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        """Simple program: int main() {} """
        input = """
            class A {
                int value=5;
            }
            class B extends A{
                int test(){
                    int a=5;
                    A b=new A();
                    string c;
                    if a < b then
                        c:="a";
                    else
                        c:="b";
                }
            }
         """
        expect = """Type Mismatch In Expression: BinaryOp(<,Id(a),Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        """Simple program: int main() {} """
        input = """
            class B{
                static void test(int a;int b;int c){

                }
            }
            class A extends B{
                int foo(){
                    B.test(1.1,2,3);
                }
            }
         """
        expect = "Type Mismatch In Statement: Call(Id(B),Id(test),[FloatLit(1.1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """ class A{} class B extends A{} class C extends A{} class F{} class A extends F{}"""
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        input = """ class C {int a;static float a;}"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = """ class C {final int a;}"""
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        input = """ class C {final int a = 10;static final float a = 2.2;}"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        input = """ class C {A a;}"""
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """ class C {void a() {} static int a() {}}"""
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """ class C {int a;int a(){}}"""
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        input = """ class C {int a(){} int a;}"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        input = """ class C {C(){} C(int a) {}}"""
        expect = "Redeclared Method: <init>"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        input = """ class C {
            int main() { break;}
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        input = """ class C {
            int main() {
                int i;
                for i:=1 to 2 do
                break;
                continue;
            }
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_48(self):
        input = """ class C {
            int main() {
                int i;
                for i:=1 to 2 do {
                    if i == 1 then break;
                    else {continue;}
                    continue;
                    break;
                }
                continue;
            }
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_49(self):
        input = """ class C {
            int a = this.b;
        }"""
        expect = "Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        input = """ class C {
            int a;
            int b = this.a;
            int c = a;
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
        input = """ class C {
            static int a;
            int b = this.a;
        }"""
        expect = "Illegal Member Access: FieldAccess(Self(),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_52(self):
        input = """ class C {
            static int a;
            int b = !C.a;
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,FieldAccess(Id(C),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        input = """ class C {
            int a;
            int[5] b = this.a[5];
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(FieldAccess(Self(),Id(a)),IntLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_54(self):
        input = """ class C {}
        class A{
            C c = new C();
            C d = new C(1);
        }
        """
        expect = "Undeclared Method: <init>"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test55(self):
        input = """
        class XXX {
            int x() {
                boolean x = true && true;
                x := false || false;
                x := !true;
                x := 1 || false;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,IntLit(1),BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_56(self):
        input = """ class A{
            int foo(){
                final int b =b;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        input = """ class A{
            int m;
            int foo(){
                int n=m;
            }

        }
        """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_58(self):
        input = """ class A{
            int m;
            final int  n=this.m;

        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Self(),Id(m))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_59(self):
        input = """ class C {
            C (int a; float b) { }
            static int get() { }
            void getC() { }
        }
        class D extends C {
            int getC() { }
        }
        class A {
            C c = new D();
            int n = this.c.getC() + 1; # getC in D is int --> correct
            static C d = new C(1,1.3);
            int f = A.d.getC();    # getC in C is void --> incorrect because expr return type != void
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(FieldAccess(Self(),Id(c)),Id(getC),[])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_60(self):
        input = """ class C {
            static int get(){}
        }
        class A{
            C C = new C();
            int a = this.C.get();
        }
        """
        expect = "Illegal Member Access: CallExpr(FieldAccess(Self(),Id(C)),Id(get),[])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input = """ class C {
            final int a = 1;
            float b = 1;
            final float c = this.a;
            final float d = this.b;
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Self(),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_62(self):
        input = """ class C {
            final int a = 1;
            float b = 1;
            final float c = this.a;
            final float d = this.get(this.a,this.c);
            int get(int a; float b){}
        }
        """
        expect = "Illegal Constant Expression: CallExpr(Self(),Id(get),[FieldAccess(Self(),Id(a)),FieldAccess(Self(),Id(c))])"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_63(self):
        input = """ class C {
            static int a = 1;
        }
        class A {
            final int a = 1 + (1 + C.a);
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,IntLit(1),FieldAccess(Id(C),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_64(self):
        input = """ class C {
            int a;
            static int b;
            int main() {
                int b = this.a + C.b;
                int c = a;
            }
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_65(self):
        input = """ class C {
            int main() {
                int c = a;
                int a;
            }
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_66(self):
        input = """class A {
            int main(int a) {
                {
                    int a; # make new block to cover is ok.
                }
            }
        }
        class C {
            int main(int b) {
                int b;
            }
        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_67(self):
        input = """
        class C {
            int main(int b) {
                final int b = 5;
            }
        }"""
        expect = "Redeclared Constant: b"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test68(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                YYY z;
                final YYY y = z;
            }
        }
        class YYY {
            static final int x = 1;
            final int y = 1;
        }
        """
        expect = "Illegal Constant Expression: Id(z)"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_69(self):
        input = """
        class C {
            static int a;
            int b;
            int get() {}
        }
        class B extends C {
            C c = new C();
            int a = C.a;
            int get = this.c.get();
            int b = this.c.b;
            boolean f = 1 != true;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(!=,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        input = """
        class C {
            final int[5] a = {1, 2, 3, 4, 5};
        }"""
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_71(self):
        input = """
        class C {
            final int a = 1 + 2 - 3;
            final C c = new C();
        }"""
        expect = "Illegal Constant Expression: NewExpr(Id(C),[])"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_72(self):
        input = """
        class C {
            final int a = 5;
            int get() {}
            int main() {
                final int a = this.a + 1;
                final int c = this.get() + 1;
            }
        }"""
        expect = "Illegal Constant Expression: BinaryOp(+,CallExpr(Self(),Id(get),[]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_73(self):
        """Simple program: int main() {} """
        input = """
            class A {
                A(){}
            }
            class B extends A{
                A a = new A();
                int test(){
                    int a;
                    int b=1;
                    if b then
                        a:=1;
                    else
                        a:=2;
                }
            }
         """
        expect = "Type Mismatch In Statement: If(Id(b),AssignStmt(Id(a),IntLit(1)),AssignStmt(Id(a),IntLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_74(self):
        """Simple program: int main() {} """
        input = """
            class A {
                A(int a){}
            }
            class B{
                A b=new A("a");
            }

        """
        expect = """Type Mismatch In Expression: NewExpr(Id(A),[StringLit("a")])"""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test75(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := YYY.method4();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(YYY),Id(method4),[])"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test76(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := b.method3();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(method3),[])"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test77(self):
        input = """
        class XXX {
            int x() {
                float x = + 2;
                x := -2;
                x := +2.0;
                x := -2.0;
                x := 1 + 2;
                x := 1 + 2.0;
                x := 1.0 + 2.0;
                x := 1 - 2;
                x := 1 - 2.0;
                x := 1.0 - 2.0;
                x := 1 * 2;
                x := 1 * 2.0;
                x := 1.0 * 2.0;
                x := 1 / 2;
                x := 1 / 2.0;
                x := 1.0 / 2.0;

            }
        }
        """
        expect = "[None]"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test78(self):
        input = """
        class XXX {
            int x() {
                int y = 1 \\ 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(\,IntLit(1),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test79(self):
        input = """
        class XXX {
            int x() {
                int y = 1.0 \\ 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(\,FloatLit(1.0),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test80(self):
        input = """
        class XXX {
            int x() {
                int y = 1 % 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLit(1),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test81(self):
        input = """
        class XXX {
            int x() {
                int y = 1.0 % 2.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.0),FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test82(self):
        input = """
        class XXX {
            int x() {
                final int y = 1 / 2;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),IntType,BinaryOp(/,IntLit(1),IntLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test83(self):
        input = """
        class XXX {
            int x() {
                int y = 1 / true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test84(self):
        input = """
        class XXX {
            int x() {
                boolean x = true && true;
                x := false || false;
                x := !true;
                x := !1;
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test85(self):
        input = """
        class XXX {
            int x() {
                boolean x = true && true;
                x := false || false;
                x := !true;
                x := 1 || false;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,IntLit(1),BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test86(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 == 2;
                x := 1 != 2;
                x := true == false;
                x := true != false;
                x := 1.0 == 1.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.0),FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test87(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 == 2;
                x := 1 != 2;
                x := true == false;
                x := true != false;
                x := 1.0 == true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.0),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test88(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 == 2;
                x := 1 != 2;
                x := true == false;
                x := true != false;
                x := 1.0 != true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,FloatLit(1.0),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test89(self):
        input = """
        class XXX {
            int x() {
                boolean x = 1 > 2;
                x := 1.0 < 2;
                x := 1.0 <= 2.0;
                x := 1.0 <= true;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,FloatLit(1.0),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test90(self):
        input = """
        class XXX {
            int x() {
                string x = "aaa";
                x := x^"bbb";
                x := x^2;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(^,Id(x),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test91(self):
        input = """
        class XXX extends YYY {
            int x() {
                XXX a;
                XXX b;
                a.b := b.b;
                a.b := b.method4();
                a.b := YYY.a;
                a.b := YYY.method2();
                a.b := b.method3();
            }
        }
        class YYY {
            static int a;
            int b;
            static void method1() { }
            static int method2() { }
            void method3() { }
            int method4() { }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(method3),[])"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test92(self):
        input = """
        class XXX {
            int x() {
                int x;
                for x := 1 to 100 do {
                    continue;
                }
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test93(self):
        input = """
        class XXX {
            int x() {
                int x;
                for x := 1 to 100 do {
                    break;
                }
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test94(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                final XXX y = new XXX();
            }
        }
        """
        expect = "Illegal Constant Expression: NewExpr(Id(XXX),[])"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test95(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                final XXX z = this.a;
            }
        }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test96(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                int b;
                final int c = b+1;
            }
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,Id(b),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test97(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                final float y = YYY.x;
            }
        }
        class YYY {
            final int x = 1;
            final int y = 1;
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(YYY),Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test98(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                YYY z;
                final float y = z.y;
            }
        }
        class YYY {
            static final int x = 1;
            static final int y = 1;
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(z),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test99(self):
        input = """
        class XXX {
            int x() {
                final float a = 1.1;
                final float x = 1 + a;
                YYY z;
                final YYY y = z;
            }
        }
        class YYY {
            static final int x = 1;
            final int y = 1;
        }
        """
        expect = "Illegal Constant Expression: Id(z)"
        self.assertTrue(TestChecker.test(input, expect, 499))
