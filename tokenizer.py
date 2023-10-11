# COMP 5210 Tokenizer for Compiler.py
# https://sly.readthedocs.io/en/latest/sly.html#introduction
# Author: Jacob Moore
# Author: Ben Hulsey

from os import times
from sly import Lexer
import sys


class Tokenizer(Lexer):



    tokens = { ID, NUM, EQREL, NOTEQ, GRT, LES, GRTEQ, LESEQ, ERROR, END, NEWLINE, ASSIGN,
               PLUS, MINUS, DIVIDE, TIMES, LPAREN, RPAREN, LCB, RCB, KEYWORD,
               LOGICAND, LOGICOR, NEGATE, INCRMNT, DECREMNT, COMMENT, SEMICOLON, STR
    } 
        
    # Keywords taken from C docs up to ISO C99
    keyword = {'auto', 'break', 'case', 'char' 'const', 'continue', 'default', 'do', 'double', 'else',
               'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return',
               'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union',
               'unsigned', 'void', 'volatile', 'while', 'inline', '_Bool', '_Complex' '_Imaginary'
    }
    
    # String with ignored characters between tokens.
    # The main purpose of ignore is to look over whitespace and other padding between the tokens.
    ignore = ' \t'
    
    
    # Regular expression rules for tokens.
    # Doubles must come first (ex: '==' must be identified before '=')
    ID          = r'[A-Za-z_][A-Za-z0-9_]*'
    STR         = r'"\t"'
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
    

    # Match action looking for keywords in Identifiers.
    @_(r'[A-Za-z_][A-Za-z0-9_]*')
    def ID(self, t):
        if t.value in self.keyword:
            t.type = 'KEYWORD'
        return t
    
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
        print("Usage: python tokenizer.py <input_file>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    
    # Open and read c file
    with open(input_file, 'r') as file:
        c_code = file.read()
        
        
    lexer = Tokenizer()
    tokens = list(lexer.tokenize(c_code))  # Convert tokens to a list
    

    for token in tokens:
        print(token)
