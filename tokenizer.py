# COMP 5210 Tokenizer for Compiler.py
# https://sly.readthedocs.io/en/latest/sly.html#introduction
# Author: Jacob Moore
# Author: Ben Hulsey


from sly import Lexer
import sys

class Tokenizer(Lexer):


    
    tokens = { LOGICAND, LOGICOR, INCRMNT, DECREMNT, EQREL, ASSIGN, NOTEQ, NEGATE, GRTEQ, LESEQ, 
               GTR, LTR, SEMI, LCB, RCB, LPAREN, RPAREN, NUM, ID, AUTO, BREAK, CASE, CHAR, CONST,
               CONTINUE, DEFAULT, DO, DOUBLE, ELSE, ENUM, EXTERN, FLOAT, FOR, GOTO, IF, INT, LONG, 
               MAIN, REGISTER, RETURN, SHORT, SIGNED, SIZEOF, STATIC, STRUCT, SWITCH, TYPEDEF, UNION,
               UNSIGNED, VOID, VOLATILE, WHILE, INLINE, BOOL, COMPLEX, IMAGINARY
             } 
        

    # String with ignored characters between tokens.
    # Characters in ignore are not ignored when such characters are part of other RE patterns.
    # The main purpose of ignore is to look over whitespace and other padding between the tokens.
    ignore = ' \t'
    
    
    # Regular expression rules for tokens.
    # Longer tokens must come first (ex: '==' must be identified before '=')
    
    LOGICAND    = r'\&\&'
    LOGICOR     = r'\|\|'
    INCRMNT     = r'\+\+'   
    DECREMNT    = r'--'
    EQREL       = r'\=\='
    ASSIGN      = r'\='
    NOTEQ       = r'!\='
    NEGATE      = r'!'
    GRTEQ       = r'>\='
    LESEQ       = r'<\='
    GTR         = r'\>'
    LTR         = r'\<'
    SEMI        = r'\;'
    LCB         = r'\{'
    RCB         = r'\}'
    LPAREN      = r'\('
    RPAREN      = r'\)'
    

    # token remapping to keywords
    ID['auto']       = AUTO
    ID['break']      = BREAK
    ID['case']       = CASE
    ID['char']       = CHAR
    ID['const']      = CONST
    ID['continue']   = CONTINUE
    ID['default']    = DEFAULT
    ID['do']         = DO
    ID['double']     = DOUBLE
    ID['else']       = ELSE
    ID['enum']       = ENUM
    ID['extern']     = EXTERN
    ID['float']      = FLOAT
    ID['for']        = FOR
    ID['goto']       = GOTO
    ID['if']         = IF
    ID['int']        = INT
    ID['long']       = LONG
    ID['main']       = MAIN
    ID['register']   = REGISTER
    ID['return']     = RETURN
    ID['signed']     = SIGNED
    ID['short']      = SHORT
    ID['sizeof']     = SIZEOF
    ID['static']     = STATIC
    ID['struct']     = STRUCT
    ID['switch']     = SWITCH
    ID['typedef']    = TYPEDEF
    ID['union']      = UNION
    ID['unsigned']   = UNSIGNED
    ID['void']       = VOID
    ID['volatile']   = VOLATILE
    ID['while']      = WHILE
    ID['inline']     = INLINE
    ID['_Bool']      = BOOL
    ID['_Complex']   = COMPLEX
    ID['_Imaginary'] = IMAGINARY
    
    # Identifies base rule 
    ID = r'[A-Za-z_][A-Za-z0-9_]*'
    
    # A match action for Hex and Decimal numbers
    @_(r'0x[0-9a-fA-F]+',
       r'\d+')
    def NUM(self, t):
        if t.value.startswith('0x'):
            t.value = int(t.value[2:], 16)
        else:
            t.value = int(t.value)
        return t


    # A way to ignore comments
    @_(r'\/\/[^\n]*',)
    def ignore_comment(self, t):
        pass

    # Literal characters
    # Single character that is returned "as is" when encountered.
    literals = {'+', '-', '*', '/', '#', '.' }

    # Rule to keep track of line numbers.
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
    
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
        
        

    
