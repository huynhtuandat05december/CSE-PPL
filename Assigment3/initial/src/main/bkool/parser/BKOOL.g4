
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: classdecl+ EOF;

/****************************************************************************/
/*																	 		*/
/*								2.Program Structure							*/
/* 																			*/
/****************************************************************************/

/**** class ****/
classdecl:
	CLASS ID LP RP
	| CLASS ID LP memdecl RP
	| CLASS ID EXTENDS ID LP RP
	| CLASS ID EXTENDS ID LP memdecl RP;
memdecl:
	attribute_declare
	| method_declare
	| attribute_declare memdecl
	| method_declare memdecl;

/**** attribute ****/
attribute_declare: immutable_attribute | mutable_attribube;
immutable_attribute:
	FINAL const_decl
	| FINAL STATIC const_decl
	| STATIC FINAL const_decl;
mutable_attribube: STATIC var_decl | var_decl;

const_decl: data_type attribute_immutable SM;
var_decl: data_type attribute_mutable SM;

attribute_immutable:
	ID declare_assign CM attribute_immutable
	| ID CM attribute_immutable
	| ID declare_assign
	| ID;
attribute_mutable:
	ID declare_assign CM attribute_mutable
	| ID CM attribute_mutable
	| ID declare_assign
	| ID;

declare_assign: ASSIGN expr;

/**** method ****/
method_declare:
	STATIC function_type ID LB parameter_list? RB block_statement
	| function_type ID LB parameter_list? RB block_statement
	| ID LB parameter_list? RB block_statement;

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
expr9:
	expr9 DOT ID
	| ID DOT ID
	| expr9 DOT ID LB RB
	| ID DOT ID LB RB
	| expr9 DOT ID LB list_of_expr RB
	| ID DOT ID LB list_of_expr RB
	| expr10;
expr10: NEW ID LB (list_of_expr)? RB expr10? | expr11;
expr11: LB expr RB | operands;
operands: ID | literal | THIS | NIL;
array_cell: expr9 LSB expr RSB;
field_access: expr DOT ID | ID DOT ID;
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
block_statement: LP member_block RP;
member_block: var_mem statement*;
var_mem:
	const_member_block
	| var_member_block
	| const_member_block var_mem
	| var_member_block var_mem
	|;
const_member_block: FINAL const_decl;
var_member_block: var_decl;
assignment_statement: lhs ASSINGMENT expr SM;
lhs: ID | array_cell | field_access;
if_statement: IF expr THEN statement (ELSE statement)?;
for_statement:
	FOR ID ASSINGMENT expr (TO | DOWNTO) expr DO statement;
break_statement: BREAK SM;
continue_statement: CONTINUE SM;
return_statement: RETURN expr SM;
member_access:
	expr DOT ID LB RB
	| ID DOT ID LB RB
	| expr DOT ID LB list_of_expr RB
	| ID DOT ID LB list_of_expr RB;

method_invocation_statement: member_access SM;

/****************************************************************************/
/*																	 		*/
/*								4.Type										*/
/* 																			*/
/****************************************************************************/
data_type:
	INT
	| FLOAT
	| BOOLEAN
	| STRING
	| array_type
	| class_type;
function_type:
	INT
	| FLOAT
	| BOOLEAN
	| STRING
	| VOID
	| array_type
	| class_type;
array_type: (INT | FLOAT | BOOLEAN | STRING | class_type) LSB INTLIT RSB;
literal: array_lit | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;
class_type: ID; //test

/****************************************************************************/
/*																	 		*/
/*								Utilities									*/
/* 																			*/
/****************************************************************************/

parameter_list: parameter SM parameter_list | parameter;
parameter: data_type ids_list;
ids_list: ID CM ids_list | ID;

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
array_lit: LP array_list RP;
array_list: literal CM array_list | literal;
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