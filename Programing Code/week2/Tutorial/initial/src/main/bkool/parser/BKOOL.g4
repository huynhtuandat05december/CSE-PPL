grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: mptype 'main' LB RB LP body? RP EOF;

mptype: INTTYPE | VOIDTYPE;

body: funcall SEMI;

exp: funcall | INTLIT;

funcall: ID LB exp? RB;

INTTYPE: 'int';

VOIDTYPE: 'void';

// ID: [a-zA-Z]+;

// INTLIT: [0-9]+;

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

// EX1: [a-z][a-z0-9]*;

// REAL1: [0-9]+ [.][0-9]+; REAL2: [0-9]+ [e][+|-][0-9]+; REAL3: [0-9]+ [.][0-9]+ [e][+|-][0-9]+;
// REAL: REAL1 | REAL2 | REAL3; EX2: REAL;

// EX3: [']~[']* ([']~[']* [']~[']*)? ['];
ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
