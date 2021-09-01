grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decl decllist EOF;
decllist: decl decllist |;
decl: vardecl | funcdecl;

vardecl: mc_type ID varlist SM;
varlist: CM ID varlist |;

funcdecl:
	mc_type ID LP (mc_type ID varlist (SM mc_type ID varlist)*)? RP LB body RB;

body:
	(
		vardecl
		| assignment_statement
		| call_statement
		| return_statement
	)*;

exprdecl: expr list_expr |;
list_expr: CM expr list_expr |;

assignment_statement: ID EQ expr SM;
call_statement: ID LP exprdecl RP SM;
return_statement: RETURN expr SM;

func_call: ID LP exprdecl RP;
operands: (LP expr RP) | func_call | ID | INTLIT | FLOATLIT;
expr:
	operands
	| expr (MUL | DIV) expr
	| operands SUB operands
	| <assoc = right> expr ADD expr;
mc_type: INT | FLOAT;
// Keywords
RETURN: 'return';
FLOAT: 'float';
INT: 'int';

// Specific characters
LB: '{';
RB: '}';
LP: '(';
RP: ')';

SM: ';';
CM: ',';

EQ: '=';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

FLOATLIT: INTLIT ([.][0-9]+)? ([eE][+-]? [0-9]+)?;

INTLIT: [1-9] [0-9]* | '0';

ID: [_a-zA-Z] [_a-zA-Z0-9]*;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};