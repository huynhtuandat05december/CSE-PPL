// My ID:1913026

grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (class_declare)* EOF;

/****************************************************************************/
/*																	 		*/
/*								2.Program Structure							*/
/* 																			*/
/****************************************************************************/

/**** class ****/
class_declare: CLASS ID ( EXTENDS ID)? LP members* RP;
members: (attribute_declare | method_declare);

/**** attribute ****/
attribute_declare:
	(STATIC | FINAL | FINAL STATIC | STATIC FINAL)? var_decl;
var_decl: (immutable_attribute | mutable_attribute) SM;
immutable_attribute: data_type attribute;
mutable_attribute: data_type attribute;

/**** method ****/
method_declare:
	(STATIC) (data_type | VOID) ID LB parameter RB block_statement
	| (data_type | VOID)? ID LB parameter RB block_statement;

/****************************************************************************/
/*																	 		*/
/*								5.Expressions								*/
/* 																			*/
/****************************************************************************/

expr: expr1 (LT | GT | LE | GE) expr1 | expr1;
expr1: expr2 (EQUAL | NOT_EQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 ( ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD | INT_DIV) expr5 | expr5;
expr5: expr5 (CONCATENATION) expr6 | expr6;
expr6: NOT expr6 | expr7;
expr7: ( ADD | SUB) expr7 | expr8;
expr8: expr9 LSB expr RSB | expr9;
// member_access: expr DOT ID | ID DOT ID | expr DOT ID LB (list_of_expr)? RB | ID DOT ID LB
// (list_of_expr)? RB;
expr9:
	expr9 DOT ID (LB list_of_expr? RB)?
	| ID DOT ID (LB list_of_expr? RB)?
	| expr10;
expr10: NEW ID LB (list_of_expr)? RB expr10? | expr11;
expr11: LB expr RB | ID | literal | THIS | NIL;
list_of_expr: expr (CM expr)*;
/****************************************************************************/
/*																	 		*/
/*								6.Statements 								*/
/* 																			*/
/****************************************************************************/
statement:
	assignment_statement
	| if_statement
	| for_statement
	| break_statement
	| continue_statement
	| return_statement
	| method_invocation_statement
	| block_statement;
block_statement: LP member_block? RP;
member_block: (FINAL? var_decl)* statement+;
assignment_statement: (ID | expr8) ASSINGMENT expr SM;
if_statement: IF expr THEN statement (ELSE statement)?;
for_statement:
	FOR ID ASSINGMENT expr (TO | DOWNTO) expr DO statement;
break_statement: BREAK SM;
continue_statement: CONTINUE SM;
return_statement: RETURN expr SM;
member_access: (ID | expr) DOT ID LB list_of_expr? RB;

method_invocation_statement: member_access SM;

/****************************************************************************/
/*																	 		*/
/*								4.Type										*/
/* 																			*/
/****************************************************************************/
data_type: type_not_void | array_type | class_type;
type_not_void: INT | FLOAT | BOOLEAN | STRING;
// primitive_type: type_not_void | VOID;
array_type: type_not_void LSB INTLIT RSB;
literal: array_lit | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;
class_type: ID; //test

/****************************************************************************/
/*																	 		*/
/*								Utilities									*/
/* 																			*/
/****************************************************************************/

attribute: ID (ASSIGN expr)? idlist;
parameter: data_type ID idlist parameter_list |;
parameter_list: SM data_type ID idlist parameter_list |;
idlist: CM ID (ASSIGN expr)? idlist |;

/****************************************************************************/
/*																	 		*/
/*								3.Lexers									*/
/* 																			*/
/****************************************************************************/
/****** COMMENT *****/
LINE_CMT: '#' ~[\r\n]* -> skip;
BLOCK_CMT: '/*' .*? '*/' -> skip;

/****** KEYWORDS *****/

BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOAT: 'float';
IF: 'if';
INT: 'int';
NEW: 'new';
STRING: 'string';
THEN: 'then';
FOR: 'for';
RETURN: 'return';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';
/****** OPERATORS ***
 */
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
INT_DIV: '\\';
MOD: '%';
NOT_EQUAL: '!=';
EQUAL: '==';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCATENATION: '^';
NEW_OP: NEW;
ASSINGMENT: ':=';
ASSIGN: '=';
/****** SEPARATORS *****/
LSB: '[';
RSB: ']';
LP: '{';
RP: '}';
LB: '(';
RB: ')';
SM: ';';
CL: ':';
DOT: '.';
CM: ',';

/****** LITERALS *********/
BOOLLIT: 'true' | 'false';

STRINGLIT:
	'"' STR_CHAR* '"' {
    self.text = self.text[:]
};
array_lit: LP array_declare RP;
array_declare: expr array_list;
array_list: CM expr array_list |;
FLOATLIT:
	DIGIT+ DOT
	| DIGIT+ DOT DIGIT+
	| DIGIT+ (DOT DIGIT+)? [eE] [+-]? DIGIT+
	| DIGIT+ DOT [eE] [+-]? DIGIT+;
INTLIT: DIGIT+;
ID: [_a-zA-Z][_a-zA-Z0-9]*;
UNCLOSE_STRING:
	'"' STR_CHAR* {
    raise UncloseString(self.text[:])
};
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text[:])
};

/**** FRAGMENT *****/
fragment DIGIT: [0-9];
// fragment STR_CHAR: ~[\r\n"\\] | ('\\' [bfrnt"\\]);

fragment STR_CHAR: ~[\b\t\n\f\r"\\] | ESC_SEQ;

fragment ESC_SEQ: '\\' [btnfr"\\];
fragment ESC_ILLEGAL: '\\' ~[btnfr"\\] | '\\';
WS: [ \t\r\f]+ -> skip; // skip spaces, tabs, form feed, newline
NEWLINE: '\n'+ -> skip;
ERROR_CHAR:
	. {
		raise ErrorToken(self.text)
	};