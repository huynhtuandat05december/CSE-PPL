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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("|\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\20\6\20T\n\20\r\20\16\20U\5\20")
        buf.write("X\n\20\3\20\3\20\5\20\\\n\20\3\20\6\20_\n\20\r\20\16\20")
        buf.write("`\5\20c\n\20\3\21\3\21\7\21g\n\21\f\21\16\21j\13\21\3")
        buf.write("\21\5\21m\n\21\3\22\3\22\7\22q\n\22\f\22\16\22t\13\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\2\2\25\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25\3\2\n\3\2\60\60\3\2\62;\4\2")
        buf.write("GGgg\4\2--//\3\2\63;\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\2\u0083\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\5\60")
        buf.write("\3\2\2\2\7\66\3\2\2\2\t:\3\2\2\2\13<\3\2\2\2\r>\3\2\2")
        buf.write("\2\17@\3\2\2\2\21B\3\2\2\2\23D\3\2\2\2\25F\3\2\2\2\27")
        buf.write("H\3\2\2\2\31J\3\2\2\2\33L\3\2\2\2\35N\3\2\2\2\37P\3\2")
        buf.write("\2\2!l\3\2\2\2#n\3\2\2\2%u\3\2\2\2\'y\3\2\2\2)*\7t\2\2")
        buf.write("*+\7g\2\2+,\7v\2\2,-\7w\2\2-.\7t\2\2./\7p\2\2/\4\3\2\2")
        buf.write("\2\60\61\7h\2\2\61\62\7n\2\2\62\63\7q\2\2\63\64\7c\2\2")
        buf.write("\64\65\7v\2\2\65\6\3\2\2\2\66\67\7k\2\2\678\7p\2\289\7")
        buf.write("v\2\29\b\3\2\2\2:;\7}\2\2;\n\3\2\2\2<=\7\177\2\2=\f\3")
        buf.write("\2\2\2>?\7*\2\2?\16\3\2\2\2@A\7+\2\2A\20\3\2\2\2BC\7=")
        buf.write("\2\2C\22\3\2\2\2DE\7.\2\2E\24\3\2\2\2FG\7?\2\2G\26\3\2")
        buf.write("\2\2HI\7-\2\2I\30\3\2\2\2JK\7/\2\2K\32\3\2\2\2LM\7,\2")
        buf.write("\2M\34\3\2\2\2NO\7\61\2\2O\36\3\2\2\2PW\5!\21\2QS\t\2")
        buf.write("\2\2RT\t\3\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2")
        buf.write("VX\3\2\2\2WQ\3\2\2\2WX\3\2\2\2Xb\3\2\2\2Y[\t\4\2\2Z\\")
        buf.write("\t\5\2\2[Z\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2]_\t\3\2\2^]\3")
        buf.write("\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ac\3\2\2\2bY\3\2\2")
        buf.write("\2bc\3\2\2\2c \3\2\2\2dh\t\6\2\2eg\t\3\2\2fe\3\2\2\2g")
        buf.write("j\3\2\2\2hf\3\2\2\2hi\3\2\2\2im\3\2\2\2jh\3\2\2\2km\7")
        buf.write("\62\2\2ld\3\2\2\2lk\3\2\2\2m\"\3\2\2\2nr\t\7\2\2oq\t\b")
        buf.write("\2\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2s$\3\2\2\2")
        buf.write("tr\3\2\2\2uv\t\t\2\2vw\3\2\2\2wx\b\23\2\2x&\3\2\2\2yz")
        buf.write("\13\2\2\2z{\b\24\3\2{(\3\2\2\2\13\2UW[`bhlr\4\b\2\2\3")
        buf.write("\24\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RETURN = 1
    FLOAT = 2
    INT = 3
    LB = 4
    RB = 5
    LP = 6
    RP = 7
    SM = 8
    CM = 9
    EQ = 10
    ADD = 11
    SUB = 12
    MUL = 13
    DIV = 14
    FLOATLIT = 15
    INTLIT = 16
    ID = 17
    WS = 18
    ERROR_CHAR = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'float'", "'int'", "'{'", "'}'", "'('", "')'", 
            "';'", "','", "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "FLOAT", "INT", "LB", "RB", "LP", "RP", "SM", "CM", 
            "EQ", "ADD", "SUB", "MUL", "DIV", "FLOATLIT", "INTLIT", "ID", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "RETURN", "FLOAT", "INT", "LB", "RB", "LP", "RP", "SM", 
                  "CM", "EQ", "ADD", "SUB", "MUL", "DIV", "FLOATLIT", "INTLIT", 
                  "ID", "WS", "ERROR_CHAR" ]

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
            actions[18] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


