# COMP 5210 Tokenizer for Compiler.py
# https://sly.readthedocs.io/en/latest/sly.html#introduction
# Author: Jacob Moore jwm0083.

from sly import Lexer

class Tokenizer(Lexer):

    tokens = { ID, NUMBER, EQREL, NOTEQ, GRT, LES, GRTEQ, LESEQ, 
               END, NEWLINE, ASSIGN, OP, LPAREN, RPAREN, LCB, RCB,
               LOGICAND, LOGICOR, NEGATE, INCRMNT, DECREMNT, COMMENT, ERROR}
               
    # String with ignored characters between tokens.
    ignore = ' \t'
    
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
    
if __name__ == '__main__':
    data = 'x = 3 + 42 * (s - t)'
    lexer = Tokenizer()
    for tok in lexer.tokenize(data):
        print('type = %r, value = %r' % (tok.type, tok.value))


