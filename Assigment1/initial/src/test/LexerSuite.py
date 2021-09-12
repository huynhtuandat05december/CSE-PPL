import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_valid_identifier1(self):
        """Test Valid Identifiers"""
        self.assertTrue(TestLexer.test(
            """
    id ID _id 89id 89ID 89_id
                """,
            "id,ID,_id,89,id,89,ID,89,_id,<EOF>",
            101
        ))

    def test_valid_identifier2(self):
        """Test Valid Identifiers"""
        self.assertTrue(TestLexer.test(
            """
    id boolean_id float_id int_id string_id void_id
                """,
            "id,boolean_id,float_id,int_id,string_id,void_id,<EOF>",
            102
        ))

    def test_valid_identifier3(self):
        """ Test Valid Identifiers """
        self.assertTrue(TestLexer.test(
            """
    a abc a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123
    _ _abc _123 _abc123 _abc_123 _123_abc
    __ ____ ____123____
    abc ABC aBC Abc _ABC __ABc __123ABc
    hdad_adsajdk_hf__T_
                """,

            "a,abc,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,_,_abc,_123,_abc123,_abc_123,_123_abc,__,____,____123____,abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,hdad_adsajdk_hf__T_,<EOF>",
            103
        ))

    def test_valid_identifier4(self):
        """ Test Valid Identifiers """
        self.assertTrue(TestLexer.test(
            """
    abc ABC aBC __abcd
    KK __abc___________________d ABC___1 AC90
    AB thang b c
                """,

            "abc,ABC,aBC,__abcd,KK,__abc___________________d,ABC___1,AC90,AB,thang,b,c,<EOF>",
            104
        ))

    def test_valid_identifier5(self):
        """ Test Valid Identifiers """
        self.assertTrue(TestLexer.test(
            """
    ac cb KL Ab Abc_abc
     ANKD______ccs abc_____________abc____________abc
     abc__ab abc______________________c dsa
                """,
            "ac,cb,KL,Ab,Abc_abc,ANKD______ccs,abc_____________abc____________abc,abc__ab,abc______________________c,dsa,<EOF>",
            105
        ))

    def test_invalid_identifier(self):
        """Test Invalid Identifiers"""
        self.assertTrue(TestLexer.test(
            """
    id-1 id&1
                """,
            "id,-,1,id,Error Token &",
            106
        ))

    def test_invalid_identifier2(self):
        """ Test Invalid Identifiers """
        self.assertTrue(TestLexer.test(
            """
    123abc 123_abc 00000123_123abc
    id_id 1id 321id 1321_id 89________________id
    id___2 90___abc__ads___sba____abc____dba ds&a
                """,

            "123,abc,123,_abc,00000123,_123abc,id_id,1,id,321,id,1321,_id,89,________________id,id___2,90,___abc__ads___sba____abc____dba,ds,Error Token &",
            107
        ))

    def test_inline_comment(self):
        """Test Inline Comment"""
        self.assertTrue(TestLexer.test(
            """
    # inline comment
    # inline comment
                """, "<EOF>", 108
        ))

    def test_block_comment(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.test(
            """
    /* Comment with multiple lines
        Hello comments
        This is block comment
    */
                """,

            "<EOF>",
            109
        ))

    def test_block_comment2(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.test(
            """
    /* This is another way to do it, also in C.
     ** It is easier to do in editors that do not automatically indent the second
     ** through last lines of the comment one space from the first.
     ** It is also used in Holub's book, in rule 31.
     */
                """,

            "<EOF>",
            110
        ))

    def test_block_comment3(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.test(
            """
    /***************************\
    *                           *
    * This is the comment body. *
    * Variation Two.            *
    *                           *
    \***************************/
                """,

            "<EOF>",
            111
        ))

    def test_mix_comment(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
    /* This is a block comment */
    # This is a line comment
    /* Comment with multiple lines
        Hello comments
    */
    /*
        Comment multiple lines
    */
    /* nest comments
        # inline comment
    # inline comment
    */
                """,

            "<EOF>",
            112
        ))

    def test_mix_comment2(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
    /* This is the style recommended by Holub for C and C++.
    * It is demonstrated in ''Enough Rope'', in rule 29.
    */
    # This is inline comment
    #
    /**/
    /*                          */
    # This is comment
                """,

            "<EOF>",
            113
        ))

    def test_mix_comment3(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
    /* /* # // /b/r/n */ */
    /*/* This is a block comment so # has no meaning here*/ */
    # This is comment
                """,

            "*,/,*,/,<EOF>",
            114
        ))

    def test_mix_comment4(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.test(
            """
    # This is a line comment so /* has no meaning here
                """,

            "<EOF>",
            115
        ))

    def test_invalid_comment(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
    # inline comment \b \t
        is multiple lines
    # inline comment
    """,

            "is,multiple,lines,<EOF>",
            116
        ))

    def test_invalid_comment2(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
    #!/usr/bin/env python3
    /# -*- coding: UTF-8 -*-
                """,

            "/,<EOF>",
            117
        ))

    def test_invalid_comment3(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
    <!-- begin& wsf_resource_nodes -->
    <!-- end: wsf_resource_nodes -->
                """,

            "<,!,-,-,begin,Error Token &",
            118
        ))

    def test_invalid_comment4(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.test(
            """
    !* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    !* All characters after an exclamation mark are considered as comments *
    !* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                """,

            "!,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,!,*,All,characters,after,an,exclamation,mark,are,considered,as,comments,*,!,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,<EOF>",
            119
        ))

    def test_valid_int_lit(self):
        """ Test Valid Integer Literal """
        self.assertTrue(TestLexer.test(
            """
    0 1 2 3 4 123 123456789 001 0x123
                """,

            "0,1,2,3,4,123,123456789,001,0,x123,<EOF>",
            120
        ))

    def test_valid_int_lit2(self):
        """ Test Valid Integer Literal """
        self.assertTrue(TestLexer.test(
            """
    0001321 00000031231 000312312
    00312 0 123 132 012 1 2 3 8912
    0000000000000000000000000000000001
    09132 321 00000000000000000000000000000000000000000001
                """,

            "0001321,00000031231,000312312,00312,0,123,132,012,1,2,3,8912,0000000000000000000000000000000001,09132,321,00000000000000000000000000000000000000000001,<EOF>",
            121
        ))

    def test_invalid_int_lit2(self):
        """ Test Invalid Integer Literal """
        self.assertTrue(TestLexer.test(
            """
    0x131321 0X89ABC 0xffffff
    0xABC 0X2132
                """,
            "0,x131321,0,X89ABC,0,xffffff,0,xABC,0,X2132,<EOF>",
            122
        ))

    def test_bool_lit(self):
        """ Test Boolean Literal """
        self.assertTrue(TestLexer.test(
            """
    true false
                """,
            "true,false,<EOF>",
            123
        ))

    def test_invalid_bool_lit(self):
        """ Test Invalid Boolean Literal """
        self.assertTrue(TestLexer.test(
            """
    TRUE True TRue TRUe falSe
    falSE FAlse FAlsE
    truE False FAlSE
                """,
            "TRUE,True,TRue,TRUe,falSe,falSE,FAlse,FAlsE,truE,False,FAlSE,<EOF>",
            124
        ))

    def test_float_lit(self):
        """ Test Float Literal """
        self.assertTrue(TestLexer.test(
            """
    9.0 12e8 1. 0.33E-3 128e+42
                """,

            "9.0,12e8,1.,0.33E-3,128e+42,<EOF>",
            125
        ))

    def test_float_leading_zero(self):
        """ Test Float Leading Zero """
        self.assertTrue(TestLexer.test(
            """
    00001.1101010101000
    0e-432
    000000001e-542400
    000313121.e00031321132
                """,

            "00001.1101010101000,0e-432,000000001e-542400,000313121.e00031321132,<EOF>",
            126
        ))

    def test_invalid_float_lit(self):
        """ Test Invalid Float Literal """
        self.assertTrue(TestLexer.test(
            """
    1e 123e e123 e-132 -e123 123e1
    1.e3 .e10
                """,

            "1,e,123,e,e123,e,-,132,-,e123,123e1,1.e3,.,e10,<EOF>",
            127
        ))

    def test_string_lit(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.test(
            """
    ""
    "String"
    " "
    "?"
    "-"
    "//"
    "Mulitiple Characters"
                """,

            """"","String"," ","?","-","//","Mulitiple Characters",<EOF>""",
            128
        ))

    def test_invalid_string_lit(self):
        """ Test Invalid String Literal """
        self.assertTrue(TestLexer.test(
            """
            ""
            "string"
            'string'
            "string'
            'string"
            """,

            """"","string",Error Token '""",
            129
        ))

    def test_mix_lit(self):
        """ Test Mix Literal """
        self.assertTrue(TestLexer.test(
            """
            ""
            12 32.43 43.E12 4e-1 true "false" false "012" 1.32 1.
            "String"
            """,

            """"",12,32.43,43.E12,4e-1,true,"false",false,"012",1.32,1.,"String",<EOF>""",
            130
        ))

    def test_unclose_without_endline(self):
        """ Test Unclose String without endline """
        self.assertTrue(TestLexer.test(
            """
            " hello lexer
            """,

            """Unclosed String: " hello lexer""",
            131
        ))

    def test_unclose_multi_lines(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            """
    "Newline
        multiple lines
    "
                """,

            """Unclosed String: "Newline""",
            132
        ))

    def test_unclose_use_escape(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            """
    "\"abc
                """,

            """"",abc,<EOF>""",
            133
        ))

    def test_unclose_with_invalid_close(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            """
    s = "string          '
    "a = 4
    g = 9
                """,

            """s,=,Unclosed String: "string          '""",
            134
        ))

    def test_escape1(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            """
    " abc \n xyz "
    " abc \\n xyz "
    """,

            """Unclosed String: " abc """,
            135
        ))

    def test_escape2(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            """
    " hello lexer \t \b \n \""     asdf
    """,

            """Unclosed String: " hello lexer """,
            136
        ))

    def test_escape3(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.test(
            r"""
    "Backspace  \b"
    "Formfeed   \f"
    "Return     \r"
    "Newline    \n"
    "Tab        \t"
    "Double quote       \""
    "Backslash  \\ "
                """,

            r""""Backspace  \b","Formfeed   \f","Return     \r","Newline    \n","Tab        \t","Double quote       \"","Backslash  \\ ",<EOF>""",

            137
        ))

    def test_illegal1(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """ Illegal"\a" """,

            """Illegal,"",<EOF>""",
            138
        ))

    def test_illegal2(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
    " Hi Hi \c \d "
                """,

            """Illegal Escape In String: " Hi Hi \c""",
            139
        ))

    def test_illegal3(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
    " Hi Hi \s\d\\f "
                """,

            """Illegal Escape In String: " Hi Hi \s""",
            140
        ))

    def test_illegal4(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            """
    "abc - xyz"
    "abc \ xyz"
                """,

            """"abc - xyz",Illegal Escape In String: "abc \ """,
            141
        ))

    def test_illegal5(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            """
    "abc - xyz"
    "abc \yyz"
                """,

            """"abc - xyz",Illegal Escape In String: "abc \y""",
            142
        ))

    def test_illegal6(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            """
    "abc\mabc"
                """,

            """Illegal Escape In String: "abc\m""",
            143
        ))

    def test_illegal7(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            """
    "\a"
                """,

            """"",<EOF>""",
            144
        ))

    def test_illegal8(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.test(
            """
    "2.dasd1f21.da1.24@%761!809!@808132)318()^*&*13\o"
                """,

            """Illegal Escape In String: "2.dasd1f21.da1.24@%761!809!@808132)318()^*&*13\o""",
            145
        ))

    def test_illegal9(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.test(
            """
    "&*&(^(\#!\4))"
                """,
            """Illegal Escape In String: "&*&(^(\#""", 146
        ))

    def test_94_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """
        " abc \r  xyz "
    """,

            """Unclosed String: " abc """,
            147
        ))

    def test_95_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """ "abc\fabc" """, """Unclosed String: "abc""", 148))

    def test_96_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """
        " abc \n  xyz "
    """,

            """Unclosed String: " abc """,
            149
        ))

    def test_97_illegal_char_in_string(self):
        """ Test Illegal Character in String """
        self.assertTrue(TestLexer.test(
            """
        " abc \t  xyz "
    """,

            """Unclosed String: " abc """,
            150
        ))

    def test_err_tok1(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
    !== != & ^ % $ # ... \
                """,

            "!=,=,!=,Error Token &",
            151
        ))

    def test_err_tok2(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
    a = a ~ 1
                """,

            "a,=,a,Error Token ~",
            152
        ))

    def test_err_tok3(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
    'a = 5
                """,

            "Error Token '",
            153
        ))

    def test_err_tok4(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            """
    abc?
                """,

            "abc,Error Token ?",
            154
        ))

    def test_err_tok5(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            "aAajskjkwscsVN hgSVnxx%**/*/*hg?dajkj",
            "aAajskjkwscsVN,hgSVnxx,%,*,*,/,*,/,*,hg,Error Token ?",
            155
        ))

    def test_err_tok6(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            "*(*)()_+_+)(()$)",
            "*,(,*,),(,),_,+,_,+,),(,(,),Error Token $",
            156
        ))

    def test_err_tok7(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            "hakasjdklsajdkla*()*)%!++(+)|*()",
            "hakasjdklsajdkla,*,(,),*,),%,!,+,+,(,+,),Error Token |",
            157
        ))

    def test_err_tok8(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            " ;,[](){}%+-=====*/@asnakncslka&*))(_h",
            ";,,,[,],(,),{,},%,+,-,==,==,=,*,/,Error Token @",
            158
        ))

    def test_keyword(self):
        """ Test Keyword """
        self.assertTrue(TestLexer.test(
            """
    boolean break class continue do else
    extends float if int new string
    then for return true false void
    nil this final static to downto
                """,
            "boolean,break,class,continue,do,else,extends,float,if,int,new,string,then,for,return,true,false,void,nil,this,final,static,to,downto,<EOF>",
            159
        ))

    def test_invalid_keyword(self):
        """ Test Invalid Keyword """
        self.assertTrue(TestLexer.test(
            "BOOLEAN int 1.12INTEGER sTRIng not 12and",
            "BOOLEAN,int,1.12,INTEGER,sTRIng,not,12,and,<EOF>",
            160
        ))

    def test_invalid_keyword2(self):
        """ Test Invalid Keyword """
        self.assertTrue(TestLexer.test(
            "BOOLean Int INTeger STRING whiLE If foR Float Void VOID Break BREAK CONtinue CONTINUE True TRUE FALSE",
            "BOOLean,Int,INTeger,STRING,whiLE,If,foR,Float,Void,VOID,Break,BREAK,CONtinue,CONTINUE,True,TRUE,FALSE,<EOF>",
            161
        ))

    def test_operator(self):
        """ Test Operator """
        self.assertTrue(TestLexer.test(
            """
    + - * / \ % != == < > <= >= || && ! ^ new
                """,

            "+,-,*,/,\,%,!=,==,<,>,<=,>=,||,&&,!,^,new,<EOF>",
            162
        ))

    def test_invalid_operator2(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            """
    *= /= %=
                """,

            "*,=,/,=,%,=,<EOF>",
            163
        ))

    def test_invalid_operator(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            """
    ++ -- += -= & ^ |
                """,

            "+,+,-,-,+,=,-,=,Error Token &",
            164
        ))

    def test_invalid_operator3(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            " !xyz 45**4290=12 a<>b+2^3 c-=d) x=y",
            "!,xyz,45,*,*,4290,=,12,a,<,>,b,+,2,^,3,c,-,=,d,),x,=,y,<EOF>",
            165
        ))

    def test_invalid_operator4(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            "   income+=salary.12*12+month/3",
            "income,+,=,salary,.,12,*,12,+,month,/,3,<EOF>",
            166
        ))

    def test_invalid_operator5(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            "   x = (4 + 3i)(2 + 5i)?i^2",
            "x,=,(,4,+,3,i,),(,2,+,5,i,),Error Token ?",
            167
        ))

    def test_invalid_operator6(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.test(
            "cost = sum((y - h(i))**2)",
            "cost,=,sum,(,(,y,-,h,(,i,),),*,*,2,),<EOF>",
            168
        ))

    def test_case_sensitive_keyword(self):
        """ Test Case Sensitive Keyword """
        self.assertTrue(TestLexer.test(
            "truE TRUE tRUe",
            "truE,TRUE,tRUe,<EOF>",
            169
        ))

    def test_case_sensitive_keyword2(self):
        """ Test Case Sensitive Keyword """
        self.assertTrue(TestLexer.test(
            "false FALse FOR FOr If iF While WHILE contiNue CONTInue Break break",
            "false,FALse,FOR,FOr,If,iF,While,WHILE,contiNue,CONTInue,Break,break,<EOF>",
            170
        ))

    def test_unclose_string(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.test(
            "38n\"[#Ffs?0ED\"0.\"T`#!7n",
            """38,n,"[#Ffs?0ED",0.,Unclosed String: "T`#!7n""",
            171
        ))

    def test_unclose_string2(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.test(
            "{SRs}\"Nk8U;\"rA\"@Y3*\"oV\"bh1",
            """{,SRs,},"Nk8U;",rA,"@Y3*",oV,Unclosed String: "bh1""",
            172
        ))

    def test_unclose_string3(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.test(
            "\"o|F&)LqX\"+>X+\"#Fft",
            """"o|F&)LqX",+,>,X,+,Unclosed String: "#Fft""",
            173
        ))

    def test_unclose_string4(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.test(
            "a+11.2+\"mam.123\" 12 \"%^&",
            """a,+,11.2,+,"mam.123",12,Unclosed String: "%^&""",
            174
        ))

    def test_operator2(self):
        """ Test Operator """
        self.assertTrue(TestLexer.test(
            "not<>=and>=mod<=-and!=or&&^^",
            "not,<,>=,and,>=,mod,<=,-,and,!=,or,&&,^,^,<EOF>",
            175
        ))

    def test_operator3(self):
        """ Test Operator """
        self.assertTrue(TestLexer.test(
            "+-*/%*()/*//$#",
            "+,-,*,/,%,*,(,),/,*,/,/,Error Token $",
            176
        ))

    def test_operator4(self):
        """ Test Operator """
        self.assertTrue(TestLexer.test(
            """
                a + b = c
                a * b = c ** 2
                a / 2 = 5
                a % 2 = 6
                a # 2 = 0.6
                a && a == 1
                """,
            "a,+,b,=,c,a,*,b,=,c,*,*,2,a,/,2,=,5,a,%,2,=,6,a,a,&&,a,==,1,<EOF>",
            177
        ))

    def test_random1(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
                # \f abc
                /* // */ acc
                a++;
                string a = "a";
                """,
            """acc,a,+,+,;,string,a,=,"a",;,<EOF>""",
            178
        ))

    def test_random2(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
                for (int a ; b = 2 && c = 2; 2**2)
                break
                """,
            "for,(,int,a,;,b,=,2,&&,c,=,2,;,2,*,*,2,),break,<EOF>",
            179
        ))

    def test_random3(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
                int a,b       ,c ,a                   b;
                float a = b (abc).12;
                str abc[] = {1,2,3};
                """,
            "int,a,,,b,,,c,,,a,b,;,float,a,=,b,(,abc,),.,12,;,str,abc,[,],=,{,1,,,2,,,3,},;,<EOF>",
            180
        ))

    def test_full11(self):
        """all of the token"""
        self.assertTrue(TestLexer.test("$no idea", "Error Token $", 181))

    def test_random5(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
                INT abc = 12;
                abc = "";
                float = 2.e2
                char = ''
                """,
            """INT,abc,=,12,;,abc,=,"",;,float,=,2.e2,char,=,Error Token '""",
            182
        ))

    def test_random6(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
                "t \{abcd}\\x efg"
                """,
            """Illegal Escape In String: "t \{""",
            183
        ))

    def test_random7(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
    # ],],* ae0bc not mod,return,,
    {} < + Qefbe and ; of o366c false array else < > and for J4981 & <> return = for if ..
    (* of break h80bb,or,bfa18 ) W6bd3,float,<*)
                """,
            "{,},<,+,Qefbe,and,;,of,o366c,false,array,else,<,>,and,for,J4981,Error Token &",
            184
        ))

    def test_random8(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
    # and,<=,return v415f ( division,and,or
    + , or b328b = <= ) G39be ? else break / * = [ Qd057 ] float[] break * >= do >
    (* end , b60f1,>=,dd28e , dd3ab,string,of*)
                """,
            "+,,,or,b328b,=,<=,),G39be,Error Token ?",
            185
        ))

    def test_random9(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
    # >=,<=,for of8ae * :=,then,>=
    - + false P4366 ; * , l84bc , > : flaot true [ / while Va93a boolean and integer function - , false
    (* new , Wbffd,),y6349 else w7e53,(,)*)
                """,
            "-,+,false,P4366,;,*,,,l84bc,,,>,:,flaot,true,[,/,while,Va93a,boolean,and,integer,function,-,,,false,(,*,new,,,Wbffd,,,),,,y6349,else,w7e53,,,(,,,),*,),<EOF>",
            186
        ))

    def test_random10(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
    # [,<>,( k6301 with begin,],true
    + - integer N0699 + > then L09e7 >= float > >= , ] <> * eb142 > integer / while boolean procedure false
    (* false for Z2262,do,G9a7c continue e46e2,+,break*)
                """,
            "+,-,integer,N0699,+,>,then,L09e7,>=,float,>,>=,,,],<,>,*,eb142,>,integer,/,while,boolean,procedure,false,(,*,false,for,Z2262,,,do,,,G9a7c,continue,e46e2,,,+,,,break,*,),<EOF>",
            187
        ))

    def test_random11(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """ " """"" " " " a""",
            """Unclosed String: "   a""",
            188
        ))

    def test_random12(self):
        """ Test Random """
        self.assertTrue(TestLexer.test(
            """
        if flag then
            a:=1
        else
            a:=2
                """,
            "if,flag,then,a,:=,1,else,a,:=,2,<EOF>",

            189
        ))

    def test_complex_program1(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
    float a, b, c;
    boolean x, y, z;
    int g, h, y;
    float nty();
    int x, y, z;
    int q, w;
    string a;
        /*
            =======================================
            Comment here
            =======================================
        */
    """,

            """float,a,,,b,,,c,;,boolean,x,,,y,,,z,;,int,g,,,h,,,y,;,float,nty,(,),;,int,x,,,y,,,z,;,int,q,,,w,;,string,a,;,<EOF>""",
            190
        ))

    def test_complex_program2(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
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
                """,

            "class,Example1,{,int,factorial,(,int,n,),{,if,n,==,0,then,return,1,;,else,return,n,*,this,.,factorial,(,n,-,1,),;,},void,main,(,),{,int,x,;,x,:=,io,.,readInt,(,),;,io,.,writeIntLn,(,this,.,factorial,(,x,),),;,},},<EOF>",
            191
        ))

    def test_complex_program3(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
    class Shape {
    float length,width;
    float getArea() {}
    Shape(float length,width){
    this.length := length;
    this.width := width;
    }
    }
                """,

            "class,Shape,{,float,length,,,width,;,float,getArea,(,),{,},Shape,(,float,length,,,width,),{,this,.,length,:=,length,;,this,.,width,:=,width,;,},},<EOF>",
            192
        ))

    def test_complex_program4(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
    class Rectangle extends Shape {
    float getArea(){
    return this.length*this.width;
    }
    }
                """,

            "class,Rectangle,extends,Shape,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},<EOF>",
            193
        ))

    def test_complex_program5(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
    class Triangle extends Shape {
    float getArea(){
    return this.length*this.width / 2;
    }
    }
                """,

            "class,Triangle,extends,Shape,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,/,2,;,},},<EOF>",
            194
        ))

    def test_complex_program6(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """
    class Example2 {
    void main(){
    s:Shape;
    s := new Rectangle(3,4);
    io.writeFloatLn(s.getArea());
    s := new Triangle(3,4);
    io.writeFloatLn(s.getArea());
    }
    }
                """,

            "class,Example2,{,void,main,(,),{,s,:,Shape,;,s,:=,new,Rectangle,(,3,,,4,),;,io,.,writeFloatLn,(,s,.,getArea,(,),),;,s,:=,new,Triangle,(,3,,,4,),;,io,.,writeFloatLn,(,s,.,getArea,(,),),;,},},<EOF>",
            195
        ))

    def test_complex_program7(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.test(
            """classX{
    void print(string str){io.writeString(str);}
    void main(){this.print(\"\";}}""",
            """classX,{,void,print,(,string,str,),{,io,.,writeString,(,str,),;,},void,main,(,),{,this,.,print,(,"",;,},},<EOF>""",
            196
        ))

    def test_070(self):
        input = """ a:="Hello world \t Hello World " """
        expect = """a,:=,Unclosed String: "Hello world """
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test_str10(self):
        self.assertTrue(TestLexer.test(""" "String with newline\nafter newline" """,
                        """Unclosed String: "String with newline""", 198))

    def test_string(self):
        input = """a:="Hello world1 \b Hello World1 " """
        expect = """a,:=,Unclosed String: "Hello world1 """
        self.assertTrue(TestLexer.test(input, expect, 199))

    def test_prog8(self):
        """a full program"""
        input = """class A{void x(){}}
        class B extends A{void x(){/*cmt*/}}"""
        expect = "class,A,{,void,x,(,),{,},},class,B,extends,A,{,void,x,(,),{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 200))
