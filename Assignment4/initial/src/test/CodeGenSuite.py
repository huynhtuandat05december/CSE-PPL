import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_bkool_int_ast(self):
        input = """class BKoolClass {static void main() {io.writeInt(1);}}"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_bkool_bin_ast(self):
        input = """class BKoolClass {static void main() {io.writeInt(1+3);}}"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_int_ast(self):
        input = Program([ClassDecl(Id("BKoolClass"),
                                   [MethodDecl(Static(), Id("main"), [], VoidType(),
                                               Block([], [CallStmt(Id("io"), Id("writeInt"), [IntLiteral(1)])]))])])
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_binary_ast(self):
        input = Program([ClassDecl(Id("BKoolClass"),
                                   [MethodDecl(Static(), Id("main"), [], VoidType(),
                                               Block([], [CallStmt(Id("io"), Id("writeInt"), [BinaryOp("+", IntLiteral(1), IntLiteral(3))])]))])])
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_4(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static final string b="abc";
            static final boolean c=false;
            static void main() {
                final boolean d=true;
                io.writeFloat(-this.a);
                io.writeStr(this.b);
                io.writeBool(!c);
                io.writeBool(!d);
            }
        }
        """
        expect = """-1.0abctruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_5(self):
        input = """class BKoolClass {
            static void main() {
                final int a=2;
                io.writeInt(a);
            }
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_6(self):
        input = """class BKoolClass {
            static void main() {
                int a=4;
                io.writeInt(a);
            }
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_7(self):
        input = """class BKoolClass {
            static final int a=5;
            static void main() {
                io.writeInt(this.a);
            }
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_8(self):
        input = """class BKoolClass {
            static void main() {
                final float a=4.1;
                io.writeFloat(a);
            }
        }
        """
        expect = "4.1"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_9(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                io.writeFloat(this.a);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_10(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static final string b="abc";
            static final boolean c=false;
            static void main() {
                final boolean d=true;
                io.writeFloat(this.a);
                io.writeStr(this.b);
                io.writeBool(c);
                io.writeBool(d);
            }
        }
        """
        expect = """1.0abcfalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_11(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a+b);

            }
        }
        """
        expect = """3.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_12(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a-b);

            }
        }
        """
        expect = """-1.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_13(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a*b);

            }
        }
        """
        expect = """2.75"""
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_14(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a/b);

            }
        }
        """
        expect = """0.44"""
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_15(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a/b);

            }
        }
        """
        expect = """0.44"""
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_16(self):
        input = """class BKoolClass {
            static final int a=7;
            static void main() {
                int b=3;
                io.writeInt(this.a \\ b);
                # io.writeInt(this.a % b);

            }
        }
        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_17(self):
        input = """class BKoolClass {
            static final boolean a=true;
            static void main() {
                boolean b=true;
                io.writeBool(this.a && b);
                io.writeBool(this.a);
                io.writeBool(b);
            }
        }
        """
        expect = """truetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_18(self):
        input = """class BKoolClass {
            static final boolean a=true;
            static final int b=7;
            static void main() {
                io.writeBool(this.a);
                io.writeInt(this.b);
                io.writeBool(true);
            }
        }
        """
        expect = """true7true"""
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_19(self):
        input = """class BKoolClass {
            static final int a=5;
            static final int b=7;
            static void main() {
                io.writeBool(this.a > this.b);
                io.writeBool(this.a >= this.b);
                io.writeBool(this.a < this.b);
                io.writeBool(this.a <= this.b);
                io.writeBool(this.a == this.b);
                io.writeBool(this.a != this.b);

            }
        }
        """
        expect = """falsefalsetruetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 519))
    def test_20(self):
        input = """class BKoolClass {
            static final string a="hello";
            static final string b=" world";
            static void main() {
                io.writeStr(a^b);

            }
        }
        """
        expect = """hello world"""
        self.assertTrue(TestCodeGen.test(input, expect, 520))
    def test_21(self):
        input = """class BKoolClass {
            static final string a="hello";
            static final string b=" world!";
            static void main() {
                io.writeStr(a^b);

            }
        }
        """
        expect = """hello world!"""
        self.assertTrue(TestCodeGen.test(input, expect, 521))
    def test_22(self):
        input = """class BKoolClass {
            void main(){
                boolean flag=true;
                if flag then
                    io.writeStr("Expression is true");
                else
                    io.writeStr("Expression is false");
            }
        }
        """
        expect = """Expression is true"""
        self.assertTrue(TestCodeGen.test(input, expect, 522))
    def test_23(self):
        input = """class BKoolClass {
            void main(){
               int a;
               a:=5;
               io.writeInt(a);
            }
        }
        """
        expect = """5"""
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_24(self):
        input = """class BKoolClass {
            void main(){
               int a;
               float b;
               string c;
               boolean d;
               a:=5;
               b:=5.1;
               c:="abc";
               d:=true;
               io.writeInt(a);
               io.writeFloat(b);
               io.writeStr(c);
               io.writeBool(d);
            }
        }
        """
        expect = """55.1abctrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 524))
    def test_25(self):
        input = """class BKoolClass {
            void main(){
               int a;
               float b;
               string c;
               boolean d;
               a:=5;
               b:=5.1;
               c:="abc";
               d:=true;
               io.writeInt(a);
               io.writeFloat(b);
               io.writeStr(c);
               io.writeBool(d);
            }
        }
        """
        expect = """55.1abctrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 524))
    
    def test_26(self):
        input = """
         class BKoolClass {
            static void main() { int x = 1; io.writeInt(x);}
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 526))
    def test_27(self):
        input = """
         class BKoolClass {
            static void main() { 
                int x = 2;
                x:=x+1; 
                io.writeInt(x);
            }
        }
        """
        expect = """3"""
        self.assertTrue(TestCodeGen.test(input, expect, 527))



    def test_28(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static final string b="abc";
            static final boolean c=false;
            static void main() {
                final boolean d=true;
                io.writeFloat(-this.a+this.a);
                io.writeStr(this.b);
                io.writeBool(!c);
                io.writeBool(!d);
            }
        }
        """
        expect = """0.0abctruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_29(self):
        input = """class BKoolClass {
            static void main() {
                final float a=2.0;
                io.writeFloat(a);
            }
        }
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_30(self):
        input = """class BKoolClass {
            static void main() {
                int a=4;
                io.writeInt(a);
            }
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_31(self):
        input = """class BKoolClass {
            static final int a=5;
            static void main() {
                io.writeInt(this.a);
            }
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_32(self):
        input = """class BKoolClass {
            static void main() {
                final int a=4;
                int b=2;
                io.writeInt(a*b);
            }
        }
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_33(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                io.writeFloat(this.a);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_34(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static final string b="abc";
            static final boolean c=false;
            static void main() {
                final boolean d=true;
                io.writeFloat(this.a);
                io.writeStr(this.b);
                io.writeBool(c);
                io.writeBool(d);
            }
        }
        """
        expect = """1.0abcfalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_35(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a+b);

            }
        }
        """
        expect = """3.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_36(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a-b-b);

            }
        }
        """
        expect = """-4.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_37(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a*b);

            }
        }
        """
        expect = """2.75"""
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_38(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(-(this.a/b));

            }
        }
        """
        expect = """-0.44"""
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_39(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a/b);

            }
        }
        """
        expect = """0.44"""
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_40(self):
        input = """class BKoolClass {
            static final int a=7;
            static void main() {
                int b=3;
                io.writeInt(this.a \\ b);
                # io.writeInt(this.a % b);

            }
        }
        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_41(self):
        input = """class BKoolClass {
            static final boolean a=true;
            static void main() {
                boolean b=true;
                io.writeBool(this.a && b && true);
                io.writeBool(this.a);
                io.writeBool(b);
            }
        }
        """
        expect = """truetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_42(self):
        input = """class BKoolClass {
            static final boolean a=true;
            static final int b=7;
            static void main() {
                io.writeBool(this.a);
                io.writeInt(this.b);
                io.writeBool(true);
            }
        }
        """
        expect = """true7true"""
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_43(self):
        input = """class BKoolClass {
            static final int a=5;
            static final int b=7;
            static void main() {
                io.writeBool(this.a > this.b);
                io.writeBool(this.a >= this.b);
                io.writeBool(this.a < this.b);
                io.writeBool(this.a <= this.b);
                io.writeBool(this.a == this.b);
                io.writeBool(this.a != this.b);

            }
        }
        """
        expect = """falsefalsetruetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 543))
    def test_44(self):
        input = """class BKoolClass {
            static final string a="hello";
            static final string b=" world";
            static final string c=" world";
            static void main() {
                io.writeStr((a^b)^c);

            }
        }
        """
        expect = """hello world world"""
        self.assertTrue(TestCodeGen.test(input, expect, 544))
    def test_45(self):
        input = """class BKoolClass {
            static final string a="hello";
            static final string b=" world!";
            static void main() {
                io.writeStr(a^b);

            }
        }
        """
        expect = """hello world!"""
        self.assertTrue(TestCodeGen.test(input, expect, 545))
    def test_46(self):
        input = """class BKoolClass {
            void main(){
                boolean flag=true;
                if flag then
                    io.writeStr("Expression is true");
                else
                    io.writeStr("Expression is false");
            }
        }
        """
        expect = """Expression is true"""
        self.assertTrue(TestCodeGen.test(input, expect, 546))
    def test_47(self):
        input = """class BKoolClass {
            void main(){
               int a;
               a:=5;
               io.writeInt(a+1);
            }
        }
        """
        expect = """6"""
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_48(self):
        input = """class BKoolClass {
            void main(){
               int a;
               float b;
               string c;
               boolean d;
               a:=5;
               b:=5.1;
               c:="abc";
               d:=true;
               io.writeInt(a);
               io.writeFloat(b);
               io.writeStr(c);
               io.writeBool(d);
            }
        }
        """
        expect = """55.1abctrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 548))
    
    def test_49(self):
        input = """
         class BKoolClass {
            static void main() { int x = 1; io.writeInt(x);}
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 549))
    def test_50(self):
        input = """
         class BKoolClass {
            static void main() { 
                int x = 2;
                x:=x+1; 
                io.writeInt(x);
            }
        }
        """
        expect = """3"""
        self.assertTrue(TestCodeGen.test(input, expect, 550))
   
    def test_51(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static final string b="abc";
            static final boolean c=false;
            static void main() {
                final boolean d=true;
                io.writeFloat(-this.a);
                io.writeStr(this.b);
                io.writeBool(!c);
                io.writeBool(!d);
            }
        }
        """
        expect = """-1.0abctruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_52(self):
        input = """class BKoolClass {
            static void main() {
                final int a=2;
                io.writeInt(a);
            }
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_53(self):
        input = """class BKoolClass {
            static void main() {
                int a=4;
                io.writeInt(a);
            }
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_54(self):
        input = """class BKoolClass {
            static final int a=5;
            static void main() {
                io.writeInt(this.a);
            }
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_55(self):
        input = """class BKoolClass {
            static void main() {
                final float a=4.1;
                io.writeFloat(a);
            }
        }
        """
        expect = "4.1"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_56(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                io.writeFloat(this.a);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_57(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static final string b="abc";
            static final boolean c=false;
            static void main() {
                final boolean d=true;
                io.writeFloat(this.a);
                io.writeStr(this.b);
                io.writeBool(c);
                io.writeBool(d);
            }
        }
        """
        expect = """1.0abcfalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_58(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a+b);

            }
        }
        """
        expect = """3.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_59(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a-b);

            }
        }
        """
        expect = """-1.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_60(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a*b);

            }
        }
        """
        expect = """2.75"""
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_61(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a/b);

            }
        }
        """
        expect = """0.44"""
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_62(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a/b);

            }
        }
        """
        expect = """0.44"""
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_63(self):
        input = """class BKoolClass {
            static final int a=7;
            static void main() {
                int b=3;
                io.writeInt(this.a \\ b);
                # io.writeInt(this.a % b);

            }
        }
        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_64(self):
        input = """class BKoolClass {
            static final boolean a=true;
            static void main() {
                boolean b=true;
                io.writeBool(this.a && b);
                io.writeBool(this.a);
                io.writeBool(b);
            }
        }
        """
        expect = """truetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_65(self):
        input = """class BKoolClass {
            static final boolean a=true;
            static final int b=7;
            static void main() {
                io.writeBool(this.a);
                io.writeInt(this.b);
                io.writeBool(true);
            }
        }
        """
        expect = """true7true"""
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_66(self):
        input = """class BKoolClass {
            static final int a=5;
            static final int b=7;
            static void main() {
                io.writeBool(this.a > this.b);
                io.writeBool(this.a >= this.b);
                io.writeBool(this.a < this.b);
                io.writeBool(this.a <= this.b);
                io.writeBool(this.a == this.b);
                io.writeBool(this.a != this.b);

            }
        }
        """
        expect = """falsefalsetruetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 566))
    def test_67(self):
        input = """class BKoolClass {
            static final string a="hello";
            static final string b=" world";
            static void main() {
                io.writeStr(a^b);

            }
        }
        """
        expect = """hello world"""
        self.assertTrue(TestCodeGen.test(input, expect, 567))
    def test_68(self):
        input = """class BKoolClass {
            static final string a="hello";
            static final string b=" world!";
            static void main() {
                io.writeStr(a^b);

            }
        }
        """
        expect = """hello world!"""
        self.assertTrue(TestCodeGen.test(input, expect, 568))
    def test_69(self):
        input = """class BKoolClass {
            void main(){
                boolean flag=true;
                if flag then
                    io.writeStr("Expression is true");
                else
                    io.writeStr("Expression is false");
            }
        }
        """
        expect = """Expression is true"""
        self.assertTrue(TestCodeGen.test(input, expect, 569))
    def test_70(self):
        input = """class BKoolClass {
            void main(){
               int a;
               a:=5;
               io.writeInt(a);
            }
        }
        """
        expect = """5"""
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_71(self):
        input = """class BKoolClass {
            void main(){
               int a;
               float b;
               string c;
               boolean d;
               a:=5;
               b:=5.1;
               c:="abc";
               d:=true;
               io.writeInt(a);
               io.writeFloat(b);
               io.writeStr(c);
               io.writeBool(d);
            }
        }
        """
        expect = """55.1abctrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 571))
    def test_72(self):
        input = """
         class BKoolClass {
            static void main() { int x = 1; io.writeInt(x);}
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 573))
    
    def test_73(self):
        input = """
         class BKoolClass {
            static void main() { int x = 1; io.writeInt(x);}
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 573))
    def test_74(self):
        input = """
         class BKoolClass {
            static void main() { 
                int x = 2;
                x:=x+1; 
                io.writeInt(x);
            }
        }
        """
        expect = """3"""
        self.assertTrue(TestCodeGen.test(input, expect, 574))



    def test_75(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static final string b="abc";
            static final boolean c=false;
            static void main() {
                final boolean d=true;
                io.writeFloat(-this.a+this.a);
                io.writeStr(this.b);
                io.writeBool(!c);
                io.writeBool(!d);
            }
        }
        """
        expect = """0.0abctruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_76(self):
        input = """class BKoolClass {
            static void main() {
                final float a=2.0;
                io.writeFloat(a);
            }
        }
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_77(self):
        input = """class BKoolClass {
            static void main() {
                int a=4;
                io.writeInt(a);
            }
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_78(self):
        input = """class BKoolClass {
            static final int a=5;
            static void main() {
                io.writeInt(this.a);
            }
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_79(self):
        input = """class BKoolClass {
            static void main() {
                final int a=4;
                int b=2;
                io.writeInt(a*b);
            }
        }
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_80(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                io.writeFloat(this.a);
            }
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_81(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static final string b="abc";
            static final boolean c=false;
            static void main() {
                final boolean d=true;
                io.writeFloat(this.a);
                io.writeStr(this.b);
                io.writeBool(c);
                io.writeBool(d);
            }
        }
        """
        expect = """1.0abcfalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_82(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a+b);

            }
        }
        """
        expect = """3.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_83(self):
        input = """class BKoolClass {
            static final float a=1.0;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a-b-b);

            }
        }
        """
        expect = """-4.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_84(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a*b);

            }
        }
        """
        expect = """2.75"""
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_85(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(-(this.a/b));

            }
        }
        """
        expect = """-0.44"""
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_86(self):
        input = """class BKoolClass {
            static final float a=1.1;
            static void main() {
                float b=2.5;
                io.writeFloat(this.a/b);

            }
        }
        """
        expect = """0.44"""
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_87(self):
        input = """class BKoolClass {
            static final int a=7;
            static void main() {
                int b=3;
                io.writeInt(this.a \\ b);
                # io.writeInt(this.a % b);

            }
        }
        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_88(self):
        input = """class BKoolClass {
            static final boolean a=true;
            static void main() {
                boolean b=true;
                io.writeBool(this.a && b && true);
                io.writeBool(this.a);
                io.writeBool(b);
            }
        }
        """
        expect = """truetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_89(self):
        input = """class BKoolClass {
            static final boolean a=true;
            static final int b=7;
            static void main() {
                io.writeBool(this.a);
                io.writeInt(this.b);
                io.writeBool(true);
            }
        }
        """
        expect = """true7true"""
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_90(self):
        input = """class BKoolClass {
            static final int a=5;
            static final int b=7;
            static void main() {
                io.writeBool(this.a > this.b);
                io.writeBool(this.a >= this.b);
                io.writeBool(this.a < this.b);
                io.writeBool(this.a <= this.b);
                io.writeBool(this.a == this.b);
                io.writeBool(this.a != this.b);

            }
        }
        """
        expect = """falsefalsetruetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 590))
    def test_91(self):
        input = """class BKoolClass {
            static final string a="hello";
            static final string b=" world";
            static final string c=" world";
            static void main() {
                io.writeStr((a^b)^c);

            }
        }
        """
        expect = """hello world world"""
        self.assertTrue(TestCodeGen.test(input, expect, 591))
    def test_92(self):
        input = """class BKoolClass {
            static final string a="hello";
            static final string b=" world!";
            static void main() {
                io.writeStr(a^b);

            }
        }
        """
        expect = """hello world!"""
        self.assertTrue(TestCodeGen.test(input, expect, 592))
    def test_93(self):
        input = """class BKoolClass {
            void main(){
                boolean flag=true;
                if flag then
                    io.writeStr("Expression is true");
                else
                    io.writeStr("Expression is false");
            }
        }
        """
        expect = """Expression is true"""
        self.assertTrue(TestCodeGen.test(input, expect, 593))
    def test_94(self):
        input = """class BKoolClass {
            void main(){
               int a;
               a:=5;
               io.writeInt(a+1);
            }
        }
        """
        expect = """6"""
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_95(self):
        input = """class BKoolClass {
            void main(){
               int a;
               float b;
               string c;
               boolean d;
               a:=5;
               b:=5.1;
               c:="abc";
               d:=true;
               io.writeInt(a);
               io.writeFloat(b);
               io.writeStr(c);
               io.writeBool(d);
            }
        }
        """
        expect = """55.1abctrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 595))
    
    def test_96(self):
        input = """
         class BKoolClass {
            static void main() { int x = 1; io.writeInt(x);}
            }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 596))
    def test_97(self):
        input = """
         class BKoolClass {
            static void main() { 
                int x = 2;
                x:=x+1; 
                io.writeInt(x);
            }
        }
        """
        expect = """3"""
        self.assertTrue(TestCodeGen.test(input, expect, 597))   
    def test_99(self):
        input = """class BKoolClass {
            static final int a=5;
            static final int b=7;
            static void main() {
                io.writeBool(this.a > this.b);
                io.writeBool(this.a >= this.b);
                io.writeBool(this.a < this.b);
                io.writeBool(this.a <= this.b);
                io.writeBool(this.a == this.b);
                io.writeBool(this.a != this.b);

            }
        }
        """
        expect = """falsefalsetruetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 599))
    def test_98(self):
        input = """class BKoolClass {
            static final string a="hello";
            static final string b=" world";
            static final string c=" world";
            static void main() {
                io.writeStr((a^b)^c);

            }
        }
        """
        expect = """hello world world"""
        self.assertTrue(TestCodeGen.test(input, expect, 598))
    