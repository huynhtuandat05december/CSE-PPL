# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u01c0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\7\2")
        buf.write("\\\n\2\f\2\16\2_\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3g\n\3")
        buf.write("\3\3\3\3\7\3k\n\3\f\3\16\3n\13\3\3\3\3\3\3\4\3\4\5\4t")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5|\n\5\3\5\3\5\3\6\3\6")
        buf.write("\5\6\u0082\n\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\5\t\u008f\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u0099\n\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a1\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00af\n\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00b7\n\f")
        buf.write("\f\f\16\f\u00ba\13\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00c2")
        buf.write("\n\r\f\r\16\r\u00c5\13\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\7\16\u00cd\n\16\f\16\16\16\u00d0\13\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\7\17\u00d8\n\17\f\17\16\17\u00db\13\17")
        buf.write("\3\20\3\20\3\20\5\20\u00e0\n\20\3\21\3\21\3\21\5\21\u00e5")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00ed\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f5\n\23\3\23\5\23")
        buf.write("\u00f8\n\23\3\23\5\23\u00fb\n\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u0102\n\23\3\23\5\23\u0105\n\23\7\23\u0107\n")
        buf.write("\23\f\23\16\23\u010a\13\23\3\24\3\24\3\24\3\24\5\24\u0110")
        buf.write("\n\24\3\24\3\24\5\24\u0114\n\24\3\24\5\24\u0117\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0121\n\25")
        buf.write("\3\26\3\26\3\26\7\26\u0126\n\26\f\26\16\26\u0129\13\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0133\n")
        buf.write("\27\3\30\3\30\5\30\u0137\n\30\3\30\3\30\3\31\5\31\u013c")
        buf.write("\n\31\3\31\7\31\u013f\n\31\f\31\16\31\u0142\13\31\3\31")
        buf.write("\6\31\u0145\n\31\r\31\16\31\u0146\3\32\3\32\5\32\u014b")
        buf.write("\n\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0157\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \5 \u016e\n \3 \3 \3 \3 \5 \u0174\n \3 \3 ")
        buf.write("\3!\3!\3!\3\"\3\"\3\"\5\"\u017e\n\"\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3%\3%\3%\3%\3%\5%\u018c\n%\3&\3&\3\'\3\'\3\'\5\'\u0193")
        buf.write("\n\'\3\'\3\'\3(\3(\3(\3(\3(\3(\5(\u019d\n(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\5)\u01a6\n)\3*\3*\3*\3*\5*\u01ac\n*\3*\3*\5")
        buf.write("*\u01b0\n*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\5-\u01be")
        buf.write("\n-\3-\2\7\26\30\32\34$.\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\t\3")
        buf.write("\2#&\3\2!\"\3\2\'(\3\2\33\34\3\2\35 \3\2\31\32\6\2\5\5")
        buf.write("\f\f\16\16\20\20\2\u01d2\2]\3\2\2\2\4b\3\2\2\2\6s\3\2")
        buf.write("\2\2\b{\3\2\2\2\n\u0081\3\2\2\2\f\u0085\3\2\2\2\16\u0088")
        buf.write("\3\2\2\2\20\u00a0\3\2\2\2\22\u00a7\3\2\2\2\24\u00ae\3")
        buf.write("\2\2\2\26\u00b0\3\2\2\2\30\u00bb\3\2\2\2\32\u00c6\3\2")
        buf.write("\2\2\34\u00d1\3\2\2\2\36\u00df\3\2\2\2 \u00e4\3\2\2\2")
        buf.write("\"\u00ec\3\2\2\2$\u00fa\3\2\2\2&\u0116\3\2\2\2(\u0120")
        buf.write("\3\2\2\2*\u0122\3\2\2\2,\u0132\3\2\2\2.\u0134\3\2\2\2")
        buf.write("\60\u0140\3\2\2\2\62\u014a\3\2\2\2\64\u0150\3\2\2\2\66")
        buf.write("\u0158\3\2\2\28\u0161\3\2\2\2:\u0164\3\2\2\2<\u0167\3")
        buf.write("\2\2\2>\u016d\3\2\2\2@\u0177\3\2\2\2B\u017d\3\2\2\2D\u017f")
        buf.write("\3\2\2\2F\u0181\3\2\2\2H\u018b\3\2\2\2J\u018d\3\2\2\2")
        buf.write("L\u018f\3\2\2\2N\u019c\3\2\2\2P\u01a5\3\2\2\2R\u01af\3")
        buf.write("\2\2\2T\u01b1\3\2\2\2V\u01b5\3\2\2\2X\u01bd\3\2\2\2Z\\")
        buf.write("\5\4\3\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3")
        buf.write("\2\2\2_]\3\2\2\2`a\7\2\2\3a\3\3\2\2\2bc\7\7\2\2cf\7<\2")
        buf.write("\2de\7\13\2\2eg\7<\2\2fd\3\2\2\2fg\3\2\2\2gh\3\2\2\2h")
        buf.write("l\7\60\2\2ik\5\6\4\2ji\3\2\2\2kn\3\2\2\2lj\3\2\2\2lm\3")
        buf.write("\2\2\2mo\3\2\2\2nl\3\2\2\2op\7\61\2\2p\5\3\2\2\2qt\5\b")
        buf.write("\5\2rt\5\20\t\2sq\3\2\2\2sr\3\2\2\2t\7\3\2\2\2u|\7\30")
        buf.write("\2\2v|\7\27\2\2wx\7\27\2\2x|\7\30\2\2yz\7\30\2\2z|\7\27")
        buf.write("\2\2{u\3\2\2\2{v\3\2\2\2{w\3\2\2\2{y\3\2\2\2{|\3\2\2\2")
        buf.write("|}\3\2\2\2}~\5\n\6\2~\t\3\2\2\2\177\u0082\5\f\7\2\u0080")
        buf.write("\u0082\5\16\b\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2")
        buf.write("\u0082\u0083\3\2\2\2\u0083\u0084\7\64\2\2\u0084\13\3\2")
        buf.write("\2\2\u0085\u0086\5B\"\2\u0086\u0087\5L\'\2\u0087\r\3\2")
        buf.write("\2\2\u0088\u0089\5B\"\2\u0089\u008a\5L\'\2\u008a\17\3")
        buf.write("\2\2\2\u008b\u008e\7\30\2\2\u008c\u008f\5B\"\2\u008d\u008f")
        buf.write("\7\24\2\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u0090\u0091\7<\2\2\u0091\u0092\7\62\2\2")
        buf.write("\u0092\u0093\5N(\2\u0093\u0094\7\63\2\2\u0094\u0095\5")
        buf.write(".\30\2\u0095\u00a1\3\2\2\2\u0096\u0099\5B\"\2\u0097\u0099")
        buf.write("\7\24\2\2\u0098\u0096\3\2\2\2\u0098\u0097\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\7<\2\2")
        buf.write("\u009b\u009c\7\62\2\2\u009c\u009d\5N(\2\u009d\u009e\7")
        buf.write("\63\2\2\u009e\u009f\5.\30\2\u009f\u00a1\3\2\2\2\u00a0")
        buf.write("\u008b\3\2\2\2\u00a0\u0098\3\2\2\2\u00a1\21\3\2\2\2\u00a2")
        buf.write("\u00a3\5\24\13\2\u00a3\u00a4\t\2\2\2\u00a4\u00a5\5\24")
        buf.write("\13\2\u00a5\u00a8\3\2\2\2\u00a6\u00a8\5\24\13\2\u00a7")
        buf.write("\u00a2\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\23\3\2\2\2\u00a9")
        buf.write("\u00aa\5\26\f\2\u00aa\u00ab\t\3\2\2\u00ab\u00ac\5\26\f")
        buf.write("\2\u00ac\u00af\3\2\2\2\u00ad\u00af\5\26\f\2\u00ae\u00a9")
        buf.write("\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\25\3\2\2\2\u00b0\u00b1")
        buf.write("\b\f\1\2\u00b1\u00b2\5\30\r\2\u00b2\u00b8\3\2\2\2\u00b3")
        buf.write("\u00b4\f\4\2\2\u00b4\u00b5\t\4\2\2\u00b5\u00b7\5\30\r")
        buf.write("\2\u00b6\u00b3\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\27\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00bb\u00bc\b\r\1\2\u00bc\u00bd\5\32\16\2\u00bd")
        buf.write("\u00c3\3\2\2\2\u00be\u00bf\f\4\2\2\u00bf\u00c0\t\5\2\2")
        buf.write("\u00c0\u00c2\5\32\16\2\u00c1\u00be\3\2\2\2\u00c2\u00c5")
        buf.write("\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\31\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\b\16\1\2\u00c7")
        buf.write("\u00c8\5\34\17\2\u00c8\u00ce\3\2\2\2\u00c9\u00ca\f\4\2")
        buf.write("\2\u00ca\u00cb\t\6\2\2\u00cb\u00cd\5\34\17\2\u00cc\u00c9")
        buf.write("\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\33\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1")
        buf.write("\u00d2\b\17\1\2\u00d2\u00d3\5\36\20\2\u00d3\u00d9\3\2")
        buf.write("\2\2\u00d4\u00d5\f\4\2\2\u00d5\u00d6\7*\2\2\u00d6\u00d8")
        buf.write("\5\36\20\2\u00d7\u00d4\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\35\3\2\2\2\u00db")
        buf.write("\u00d9\3\2\2\2\u00dc\u00dd\7)\2\2\u00dd\u00e0\5\36\20")
        buf.write("\2\u00de\u00e0\5 \21\2\u00df\u00dc\3\2\2\2\u00df\u00de")
        buf.write("\3\2\2\2\u00e0\37\3\2\2\2\u00e1\u00e2\t\5\2\2\u00e2\u00e5")
        buf.write("\5 \21\2\u00e3\u00e5\5\"\22\2\u00e4\u00e1\3\2\2\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e5!\3\2\2\2\u00e6\u00e7\5$\23\2\u00e7")
        buf.write("\u00e8\7.\2\2\u00e8\u00e9\5\22\n\2\u00e9\u00ea\7/\2\2")
        buf.write("\u00ea\u00ed\3\2\2\2\u00eb\u00ed\5$\23\2\u00ec\u00e6\3")
        buf.write("\2\2\2\u00ec\u00eb\3\2\2\2\u00ed#\3\2\2\2\u00ee\u00ef")
        buf.write("\b\23\1\2\u00ef\u00f0\7<\2\2\u00f0\u00f1\7\66\2\2\u00f1")
        buf.write("\u00f7\7<\2\2\u00f2\u00f4\7\62\2\2\u00f3\u00f5\5*\26\2")
        buf.write("\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\3")
        buf.write("\2\2\2\u00f6\u00f8\7\63\2\2\u00f7\u00f2\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00fb\5&\24\2")
        buf.write("\u00fa\u00ee\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u0108\3")
        buf.write("\2\2\2\u00fc\u00fd\f\5\2\2\u00fd\u00fe\7\66\2\2\u00fe")
        buf.write("\u0104\7<\2\2\u00ff\u0101\7\62\2\2\u0100\u0102\5*\26\2")
        buf.write("\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103\3")
        buf.write("\2\2\2\u0103\u0105\7\63\2\2\u0104\u00ff\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0107\3\2\2\2\u0106\u00fc\3\2\2\2")
        buf.write("\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3")
        buf.write("\2\2\2\u0109%\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c")
        buf.write("\7\17\2\2\u010c\u010d\7<\2\2\u010d\u010f\7\62\2\2\u010e")
        buf.write("\u0110\5*\26\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u0111\3\2\2\2\u0111\u0113\7\63\2\2\u0112\u0114")
        buf.write("\5&\24\2\u0113\u0112\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0117\3\2\2\2\u0115\u0117\5(\25\2\u0116\u010b\3\2\2\2")
        buf.write("\u0116\u0115\3\2\2\2\u0117\'\3\2\2\2\u0118\u0119\7\62")
        buf.write("\2\2\u0119\u011a\5\22\n\2\u011a\u011b\7\63\2\2\u011b\u0121")
        buf.write("\3\2\2\2\u011c\u0121\7<\2\2\u011d\u0121\5H%\2\u011e\u0121")
        buf.write("\7\26\2\2\u011f\u0121\7\25\2\2\u0120\u0118\3\2\2\2\u0120")
        buf.write("\u011c\3\2\2\2\u0120\u011d\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u011f\3\2\2\2\u0121)\3\2\2\2\u0122\u0127\5\22\n")
        buf.write("\2\u0123\u0124\7\67\2\2\u0124\u0126\5\22\n\2\u0125\u0123")
        buf.write("\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128+\3\2\2\2\u0129\u0127\3\2\2\2\u012a")
        buf.write("\u0133\5\62\32\2\u012b\u0133\5\64\33\2\u012c\u0133\5\66")
        buf.write("\34\2\u012d\u0133\58\35\2\u012e\u0133\5:\36\2\u012f\u0133")
        buf.write("\5<\37\2\u0130\u0133\5@!\2\u0131\u0133\5.\30\2\u0132\u012a")
        buf.write("\3\2\2\2\u0132\u012b\3\2\2\2\u0132\u012c\3\2\2\2\u0132")
        buf.write("\u012d\3\2\2\2\u0132\u012e\3\2\2\2\u0132\u012f\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133-\3\2\2")
        buf.write("\2\u0134\u0136\7\60\2\2\u0135\u0137\5\60\31\2\u0136\u0135")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u0139\7\61\2\2\u0139/\3\2\2\2\u013a\u013c\7\27\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013f\5\n\6\2\u013e\u013b\3\2\2\2\u013f\u0142\3")
        buf.write("\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0144")
        buf.write("\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0145\5,\27\2\u0144")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0147\3\2\2\2\u0147\61\3\2\2\2\u0148\u014b\7<\2")
        buf.write("\2\u0149\u014b\5\"\22\2\u014a\u0148\3\2\2\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\7,\2\2\u014d")
        buf.write("\u014e\5\22\n\2\u014e\u014f\7\64\2\2\u014f\63\3\2\2\2")
        buf.write("\u0150\u0151\7\r\2\2\u0151\u0152\5\22\n\2\u0152\u0153")
        buf.write("\7\21\2\2\u0153\u0156\5,\27\2\u0154\u0155\7\n\2\2\u0155")
        buf.write("\u0157\5,\27\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157\65\3\2\2\2\u0158\u0159\7\22\2\2\u0159\u015a\7<")
        buf.write("\2\2\u015a\u015b\7,\2\2\u015b\u015c\5\22\n\2\u015c\u015d")
        buf.write("\t\7\2\2\u015d\u015e\5\22\n\2\u015e\u015f\7\t\2\2\u015f")
        buf.write("\u0160\5,\27\2\u0160\67\3\2\2\2\u0161\u0162\7\6\2\2\u0162")
        buf.write("\u0163\7\64\2\2\u01639\3\2\2\2\u0164\u0165\7\b\2\2\u0165")
        buf.write("\u0166\7\64\2\2\u0166;\3\2\2\2\u0167\u0168\7\23\2\2\u0168")
        buf.write("\u0169\5\22\n\2\u0169\u016a\7\64\2\2\u016a=\3\2\2\2\u016b")
        buf.write("\u016e\7<\2\2\u016c\u016e\5\22\n\2\u016d\u016b\3\2\2\2")
        buf.write("\u016d\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\7")
        buf.write("\66\2\2\u0170\u0171\7<\2\2\u0171\u0173\7\62\2\2\u0172")
        buf.write("\u0174\5*\26\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174\u0175\3\2\2\2\u0175\u0176\7\63\2\2\u0176?\3\2\2")
        buf.write("\2\u0177\u0178\5> \2\u0178\u0179\7\64\2\2\u0179A\3\2\2")
        buf.write("\2\u017a\u017e\5D#\2\u017b\u017e\5F$\2\u017c\u017e\5J")
        buf.write("&\2\u017d\u017a\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017c")
        buf.write("\3\2\2\2\u017eC\3\2\2\2\u017f\u0180\t\b\2\2\u0180E\3\2")
        buf.write("\2\2\u0181\u0182\5D#\2\u0182\u0183\7.\2\2\u0183\u0184")
        buf.write("\7;\2\2\u0184\u0185\7/\2\2\u0185G\3\2\2\2\u0186\u018c")
        buf.write("\5T+\2\u0187\u018c\7;\2\2\u0188\u018c\7:\2\2\u0189\u018c")
        buf.write("\78\2\2\u018a\u018c\79\2\2\u018b\u0186\3\2\2\2\u018b\u0187")
        buf.write("\3\2\2\2\u018b\u0188\3\2\2\2\u018b\u0189\3\2\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018cI\3\2\2\2\u018d\u018e\7<\2\2\u018e")
        buf.write("K\3\2\2\2\u018f\u0192\7<\2\2\u0190\u0191\7-\2\2\u0191")
        buf.write("\u0193\5\22\n\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2")
        buf.write("\2\u0193\u0194\3\2\2\2\u0194\u0195\5R*\2\u0195M\3\2\2")
        buf.write("\2\u0196\u0197\5B\"\2\u0197\u0198\7<\2\2\u0198\u0199\5")
        buf.write("R*\2\u0199\u019a\5P)\2\u019a\u019d\3\2\2\2\u019b\u019d")
        buf.write("\3\2\2\2\u019c\u0196\3\2\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("O\3\2\2\2\u019e\u019f\7\64\2\2\u019f\u01a0\5B\"\2\u01a0")
        buf.write("\u01a1\7<\2\2\u01a1\u01a2\5R*\2\u01a2\u01a3\5P)\2\u01a3")
        buf.write("\u01a6\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5\u019e\3\2\2\2")
        buf.write("\u01a5\u01a4\3\2\2\2\u01a6Q\3\2\2\2\u01a7\u01a8\7\67\2")
        buf.write("\2\u01a8\u01ab\7<\2\2\u01a9\u01aa\7-\2\2\u01aa\u01ac\5")
        buf.write("\22\n\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01ad\u01b0\5R*\2\u01ae\u01b0\3\2\2\2\u01af")
        buf.write("\u01a7\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0S\3\2\2\2\u01b1")
        buf.write("\u01b2\7\60\2\2\u01b2\u01b3\5V,\2\u01b3\u01b4\7\61\2\2")
        buf.write("\u01b4U\3\2\2\2\u01b5\u01b6\5\22\n\2\u01b6\u01b7\5X-\2")
        buf.write("\u01b7W\3\2\2\2\u01b8\u01b9\7\67\2\2\u01b9\u01ba\5\22")
        buf.write("\n\2\u01ba\u01bb\5X-\2\u01bb\u01be\3\2\2\2\u01bc\u01be")
        buf.write("\3\2\2\2\u01bd\u01b8\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("Y\3\2\2\2\60]fls{\u0081\u008e\u0098\u00a0\u00a7\u00ae")
        buf.write("\u00b8\u00c3\u00ce\u00d9\u00df\u00e4\u00ec\u00f4\u00f7")
        buf.write("\u00fa\u0101\u0104\u0108\u010f\u0113\u0116\u0120\u0127")
        buf.write("\u0132\u0136\u013b\u0140\u0146\u014a\u0156\u016d\u0173")
        buf.write("\u017d\u018b\u0192\u019c\u01a5\u01ab\u01af\u01bd")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'boolean'", 
                     "'break'", "'class'", "'continue'", "'do'", "'else'", 
                     "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
                     "'then'", "'for'", "'return'", "'void'", "'nil'", "'this'", 
                     "'final'", "'static'", "'to'", "'downto'", "'+'", "'-'", 
                     "'*'", "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", 
                     "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", 
                     "<INVALID>", "':='", "'='", "'['", "']'", "'{'", "'}'", 
                     "'('", "')'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "LINE_CMT", "BLOCK_CMT", "BOOLEAN", "BREAK", 
                      "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", 
                      "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
                      "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "ADD", "SUB", "MUL", "DIV", "INT_DIV", "MOD", "NOT_EQUAL", 
                      "EQUAL", "LT", "GT", "LE", "GE", "OR", "AND", "NOT", 
                      "CONCATENATION", "NEW_OP", "ASSINGMENT", "ASSIGN", 
                      "LSB", "RSB", "LP", "RP", "LB", "RB", "SM", "CL", 
                      "DOT", "CM", "BOOLLIT", "STRINGLIT", "FLOATLIT", "INTLIT", 
                      "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "NEWLINE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declare = 1
    RULE_members = 2
    RULE_attribute_declare = 3
    RULE_var_decl = 4
    RULE_immutable_attribute = 5
    RULE_mutable_attribute = 6
    RULE_method_declare = 7
    RULE_expr = 8
    RULE_expr1 = 9
    RULE_expr2 = 10
    RULE_expr3 = 11
    RULE_expr4 = 12
    RULE_expr5 = 13
    RULE_expr6 = 14
    RULE_expr7 = 15
    RULE_expr8 = 16
    RULE_expr9 = 17
    RULE_expr10 = 18
    RULE_expr11 = 19
    RULE_list_of_expr = 20
    RULE_statement = 21
    RULE_block_statement = 22
    RULE_member_block = 23
    RULE_assignment_statement = 24
    RULE_if_statement = 25
    RULE_for_statement = 26
    RULE_break_statement = 27
    RULE_continue_statement = 28
    RULE_return_statement = 29
    RULE_member_access = 30
    RULE_method_invocation_statement = 31
    RULE_data_type = 32
    RULE_type_not_void = 33
    RULE_array_type = 34
    RULE_literal = 35
    RULE_class_type = 36
    RULE_attribute = 37
    RULE_parameter = 38
    RULE_parameter_list = 39
    RULE_idlist = 40
    RULE_array_lit = 41
    RULE_array_declare = 42
    RULE_array_list = 43

    ruleNames =  [ "program", "class_declare", "members", "attribute_declare", 
                   "var_decl", "immutable_attribute", "mutable_attribute", 
                   "method_declare", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "expr10", "expr11", "list_of_expr", "statement", "block_statement", 
                   "member_block", "assignment_statement", "if_statement", 
                   "for_statement", "break_statement", "continue_statement", 
                   "return_statement", "member_access", "method_invocation_statement", 
                   "data_type", "type_not_void", "array_type", "literal", 
                   "class_type", "attribute", "parameter", "parameter_list", 
                   "idlist", "array_lit", "array_declare", "array_list" ]

    EOF = Token.EOF
    LINE_CMT=1
    BLOCK_CMT=2
    BOOLEAN=3
    BREAK=4
    CLASS=5
    CONTINUE=6
    DO=7
    ELSE=8
    EXTENDS=9
    FLOAT=10
    IF=11
    INT=12
    NEW=13
    STRING=14
    THEN=15
    FOR=16
    RETURN=17
    VOID=18
    NIL=19
    THIS=20
    FINAL=21
    STATIC=22
    TO=23
    DOWNTO=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    INT_DIV=29
    MOD=30
    NOT_EQUAL=31
    EQUAL=32
    LT=33
    GT=34
    LE=35
    GE=36
    OR=37
    AND=38
    NOT=39
    CONCATENATION=40
    NEW_OP=41
    ASSINGMENT=42
    ASSIGN=43
    LSB=44
    RSB=45
    LP=46
    RP=47
    LB=48
    RB=49
    SM=50
    CL=51
    DOT=52
    CM=53
    BOOLLIT=54
    STRINGLIT=55
    FLOATLIT=56
    INTLIT=57
    ID=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    WS=61
    NEWLINE=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def class_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declareContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CLASS:
                self.state = 88
                self.class_declare()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def members(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MembersContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MembersContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = BKOOLParser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKOOLParser.CLASS)
            self.state = 97
            self.match(BKOOLParser.ID)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 98
                self.match(BKOOLParser.EXTENDS)
                self.state = 99
                self.match(BKOOLParser.ID)


            self.state = 102
            self.match(BKOOLParser.LP)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 103
                self.members()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_declareContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declareContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = BKOOLParser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_members)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 111
                self.attribute_declare()
                pass

            elif la_ == 2:
                self.state = 112
                self.method_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Var_declContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declare" ):
                return visitor.visitAttribute_declare(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declare(self):

        localctx = BKOOLParser.Attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 115
                self.match(BKOOLParser.STATIC)

            elif la_ == 2:
                self.state = 116
                self.match(BKOOLParser.FINAL)

            elif la_ == 3:
                self.state = 117
                self.match(BKOOLParser.FINAL)
                self.state = 118
                self.match(BKOOLParser.STATIC)

            elif la_ == 4:
                self.state = 119
                self.match(BKOOLParser.STATIC)
                self.state = 120
                self.match(BKOOLParser.FINAL)


            self.state = 123
            self.var_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def immutable_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Immutable_attributeContext,0)


        def mutable_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Mutable_attributeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 125
                self.immutable_attribute()
                pass

            elif la_ == 2:
                self.state = 126
                self.mutable_attribute()
                pass


            self.state = 129
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Immutable_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(BKOOLParser.Data_typeContext,0)


        def attribute(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immutable_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutable_attribute" ):
                return visitor.visitImmutable_attribute(self)
            else:
                return visitor.visitChildren(self)




    def immutable_attribute(self):

        localctx = BKOOLParser.Immutable_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_immutable_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.data_type()
            self.state = 132
            self.attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mutable_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(BKOOLParser.Data_typeContext,0)


        def attribute(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mutable_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutable_attribute" ):
                return visitor.visitMutable_attribute(self)
            else:
                return visitor.visitChildren(self)




    def mutable_attribute(self):

        localctx = BKOOLParser.Mutable_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mutable_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.data_type()
            self.state = 135
            self.attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def parameter(self):
            return self.getTypedRuleContext(BKOOLParser.ParameterContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def data_type(self):
            return self.getTypedRuleContext(BKOOLParser.Data_typeContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declare" ):
                return visitor.visitMethod_declare(self)
            else:
                return visitor.visitChildren(self)




    def method_declare(self):

        localctx = BKOOLParser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_declare)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(BKOOLParser.STATIC)
                self.state = 140
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                    self.state = 138
                    self.data_type()
                    pass
                elif token in [BKOOLParser.VOID]:
                    self.state = 139
                    self.match(BKOOLParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 142
                self.match(BKOOLParser.ID)
                self.state = 143
                self.match(BKOOLParser.LB)
                self.state = 144
                self.parameter()
                self.state = 145
                self.match(BKOOLParser.RB)
                self.state = 146
                self.block_statement()
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 148
                    self.data_type()

                elif la_ == 2:
                    self.state = 149
                    self.match(BKOOLParser.VOID)


                self.state = 152
                self.match(BKOOLParser.ID)
                self.state = 153
                self.match(BKOOLParser.LB)
                self.state = 154
                self.parameter()
                self.state = 155
                self.match(BKOOLParser.RB)
                self.state = 156
                self.block_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LE(self):
            return self.getToken(BKOOLParser.LE, 0)

        def GE(self):
            return self.getToken(BKOOLParser.GE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.expr1()
                self.state = 161
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LE) | (1 << BKOOLParser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = BKOOLParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.expr2(0)
                self.state = 168
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 169
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 182
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 177
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 178
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 179
                    self.expr3(0) 
                self.state = 184
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKOOLParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 188
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 189
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 190
                    self.expr4(0) 
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def INT_DIV(self):
            return self.getToken(BKOOLParser.INT_DIV, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 199
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 200
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.DIV) | (1 << BKOOLParser.INT_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 201
                    self.expr5(0) 
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def CONCATENATION(self):
            return self.getToken(BKOOLParser.CONCATENATION, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 210
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 211
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 212
                    self.expr6() 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = BKOOLParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr6)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(BKOOLParser.NOT)
                self.state = 219
                self.expr6()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = BKOOLParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 224
                self.expr7()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.expr8()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = BKOOLParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr8)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.expr9(0)
                self.state = 229
                self.match(BKOOLParser.LSB)
                self.state = 230
                self.expr()
                self.state = 231
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.expr9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(BKOOLParser.List_of_exprContext,0)


        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr9, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 237
                self.match(BKOOLParser.ID)
                self.state = 238
                self.match(BKOOLParser.DOT)
                self.state = 239
                self.match(BKOOLParser.ID)
                self.state = 245
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 240
                    self.match(BKOOLParser.LB)
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0):
                        self.state = 241
                        self.list_of_expr()


                    self.state = 244
                    self.match(BKOOLParser.RB)


                pass

            elif la_ == 2:
                self.state = 247
                self.expr10()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                    self.state = 250
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 251
                    self.match(BKOOLParser.DOT)
                    self.state = 252
                    self.match(BKOOLParser.ID)
                    self.state = 258
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        self.state = 253
                        self.match(BKOOLParser.LB)
                        self.state = 255
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0):
                            self.state = 254
                            self.list_of_expr()


                        self.state = 257
                        self.match(BKOOLParser.RB)

             
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def list_of_expr(self):
            return self.getTypedRuleContext(BKOOLParser.List_of_exprContext,0)


        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def expr11(self):
            return self.getTypedRuleContext(BKOOLParser.Expr11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(BKOOLParser.NEW)
                self.state = 266
                self.match(BKOOLParser.ID)
                self.state = 267
                self.match(BKOOLParser.LB)
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0):
                    self.state = 268
                    self.list_of_expr()


                self.state = 271
                self.match(BKOOLParser.RB)
                self.state = 273
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 272
                    self.expr10()


                pass
            elif token in [BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr11)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(BKOOLParser.LB)
                self.state = 279
                self.expr()
                self.state = 280
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LP, BKOOLParser.BOOLLIT, BKOOLParser.STRINGLIT, BKOOLParser.FLOATLIT, BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 285
                self.match(BKOOLParser.NIL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_list_of_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_expr" ):
                return visitor.visitList_of_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_of_expr(self):

        localctx = BKOOLParser.List_of_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_of_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.expr()
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 289
                self.match(BKOOLParser.CM)
                self.state = 290
                self.expr()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(BKOOLParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKOOLParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Return_statementContext,0)


        def method_invocation_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invocation_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.assignment_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 299
                self.break_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 300
                self.continue_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 301
                self.return_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 302
                self.method_invocation_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 303
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def member_block(self):
            return self.getTypedRuleContext(BKOOLParser.Member_blockContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = BKOOLParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(BKOOLParser.LP)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 307
                self.member_block()


            self.state = 310
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def FINAL(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.FINAL)
            else:
                return self.getToken(BKOOLParser.FINAL, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_member_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_block" ):
                return visitor.visitMember_block(self)
            else:
                return visitor.visitChildren(self)




    def member_block(self):

        localctx = BKOOLParser.Member_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_member_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 313
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==BKOOLParser.FINAL:
                        self.state = 312
                        self.match(BKOOLParser.FINAL)


                    self.state = 315
                    self.var_decl() 
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 322 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 321
                self.statement()
                self.state = 324 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSINGMENT(self):
            return self.getToken(BKOOLParser.ASSINGMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = BKOOLParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 326
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 327
                self.expr8()
                pass


            self.state = 330
            self.match(BKOOLParser.ASSINGMENT)
            self.state = 331
            self.expr()
            self.state = 332
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BKOOLParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(BKOOLParser.IF)
            self.state = 335
            self.expr()
            self.state = 336
            self.match(BKOOLParser.THEN)
            self.state = 337
            self.statement()
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 338
                self.match(BKOOLParser.ELSE)
                self.state = 339
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSINGMENT(self):
            return self.getToken(BKOOLParser.ASSINGMENT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BKOOLParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(BKOOLParser.FOR)
            self.state = 343
            self.match(BKOOLParser.ID)
            self.state = 344
            self.match(BKOOLParser.ASSINGMENT)
            self.state = 345
            self.expr()
            self.state = 346
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 347
            self.expr()
            self.state = 348
            self.match(BKOOLParser.DO)
            self.state = 349
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = BKOOLParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(BKOOLParser.BREAK)
            self.state = 352
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = BKOOLParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(BKOOLParser.CONTINUE)
            self.state = 355
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BKOOLParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(BKOOLParser.RETURN)
            self.state = 358
            self.expr()
            self.state = 359
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def list_of_expr(self):
            return self.getTypedRuleContext(BKOOLParser.List_of_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access" ):
                return visitor.visitMember_access(self)
            else:
                return visitor.visitChildren(self)




    def member_access(self):

        localctx = BKOOLParser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_member_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 361
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 362
                self.expr()
                pass


            self.state = 365
            self.match(BKOOLParser.DOT)
            self.state = 366
            self.match(BKOOLParser.ID)
            self.state = 367
            self.match(BKOOLParser.LB)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.BOOLLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 368
                self.list_of_expr()


            self.state = 371
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access(self):
            return self.getTypedRuleContext(BKOOLParser.Member_accessContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = BKOOLParser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.member_access()
            self.state = 374
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_not_void(self):
            return self.getTypedRuleContext(BKOOLParser.Type_not_voidContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = BKOOLParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_data_type)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.type_not_void()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.array_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.class_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_not_voidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_type_not_void

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_not_void" ):
                return visitor.visitType_not_void(self)
            else:
                return visitor.visitChildren(self)




    def type_not_void(self):

        localctx = BKOOLParser.Type_not_voidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_type_not_void)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_not_void(self):
            return self.getTypedRuleContext(BKOOLParser.Type_not_voidContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.type_not_void()
            self.state = 384
            self.match(BKOOLParser.LSB)
            self.state = 385
            self.match(BKOOLParser.INTLIT)
            self.state = 386
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Array_litContext,0)


        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(BKOOLParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_literal)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.array_lit()
                pass
            elif token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 391
                self.match(BKOOLParser.BOOLLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 392
                self.match(BKOOLParser.STRINGLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = BKOOLParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = BKOOLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(BKOOLParser.ID)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ASSIGN:
                self.state = 398
                self.match(BKOOLParser.ASSIGN)
                self.state = 399
                self.expr()


            self.state = 402
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(BKOOLParser.Data_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(BKOOLParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = BKOOLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_parameter)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.data_type()
                self.state = 405
                self.match(BKOOLParser.ID)
                self.state = 406
                self.idlist()
                self.state = 407
                self.parameter_list()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def data_type(self):
            return self.getTypedRuleContext(BKOOLParser.Data_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(BKOOLParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = BKOOLParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_parameter_list)
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(BKOOLParser.SM)
                self.state = 413
                self.data_type()
                self.state = 414
                self.match(BKOOLParser.ID)
                self.state = 415
                self.idlist()
                self.state = 416
                self.parameter_list()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(BKOOLParser.CM)
                self.state = 422
                self.match(BKOOLParser.ID)
                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.ASSIGN:
                    self.state = 423
                    self.match(BKOOLParser.ASSIGN)
                    self.state = 424
                    self.expr()


                self.state = 427
                self.idlist()
                pass
            elif token in [BKOOLParser.RB, BKOOLParser.SM]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def array_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Array_declareContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKOOLParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(BKOOLParser.LP)
            self.state = 432
            self.array_declare()
            self.state = 433
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def array_list(self):
            return self.getTypedRuleContext(BKOOLParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declare" ):
                return visitor.visitArray_declare(self)
            else:
                return visitor.visitChildren(self)




    def array_declare(self):

        localctx = BKOOLParser.Array_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.expr()
            self.state = 436
            self.array_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def array_list(self):
            return self.getTypedRuleContext(BKOOLParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKOOLParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_list)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.match(BKOOLParser.CM)
                self.state = 439
                self.expr()
                self.state = 440
                self.array_list()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr2_sempred
        self._predicates[11] = self.expr3_sempred
        self._predicates[12] = self.expr4_sempred
        self._predicates[13] = self.expr5_sempred
        self._predicates[17] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




