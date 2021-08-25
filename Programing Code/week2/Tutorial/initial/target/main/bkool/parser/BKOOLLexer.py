# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\6")
        buf.write("\n\67\n\n\r\n\16\n8\3\n\3\n\3\13\3\13\7\13?\n\13\f\13")
        buf.write("\16\13B\13\13\3\13\3\13\7\13F\n\13\f\13\16\13I\13\13\3")
        buf.write("\13\3\13\7\13M\n\13\f\13\16\13P\13\13\5\13R\n\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\2\2\17\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3")
        buf.write("\2\4\5\2\13\f\17\17\"\"\3\2))\2`\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\"\3")
        buf.write("\2\2\2\7&\3\2\2\2\t+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17")
        buf.write("\61\3\2\2\2\21\63\3\2\2\2\23\66\3\2\2\2\25<\3\2\2\2\27")
        buf.write("U\3\2\2\2\31X\3\2\2\2\33Z\3\2\2\2\35\36\7o\2\2\36\37\7")
        buf.write("c\2\2\37 \7k\2\2 !\7p\2\2!\4\3\2\2\2\"#\7k\2\2#$\7p\2")
        buf.write("\2$%\7v\2\2%\6\3\2\2\2&\'\7x\2\2\'(\7q\2\2()\7k\2\2)*")
        buf.write("\7f\2\2*\b\3\2\2\2+,\7*\2\2,\n\3\2\2\2-.\7+\2\2.\f\3\2")
        buf.write("\2\2/\60\7}\2\2\60\16\3\2\2\2\61\62\7\177\2\2\62\20\3")
        buf.write("\2\2\2\63\64\7=\2\2\64\22\3\2\2\2\65\67\t\2\2\2\66\65")
        buf.write("\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29:\3\2\2\2:")
        buf.write(";\b\n\2\2;\24\3\2\2\2<@\t\3\2\2=?\n\3\2\2>=\3\2\2\2?B")
        buf.write("\3\2\2\2@>\3\2\2\2@A\3\2\2\2AQ\3\2\2\2B@\3\2\2\2CG\t\3")
        buf.write("\2\2DF\n\3\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2")
        buf.write("HJ\3\2\2\2IG\3\2\2\2JN\t\3\2\2KM\n\3\2\2LK\3\2\2\2MP\3")
        buf.write("\2\2\2NL\3\2\2\2NO\3\2\2\2OR\3\2\2\2PN\3\2\2\2QC\3\2\2")
        buf.write("\2QR\3\2\2\2RS\3\2\2\2ST\t\3\2\2T\26\3\2\2\2UV\13\2\2")
        buf.write("\2VW\b\f\3\2W\30\3\2\2\2XY\13\2\2\2Y\32\3\2\2\2Z[\13\2")
        buf.write("\2\2[\34\3\2\2\2\b\28@GNQ\4\b\2\2\3\f\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    LB = 4
    RB = 5
    LP = 6
    RP = 7
    SEMI = 8
    WS = 9
    EX3 = 10
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "LB", "RB", "LP", "RP", "SEMI", "WS", 
            "EX3", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "LB", "RB", "LP", "RP", 
                  "SEMI", "WS", "EX3", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[10] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


