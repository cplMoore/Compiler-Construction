# COMP 5210 Tokenizer for Compiler.py
# https://sly.readthedocs.io/en/latest/sly.html#introduction
# Author: Jacob Moore
# Author: Ben Hulsey

from os import times
from sly import Lexer
from pprint import pprint

file_path = "test.c" #read in a file 
with open(file_path, "r") as file:
        file_contents = file.read()

class Tokenizer(Lexer):


    tokens = { ID, NUM, EQREL, NOTEQ, GRT, LES, GRTEQ, LESEQ, ERROR, 
               END, NEWLINE, ASSIGN, PLUS, MINUS, DIVIDE, TIMES, LPAREN, RPAREN, LCB, RCB, KEYWORD,
               LOGICAND, LOGICOR, NEGATE, INCRMNT, DECREMNT, COMMENT, INT, EOF, STR
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
    EOF         = r';'
    

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
    data = file_contents
    lexer = Tokenizer()
    tokens = list(lexer.tokenize(data))  # Convert tokens to a list
    

    for token in tokens:
        print(token)
