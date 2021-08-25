# Generated from /home/tuandat/vscode/PPL/Programing Code/week2/Tutorial/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("A\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\6\n\65\n\n")
        buf.write("\r\n\16\n\66\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\2")
        buf.write("\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\3\2\3\5\2\13\f\17\17\"\"\2A\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5 \3\2\2\2\7$")
        buf.write("\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2\17/\3\2\2\2")
        buf.write("\21\61\3\2\2\2\23\64\3\2\2\2\25:\3\2\2\2\27=\3\2\2\2\31")
        buf.write("?\3\2\2\2\33\34\7o\2\2\34\35\7c\2\2\35\36\7k\2\2\36\37")
        buf.write("\7p\2\2\37\4\3\2\2\2 !\7k\2\2!\"\7p\2\2\"#\7v\2\2#\6\3")
        buf.write("\2\2\2$%\7x\2\2%&\7q\2\2&\'\7k\2\2\'(\7f\2\2(\b\3\2\2")
        buf.write("\2)*\7*\2\2*\n\3\2\2\2+,\7+\2\2,\f\3\2\2\2-.\7}\2\2.\16")
        buf.write("\3\2\2\2/\60\7\177\2\2\60\20\3\2\2\2\61\62\7=\2\2\62\22")
        buf.write("\3\2\2\2\63\65\t\2\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66")
        buf.write("\64\3\2\2\2\66\67\3\2\2\2\678\3\2\2\289\b\n\2\29\24\3")
        buf.write("\2\2\2:;\13\2\2\2;<\b\13\3\2<\26\3\2\2\2=>\13\2\2\2>\30")
        buf.write("\3\2\2\2?@\13\2\2\2@\32\3\2\2\2\4\2\66\4\b\2\2\3\13\2")
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
    ERROR_CHAR = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "LB", "RB", "LP", "RP", "SEMI", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "LB", "RB", "LP", "RP", 
                  "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[9] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


