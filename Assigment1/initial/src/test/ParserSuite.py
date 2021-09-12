import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1(self):
        """Miss ) int main( {}"""
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2(self):
        """Miss ) int main( {}"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_complex_program3(self):
        """Test Complex Program """
        input = '''
        class Example1 {
    int factorial(int n){
    if n == 0 then return 1; else return n * this.factorial(n - 1);
    }
    void main(){
    int x;
    x := io.readInt();
    io.writeIntLn(this.factorial(x));
    }
    }
            '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_complex_program4(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_complex_program5(self):
        """Test Complex Program """
        input = '''
        class Rectangle extends Shape {
    float getArea(){
    return this.length*this.width;
    }
    }
            '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_complex_program6(self):
        """Test Complex Program """
        input = '''
    class Triangle extends Shape {
    float getArea(){
    return this.length*this.width / 2;
    }
    }
            '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_complex_program7(self):
        """Test Complex Program """
        input = '''
class Example2 {
void main(){
   s := new Rectangle(3,4);
}}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_complex_program8(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_complex_program9(self):
        """Test Complex Program """
        input = '''
class Example2 {
float nty(){
    b[3]:={2.3, 4.2, 102e3};
    a[3+x.foo(2)] := a[b[2]] +3;
}
}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_complex_program10(self):
        """Test Complex Program """
        input = '''
class Example2 {
    float nty(){
#start of declaration part
float r,s;
int[5] a,b;
#list of statements
r:=2.0;
s:=r*r*this.myPI;
a[0]:= s;
}
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_complex_program11(self):
        """Test Complex Program """
        input = '''
class Example2 {
    float nty(){
if flag then
r:=2.0;
else
a[0]:= s;
}
}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_complex_program12(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_complex_program13(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_complex_program14(self):
        """Test Complex Program """
        input = '''
/* class Person {

        string firstName; # property
        string lastName;  # property
        int age;          # property

        void fullname() {

        }
};*/
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_complex_program15(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_complex_program16(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_complex_program17(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_complex_program18(self):
        """Test Complex Program """
        input = '''
 class Test {

        int main(int[5] arg){}
        void goo ( float[5] x  ) {
    float[ 10 ] y ;
    float[ 10 ] x ;
    float[ 10 ] z ;
    a.foo( z ) ;
     a.foo( x ) ;
      a.foo( y ) ;
    return y;
}

}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_complex_program19(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 219))
# loi return boolean

    def test_complex_program20(self):
        """Test Complex Program """
        input = '''
 class Test {
    boolean swap(int a; int b)
{
    int tmp;
    tmp := a;
    a := b;
    b := tmp;
    Other.printf(a, b);
    # return true;
}
int main(){
    int a,b;
    boolean result;
    result := Test.swap(a,b);
    Other.print(result);
}

}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_complex_program21(self):
        """Test Complex Program """
        input = '''
 class Test {
     int a(int abc){}
        float a(int[5] a){}

}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_complex_program22(self):
        """Test Complex Program """
        input = '''
 class Test {
     int a(int abc){}
        float a(int[5] a){}

}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_complex_program23(self):
        """Test Complex Program """
        input = '''
 class Test {
    void a(){}
    string a(int a; int b; int c; float[1] d){}
    float a(int a, b, c){}

}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_complex_program24(self):
        """Test Complex Program """
        input = '''
 class Test {
    int float2int(float a){}
    int a(int[1] a; int b; string[5] c; string d){}
    float b(){}
    int c(string[7] c; int a; int b){}

}
        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 224))
############### invalid ##################

    def test_invalid_complex_program25(self):
        """Test Complex Program """
        input = '''
 class Test {
    int b(){}
    void c(int c){return c;}
    int d()

}

        '''
        expect = 'Error on line 7 col 0: }'
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_invalid_complex_program26(self):
        """Test Complex Program """
        input = '''
 class Test {
    int main(){}
    int main(int a; int[5] b){};
}

        '''
        expect = 'Error on line 4 col 31: ;'
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_invalid_complex_program27(self):
        """Test Complex Program """
        input = '''
 class Test {
      int a;
        float b;
        boolean c;
        string d

}

        '''
        expect = 'Error on line 8 col 0: }'
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_invalid_complex_program28(self):
        """Test Complex Program """
        input = '''
class Test {
    int a;
    void b;
}

        '''
        expect = 'Error on line 4 col 10: ;'
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_invalid_complex_program29(self):
        """Test Complex Program """
        input = '''
class Test {
    int a;
    float b;
    boolean[] c;
}

        '''
        expect = 'Error on line 5 col 12: ]'
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_invalid_complex_program30(self):
        """Test Complex Program """
        input = '''
class Test {
    void foo(int i){
            int child_foo(float f){}
        }
}

        '''
        expect = 'Error on line 4 col 25: ('
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_invalid_complex_program31(self):
        """Test Complex Program """
        input = '''
class Test {
    int main( {}
}

        '''
        expect = 'Error on line 3 col 14: {'
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_invalid_complex_program32(self):
        """Test Complex Program """
        input = '''
class Test {
    int main(){
            if abc then a=c
            else c=d;
        }
}

        '''
        expect = 'Error on line 4 col 25: ='
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_invalid_complex_program33(self):
        """Test Complex Program """
        input = '''
class Test {
    int main(){
             for true;(a);1 do {a=c;b=d;}{} while a;
        }
}

        '''
        expect = 'Error on line 4 col 17: true'
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_invalid_complex_program34(self):
        """Test Complex Program """
        input = '''
class Test {
    int main()
        {
            for i := 1- to 100 do {
                io.writeIntLn(i);
                Intarray[i] := i + 1;
            }
        }
}

        '''
        expect = 'Error on line 5 col 24: to'
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_invalid_complex_program35(self):
        """Test Complex Program """
        input = '''
class Test {
    private boolean check(TokenType type) {
            if (isAtEnd()) return false;
            return peek().type == type;
        }
}

        '''
        expect = 'Error on line 3 col 12: boolean'
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_invalid_complex_program36(self):
        """Test Complex Program """
        input = '''
class Test {
    int main(){
            int i;
            i := 1;
            for (i;i;i)
        }
}

        '''
        expect = 'Error on line 6 col 16: ('
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_invalid_complex_program37(self):
        """Test Complex Program """
        input = '''
class Test {
    void main() {
            else {
                #comment
            }
        }
}

        '''
        expect = 'Error on line 4 col 12: else'
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_invalid_complex_program38(self):
        """Test Complex Program """
        input = '''
class Test {
    void main() {
            if a==b then
                a:=1;
            else
                a:=2;
            else {

            }
        }
}

        '''
        expect = 'Error on line 8 col 12: else'
        self.assertTrue(TestParser.test(input, expect, 238))
# test phai loi {a==b} nhung lai success

    def test_invalid_complex_program39(self):
        """Test Complex Program """
        input = '''
class Test {
    void main() {
            if {a==b} then{
                a:=1;
            }
            else
                a:=2;
        }
}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_invalid_complex_program40(self):
        """Test Complex Program """
        input = '''
class Test {
    int main()
        {
            for [i=1;i>1;i+1]{}
        }
}

        '''
        expect = 'Error on line 5 col 16: ['
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_invalid_complex_program41(self):
        """Test Complex Program """
        input = '''
class Test {
    int main()
        {
            for {i=1;i>1;i+1}{}
        }
}

        '''
        expect = 'Error on line 5 col 16: {'
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_invalid_complex_program42(self):
        """Test Complex Program """
        input = '''
class Test {
        int main()
        {
            for (i=1;i>1;i+1 {}
        }
}

        '''
        expect = 'Error on line 5 col 16: ('
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_invalid_complex_program43(self):
        """Test Complex Program """
        input = '''
class Test {
        int main()
        {
            for i:=1 to 100 do {
                break
            }
        }
}

        '''
        expect = 'Error on line 7 col 12: }'
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_invalid_complex_program44(self):
        """Test Complex Program """
        input = '''
class Test {
        int main()
        {
            for i:=1 to 100 do {
                continue
            }
        }
}

        '''
        expect = 'Error on line 7 col 12: }'
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_invalid_complex_program45(self):
        """Test Complex Program """
        input = '''
class Test {
        int (){}
}

        '''
        expect = 'Error on line 3 col 12: ('
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_invalid_complex_program46(self):
        """Test Complex Program """
        input = '''
class Test {
       int mainTest(){};
}

        '''
        expect = 'Error on line 3 col 23: ;'
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_invalid_complex_program47(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            int a;
            a := continue + 1;
        };
}

        '''
        expect = 'Error on line 5 col 17: continue'
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_invalid_complex_program48(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            int a;
            a := int + 1;
        }
        int main(){
            int a;
            a := void + 1;
        }
}

        '''
        expect = 'Error on line 5 col 17: int'
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_invalid_complex_program49(self):
        """Test Complex Program """
        input = '''
class Test {
        int main ()
{
    a := !(a && b || c);
    e := a / b *c / (10 * c % d) && !(1) || (1) / 2;
    (b)[3] := a && b;
    !(b) := 3;
    b! := a || b;
}
}

        '''
        expect = 'Error on line 8 col 9: :='
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_invalid_complex_program50(self):
        """Test Complex Program """
        input = '''
class Test {
        int main ()
{
    int a;
    a := b[];
}
}

        '''
        expect = 'Error on line 6 col 11: ]'
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_invalid_complex_program51(self):
        """Test Complex Program """
        input = '''
class Test {
        int main ()
{
    int a;
    a := [2]b;
}
}

        '''
        expect = 'Error on line 6 col 9: ['
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_invalid_complex_program52(self):
        """Test Complex Program """
        input = '''
class Test {
        {}
}

        '''
        expect = 'Error on line 3 col 8: {'
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_invalid_complex_program53(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            {
                void main(){
                    return;
                }
            }
        }
}

        '''
        expect = 'Error on line 5 col 16: void'
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_invalid_complex_program54(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            call("alo")
        }
}

        '''
        expect = 'Error on line 4 col 16: ('
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_invalid_complex_program55(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            a.call("alo"};
        }
}

        '''
        expect = 'Error on line 4 col 24: }'
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_invalid_complex_program56(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            return boolean;
        }
}

        '''
        expect = 'Error on line 4 col 19: boolean'
        self.assertTrue(TestParser.test(input, expect, 256))
################# valid ###########

    def test_complex_program57(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_complex_program58(self):
        """Test Complex Program """
        input = '''
class Test {
        int main()
{
   int A, B, temp;

   Other.printf("Please enter the 1st number : ");
   Other.scanf("%d",A);
   Other.printf("\\nPlease enter the 2nd number : ");
   Other.scanf("%d",B);

   Other.printf("\\nBefore swapping:\\n");
   Other.printf("A - %d \\nB - %d", A, B);

   temp := A;
   A := B;
   B := temp;

   Other.printf("\\nAfter swapping:\\n");
   Other.printf("A - %d \\nB - %d", A, B);

   return 0;
}

}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_complex_program59(self):
        """Test Complex Program """
        input = '''
class Test {
        int main()
{
   int f1, f2, fib_ser, cnt, lmt;

   Other.printf("Please enter the limit of the Fibonacci series :");
   Other.scanf("%d",lmt);
   Other.printf("\\nFibonacci series is: \\n%d \\n%d \\n",f1,f2);
   fib_ser:=f1+f2;
    cnt := cnt + 1;
    Other.printf("%d\\n",fib_ser);
    f1:=f2;
    f2:=fib_ser;

   return 0;
}

}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_complex_program60(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_complex_program61(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_complex_program62(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            return 1+2;
        }

}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_complex_program63(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            return true;
        }

}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_complex_program64(self):
        """Test Complex Program """
        input = '''
class Test {
        int main(){
            return "abc"^"cde";
        }

}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_complex_program65(self):
        """Test Complex Program """
        input = '''
class Student {
     int id;  # truong hoac thanh vien du lieu
     float salary; # truong hoac thanh vien du lieu
     String name; #  truong hoac thanh vien du lieu
 }

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_complex_program66(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_complex_program67(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_complex_program68(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_complex_program69(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_complex_program70(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_complex_program71(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_complex_program72(self):
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
class Triangle extends Shape {
    float getArea(){
        return this.length*this.width / 2;
    }
}
class Example2 {
    void main(){
        s := new Rectangle(3,4);
        io.writeFloatLn(s.getArea());
        s := new Triangle(3,4);
        io.writeFloatLn(s.getArea());
    }
}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_complex_program73(self):
        """Test Complex Program """
        input = '''
class Parent {
    int p;
}
class Child extends Parent {
    int c;
}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_complex_program74(self):
        """Test Complex Program """
        input = '''
class Vehicle
{
    Vehicle()
    {
        io.writeFloatLn("This is a Vehicle");
    }
}

class FourWheeler
{
    FourWheeler()
    {
        io.writeFloatLn("This is a 4 wheeler Vehicle");
    }
}

class Car extends Vehicle, FourWheeler
{
}

        '''
        expect = 'Error on line 18 col 25: ,'
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_complex_program75(self):
        """Test Complex Program """
        input = '''
class Vehicle
{
    Vehicle()
    {
        io.writeFloatLn("This is a Vehicle");
    }
}

class FourWheeler extends Vehicle
{
    FourWheeler()
    {
        io.writeFloatLn("This is a 4 wheeler Vehicle");
    }
}

class Car extends FourWheeler
{
    Car()
    {
        io.writeFloatLn("This is a car");
    }
}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_complex_program76(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_complex_program76(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_complex_program77(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_complex_program77(self):
        """Test Complex Program """
        input = '''
class Vehicle
{
    Vehicle()
    {
        io.writeFloatLn("This is a Vehicle");
    }
}

class FourWheeler extends Vehicle
{
    FourWheeler()
    {
        io.writeFloatLn("This is a 4 wheeler Vehicle");
    }
}

class Car extends FourWheeler
{
    FourWheeler test= new FourWheeler();
    Car()
    {
        io.writeFloatLn("This is a car");
    }
}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_complex_program78(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_complex_program79(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_complex_program80(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_complex_program81(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_complex_program82(self):
        """Test Complex Program """
        input = '''
class Operator
{
    int main()
    {
        if flag then
            io.write("Expression is true");
        else
            io.write("Expression is false");
    }
}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_complex_program83(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_complex_program84(self):
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
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_complex_program85(self):
        """Test Complex Program """
        input = '''
class Operator
{
    int main()
    {
        RETURN 1;
    }
}

        '''
        expect = 'Error on line 6 col 15: 1'
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_complex_program86(self):
        """Test Complex Program """
        input = '''
class Operator
{
    int main()
    {
        return Other.print("this is result");
    }
}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_complex_program87(self):
        """Test Complex Program """
        input = '''
class Operator
{
    int main()
    {
        return Other.print("this is result").print1("this is result1").print2("this is result2");
    }
}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_complex_program88(self):
        """Test Complex Program """
        input = '''
class Vehicle extends Car
{
    Vehicle()
    {
        io.writeFloatLn("This is a Vehicle");
    }
}

class FourWheeler extends Vehicle
{
    FourWheeler()
    {
        io.writeFloatLn("This is a 4 wheeler Vehicle");
    }
}

class Car extends FourWheeler
{
    FourWheeler test= new FourWheeler();
    Car()
    {
        io.writeFloatLn("This is a car");
    }
}

        '''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_complex_program89(self):
        """Test Complex Program """
        input = '''
class Operator
{
    void main()
    {
        return ;
    }
}

        '''
        expect = 'Error on line 6 col 15: ;'
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_complex_program90(self):
        """Test Complex Program """
        input = '''
class Operator
{
    void main()
    {
        return && ;
    }
}

        '''
        expect = 'Error on line 6 col 15: &&'
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_complex_program91(self):
        """Test Complex Program """
        input = '''
class Operator
{
    void main()
    {
        return &&2 ;
    }
}

        '''
        expect = 'Error on line 6 col 15: &&'
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = """
        class Shape {
            float length,width;
            float getArea() {}
            Shape(float length,width){
                this.length := "length";
                this.width := width;
            }
        }
        class Rectangle extends Shape {
            float getArea(){
            return this.length*this.width;
            }
        }
        class Triangle extends Shape {
            float getArea(){
            return this.length*this.width / 2;
            }
        }
        class Example2 {
            void main(){
            s := new Rectangle(3,4);
            (b.coo().d.ass()).o();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = """
        class Shape {
            final static float length,width;
            static float getArea() {}
            Shape(float length,width){
                this.length := "length";
                this.width := width;
            }
        }
        class Rectangle extends Shape {
            float getArea(){
            return this.length*this.width;
            }
        }
        class Triangle extends Shape {
            float getArea(){
            return this.length*this.width / 2;
            }
        }
        class Example2 {
            void main(){
            s := new Rectangle(3,4);
            (b.coo().d.ass()).o();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = """
        class ID {
            static final int total=0;
            final static string name;
            ID(){
                this.name:=nil;
            }
            ID(string name){
                this.name:=name;
                ID.total := ID.total +1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = """
        class ID {
            static final int total=0;
            final static string name;
            final ID(){
                this.name:=nil;
            }
            ID(string name){
                this.name:=name;
                ID.total := ID.total +1;
            }
        }
        """
        expect = "Error on line 5 col 20: ("
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = """
        class ID extends object{
            static final int total=0;
            final static string name;
            final ID(){
                this.name:=nil;
            }
            ID(string name){
                this.name:=name;
                ID.total := ID.total +1;
            }
        }
        """
        expect = "Error on line 5 col 20: ("
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = """
        class array {
            int[4] element = { };
        }
        """
        expect = "Error on line 3 col 31: }"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = """
        class array {
            boolean main(){
                return true;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = """
        class array {
            boolean main(){
                return true&&false;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_100(self):
        input = """        class Shape {
            float length,width;
            float getArea() {}
            Shape(float length,width){
                this.length := "length";
                this.width := width;
            }
        }
        class Rectangle extends Shape {
            float getArea(){
            x.b[2] := x.m()[3];
            }
        }
        class Triangle extends Shape {
            float getArea(){
            return this.length*this.width / 2;
            }
        }
        class Example2 {
            void main(){
            s := new Rectangle(3,4);
            io.writeFloatLn(s.getArea());
            s := new Triangle(3,4);
            io.writeFloatLn(s.getArea());
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
