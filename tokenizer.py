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
               LOGICAND, LOGICOR, NEGATE, INCRMNT, DECREMNT, COMMENT, SEMICOLON, LIB
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
    COMMENT     = r'\/\/'
    NUM         = r'\d+'
    PLUS        = r'\+'
    MINUS       = r'\-'
    TIMES       = r'\*'
    DIVIDE      = r'\/'
    NEGATE      = r'\!'
    LPAREN      = r'\('
    RPAREN      = r'\)'
    ASSIGN      = r'='
    LCB         = r'\{'
    RCB         = r'\}'
    SEMICOLON   = r';'
    LIB         = r'\#'
    PRD         = r'\.'
    
    # Identifies base rule 
    ID          = r'[A-Za-z_][A-Za-z0-9_]*'
    
    # keywords
    ID['auto']  = AUTO
    ID['if']    = IF
    ID['int']   = INT
    ID['else']  = ELSE
    ID['while'] = WHILE
    
    
    
    
    
    
    
    #    # Keywords taken from C docs up to ISO C99
#    keyword = {, 'break', 'case', 'char' 'const', 'continue', 'default', 'do', 'double', 'else',
#               'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return',
#               'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union',
#               'unsigned', 'void', 'volatile', 'while', 'inline', '_Bool', '_Complex' '_Imaginary'
#    }


    
    # Literal characters
    # Single character that is returned "as is" when encountered.
    literals = {'{', '}', '(', ')', ';', '=', '+' }
    
    # A way to keep track of open () or {}
    def __init__(self):
        self.nesting_level = 0
    
    # Open bracket   
    @_(r'\{')
    def lbrace(self, t):
        t.type = '{'
        self.nesting_level += 1
    
    # Close bracket    
    @_(r'\{')
    def rbrace(self, t):
        t.type = '}'
        self.nesting_level -= 1
        
    # Checks to makes sure there isn't an open statement.
    # If the level isn't 0 then an error is thrown.
    def validate_nesting(self):
        if self.nesting_level != 0:
            raise SyntaxError(f"Unmatched {self.nesting_level} open statement somewhere.")
            
    def on_eof(self):
        self.validate_nesting()
    
#    # Match action looking for keywords in Identifiers.
#    @_(r'[A-Za-z_][A-Za-z0-9_]*')
#    def ID(self, t):
#        if t.value in self.keyword:
#            t.type = 'KEYWORD'
#        return t

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
