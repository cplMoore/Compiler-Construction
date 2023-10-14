# COMP 5210 Tokenizer for Compiler.py
# https://sly.readthedocs.io/en/latest/sly.html#introduction
# Author: Jacob Moore
# Author: Ben Hulsey

from os import times
from sly import Lexer
import sys

class Tokenizer(Lexer):



    tokens = { ID, NUM, EQREL, NOTEQ, GRT, LES, GRTEQ, LESEQ, ERROR, END, NEWLINE, ASSIGN,
               PLUS, MINUS, DIVIDE, TIMES, LPAREN, RPAREN, LCB, RCB, KEYWORD, PRD, IF, INT,
               LOGICAND, LOGICOR, NEGATE, INCRMNT, DECREMNT, COMMENT, SEMICOLON, LIB, AUTO,
               ELSE, WHILE, AUTO, BREAK, CASE, CHAR, CONST, CONTINUE, DEFAULT, DO, DOUBLE,
               ENUM, EXTERN, FLOAT, FOR, GOTO, LONG,  REGISTER, RETURN, SHORT, SIGNED, SIZEOF,
               STATIC, STRUCT, SWITCH, TYPEDEF, UNION, UNSIGNED, VOID, VOLATILE, INLINE, BOOL,
               COMPLEX, IMAGINARY
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
    NOTEQ       = r'!\='
    GRTEQ       = r'>\='
    LESEQ       = r'<\='
    NUM         = r'\d+'
#    PLUS        = r'\+'
#    MINUS       = r'\-'
#    TIMES       = r'\*'
#    DIVIDE      = r'\/'
#    NEGATE      = r'\!'
#    LPAREN      = r'\('
#    RPAREN      = r'\)'
#    ASSIGN      = r'='
#    LCB         = r'\{'
#    RCB         = r'\}'
#    SEMICOLON   = r';'
#    LIB         = r'\#'
#    PRD         = r'\.'
    
    # Identifies base rule 
    ID = r'[A-Za-z_][A-Za-z0-9_]*'
    
    # keywords
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
    ID['register']   = REGISTER
    ID['return']     = RETURN
    ID['short']      = SHORT
    ID['signed']     = SIGNED
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

    # A way to ignore comments
    @_(r'\/\/[^\n]*')
    def ignore_comment(self, t):
        pass

    # Literal characters
    # Single character that is returned "as is" when encountered.
    literals = {'{', '}', '(', ')', ';', '=', '+', '-', '*', '/',
                '#', '.' }
    
    # A way to keep track of open () or {}
    def __init__(self):
        self.nesting_level = 0
    
    # Open bracket   
    @_(r'\{')
    def lbrace(self, t):
        t.type = '{'
        self.nesting_level += 1
        return t
    
    # Close bracket    
    @_(r'\}')
    def rbrace(self, t):
        t.type = '}'
        self.nesting_level -= 1
        return t
        
    # Open parentheses   
    @_(r'\(')
    def lparen(self, t):
        t.type = '('
        self.nesting_level += 1
        return t
    
    # Close parentheses    
    @_(r'\)')
    def rparen(self, t):
        t.type = ')'
        self.nesting_level -= 1
        return t
        
    # Checks to makes sure there isn't an open statement.
    # If the level isn't 0 then an error is thrown.
    def validate_nesting(self):
        if self.nesting_level != 0:
            raise SyntaxError(f"Unmatched {self.nesting_level} open statement somewhere.")
            
    def on_eof(self):
        self.validate_nesting()
    

    # Rule to keep track of line numbers.
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
    
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


if __name__ == '__main__':
    # Checks if a c file is provided.
    if len(sys.argv) != 2:
        print("Usage: python3 tokenizer.py <input_file>")
        sys.exit(1)
        
    # Takes the c file passed with compiler.py    
    input_file = sys.argv[1]
    
    # Open and read c file
    with open(input_file, 'r') as file:
        c_code = file.read()
        
        
    lexer = Tokenizer()
    tokens = list(lexer.tokenize(c_code))  # Convert tokens to a list
    

    for token in tokens:
        print(token)
        
    
