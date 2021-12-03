import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_bkool_int_ast(self):
    #     input = """class BKoolClass {static void main() {io.writeInt(1);}}"""
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 500))

    # def test_bkool_bin_ast(self):
    #     input = """class BKoolClass {static void main() {io.writeInt(1+3);}}"""
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))

    # def test_int_ast(self):
    #     input = Program([ClassDecl(Id("BKoolClass"),
    #                                [MethodDecl(Static(), Id("main"), [], VoidType(),
    #                                            Block([], [CallStmt(Id("io"), Id("writeInt"), [IntLiteral(1)])]))])])
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))

    # def test_binary_ast(self):
    #     input = Program([ClassDecl(Id("BKoolClass"),
    #                                [MethodDecl(Static(), Id("main"), [], VoidType(),
    #                                            Block([], [CallStmt(Id("io"), Id("writeInt"), [BinaryOp("+", IntLiteral(1), IntLiteral(3))])]))])])
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))

    # def test_4(self):
    #     input = """class BKoolClass {
    #         static final float a=1.0;
    #         static final string b="abc";
    #         static final boolean c=false;
    #         static void main() {
    #             final boolean d=true;
    #             io.writeFloat(-this.a);
    #             io.writeStr(this.b);
    #             io.writeBool(!c);
    #             io.writeBool(!d);
    #         }
    #     }
    #     """
    #     expect = """-1.0abctruefalse"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))

    # def test_5(self):
    #     input = """class BKoolClass {
    #         static void main() {
    #             final int a=2;
    #             io.writeInt(a);
    #         }
    #     }
    #     """
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))

    # def test_6(self):
    #     input = """class BKoolClass {
    #         static void main() {
    #             int a=4;
    #             io.writeInt(a);
    #         }
    #     }
    #     """
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))

    # def test_7(self):
    #     input = """class BKoolClass {
    #         static final int a=5;
    #         static void main() {
    #             io.writeInt(this.a);
    #         }
    #     }
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))

    # def test_8(self):
    #     input = """class BKoolClass {
    #         static void main() {
    #             final float a=4.1;
    #             io.writeFloat(a);
    #         }
    #     }
    #     """
    #     expect = "4.1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))

    # def test_9(self):
    #     input = """class BKoolClass {
    #         static final float a=1.0;
    #         static void main() {
    #             io.writeFloat(this.a);
    #         }
    #     }
    #     """
    #     expect = "1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))

    # def test_10(self):
    #     input = """class BKoolClass {
    #         static final float a=1.0;
    #         static final string b="abc";
    #         static final boolean c=false;
    #         static void main() {
    #             final boolean d=true;
    #             io.writeFloat(this.a);
    #             io.writeStr(this.b);
    #             io.writeBool(c);
    #             io.writeBool(d);
    #         }
    #     }
    #     """
    #     expect = """1.0abcfalsetrue"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))

    # def test_11(self):
    #     input = """class BKoolClass {
    #         static final float a=1.0;
    #         static void main() {
    #             float b=2.5;
    #             io.writeFloat(this.a+b);

    #         }
    #     }
    #     """
    #     expect = """3.5"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))

    # def test_12(self):
    #     input = """class BKoolClass {
    #         static final float a=1.0;
    #         static void main() {
    #             float b=2.5;
    #             io.writeFloat(this.a-b);

    #         }
    #     }
    #     """
    #     expect = """-1.5"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))

    # def test_13(self):
    #     input = """class BKoolClass {
    #         static final float a=1.1;
    #         static void main() {
    #             float b=2.5;
    #             io.writeFloat(this.a*b);

    #         }
    #     }
    #     """
    #     expect = """2.75"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))

    # def test_14(self):
    #     input = """class BKoolClass {
    #         static final float a=1.1;
    #         static void main() {
    #             float b=2.5;
    #             io.writeFloat(this.a/b);

    #         }
    #     }
    #     """
    #     expect = """0.44"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))

    # def test_15(self):
    #     input = """class BKoolClass {
    #         static final float a=1.1;
    #         static void main() {
    #             float b=2.5;
    #             io.writeFloat(this.a/b);

    #         }
    #     }
    #     """
    #     expect = """0.44"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))

    # def test_16(self):
    #     input = """class BKoolClass {
    #         static final int a=7;
    #         static void main() {
    #             int b=3;
    #             io.writeInt(this.a \\ b);
    #             # io.writeInt(this.a % b);

    #         }
    #     }
    #     """
    #     expect = """2"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))

    # def test_17(self):
    #     input = """class BKoolClass {
    #         static final boolean a=true;
    #         static void main() {
    #             boolean b=true;
    #             io.writeBool(this.a && b);
    #             io.writeBool(this.a);
    #             io.writeBool(b);
    #         }
    #     }
    #     """
    #     expect = """truetruetrue"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))

    # def test_18(self):
    #     input = """class BKoolClass {
    #         static final boolean a=true;
    #         static final int b=7;
    #         static void main() {
    #             io.writeBool(this.a);
    #             io.writeInt(this.b);
    #             io.writeBool(true);
    #         }
    #     }
    #     """
    #     expect = """true7true"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))

    # def test_19(self):
    #     input = """class BKoolClass {
    #         static final int a=5;
    #         static final int b=7;
    #         static void main() {
    #             io.writeBool(this.a > this.b);
    #             io.writeBool(this.a >= this.b);
    #             io.writeBool(this.a < this.b);
    #             io.writeBool(this.a <= this.b);
    #             io.writeBool(this.a == this.b);
    #             io.writeBool(this.a != this.b);

    #         }
    #     }
    #     """
    #     expect = """falsefalsetruetruefalsetrue"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))
    # def test_20(self):
    #     input = """class BKoolClass {
    #         static final string a="hello";
    #         static final string b=" world";
    #         static void main() {
    #             io.writeStr(a^b);

    #         }
    #     }
    #     """
    #     expect = """hello world"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))
    # def test_21(self):
    #     input = """class BKoolClass {
    #         int factorial(int n){
    #             if n == 0 then return 1; else return n * this.factorial(n - 1);
    #         }
    #         void main(){
    #             int x;
    #             x := io.readInt();
    #             io.writeIntLn(this.factorial(x));
    #         }
    #     }
    #     """
    #     expect = """hello world"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))
    # def test_21(self):
    #     input = """class BKoolClass {
    #         void main(){
    #             boolean flag=true;
    #             if flag then
    #                 io.writeStrLn("Expression is true");
    #             else
    #                 io.writeStrLn("Expression is false");
    #         }
    #     }
    #     """
    #     expect = """hello world"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))
    # def test_22(self):
    #     input = """class BKoolClass {
    #         void main(){
    #            int a;
    #            a:=5;
    #            io.writeInt(a);
    #         }
    #     }
    #     """
    #     expect = """5"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))

    # def test_23(self):
    #     input = """class BKoolClass {
    #         void main(){
    #            int a;
    #            float b;
    #            string c;
    #            boolean d;
    #            a:=5;
    #            b:=5.1;
    #            c:="abc";
    #            d:=true;
    #            io.writeInt(a);
    #            io.writeFloat(b);
    #            io.writeStr(c);
    #            io.writeBool(d);
    #         }
    #     }
    #     """
    #     expect = """55.1abctrue"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))
    # def test_24(self):
    #     input = """
    #     class A{
    #         final int a=1;
    #     }
    #     class BKoolClass {
    #         void main(){
    #            A test= new A();
    #            io.writeInt(test.a);
    #         }
    #     }
    #     """
    #     expect = """1"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))
    def test_25(self):
        input = """
        class A{
            int a;
        }
        class BKoolClass {
            void main(){
               A test;
               test:= new A();
               test.a:=1;
               io.writeInt(test.a);
            }
        }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 525))
