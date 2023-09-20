# COMP 5210 Tokenizer for Compiler.py
# https://sly.readthedocs.io/en/latest/sly.html#introduction
# Author: Jacob Moore jwm0083.

from sly import Lexer

class Tokenizer(Lexer):

    tokens = { ID, NUMBER, EQREL, NOTEQ, GRT, LES, GRTEQ, LESEQ, ERROR, 
               END, NEWLINE, ASSIGN, OP, LPAREN, RPAREN, LCB, RCB, KEYWORD,
               LOGICAND, LOGICOR, NEGATE, INCRMNT, DECREMNT, COMMENT
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
    
     # Rule to keep track of line numbers.
    @_(r'\n+')
    def ignore_newline(self, t):
        self.linenum += len(t.value)
    
    # Regular expression rules for tokens.
    ID          = r'[A-Za-z_][A-Za-z0-9_]*'# changed + to * finally worked. Look into re library.
    NUMBER      = r'\d+'
    OP          = r'[+\-*/]'
    EQREL       = r'\=\='
    NOTEQ       = r'!\='
    GRTEQ       = r'>\='
    LESEQ       = r'<\='
    LOGICAND    = r'\&\&'
    LOGICOR     = r'\|\|'
    INCRMNT     = r'\+\+'
    DECREMNT    = r'--'
    NEGATE      = r'\!'
    LPAREN      = r'\('
    RPAREN      = r'\)'
    ASSIGN      = r'='
    LCB         = r'\{'
    RCB         = r'\}'

    # Match action looking for keywords in Identifiers.
    @_(r'[A-Za-z_][A-Za-z0-9_]*')
    def ID(self, t):
        if t.value in self.keyword:
            t.type = 'KEYWORD'
        return t
    
    
    
if __name__ == '__main__':
    data = 'x = 3 + 42 * (s - t)'
    lexer = Tokenizer()
    tokens = []
    for tok in lexer.tokenize(data):
        tokens.append((tok.type, tok.value))


