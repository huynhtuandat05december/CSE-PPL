import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
if not './main/bkool/parser/' in sys.path:
    sys.path.append('./main/bkool/parser/')
if os.path.isdir('../target/main/bkool/parser') and not '../target/main/bkool/parser/' in sys.path:
    sys.path.append('../target/main/bkool/parser/')
from BKOOLLexer import *
from BKOOLParser import *
from ASTGeneration import *
from StaticError import *
from CodeGenerator import CodeGenerator
import subprocess

JASMIN_JAR = "./external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
Lexer = BKOOLLexer
Parser = BKOOLParser


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestCodeGen():
    @staticmethod
    def test(input, expect, num):

        if type(input) is str:
            inputfile = TestUtil.makeSource(input, num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input

        TestCodeGen.check(SOL_DIR, asttree, num)

        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        codeGen = CodeGenerator()
        path = os.path.join(soldir, str(num))
        if not os.path.isdir(path):
            os.mkdir(path)
        f = open(os.path.join(soldir, str(num) + ".txt"), "w")
        try:
            codeGen.gen(asttree, path)

            subprocess.call("java  -jar " + JASMIN_JAR + " " + path +
                            "/*.j", shell=True, stderr=subprocess.STDOUT)

            subprocess.run("java -cp ./lib:. BKoolClass",
                           shell=True, stdout=f, timeout=10)
        except StaticError as e:
            f.write(str(e))
        except subprocess.TimeoutExpired:
            f.write("Time out\n")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(
                e.cmd, e.returncode, e.output))
        finally:
            f.close()
