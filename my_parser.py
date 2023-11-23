# Parser for COMP 5210 compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction



# https://docs.python.org/3/library/symtable.html#module-symtable
# for symbol table

from sly import Parser
from tokenizer import Tokenizer

class MyParser(Parser):


     # Debugging help from SLY
    debugfile = 'parser.out'
    
    # Brings in the token list.
    tokens = Tokenizer.tokens
    
    # Keeps order of operations.
    # + and - have the same precedence.
    # * and / have the same precedence, 
    # but have a higher level of precedence than + or - since they come later in the list per SLY.
    precedence = (
        ('left', "+", "-"),
        ('left', "*", "/"),
    )

    def __init__(self):
        self.ast = None

    # def error(self, t):
        # print(f"Syntax error at line {t.lineno}, position {t.index}: Unexpected token '{t.value}'")


    # Grammar rules and actions
    # The last match action is the first grammar rule.
    # i.e. stmt -> expr | INT ID ASSIGN NUM SEMI.
    @_('INT MAIN LPAREN RPAREN LCB stmt_list return_stmt RCB')
    def program(self, p):
        self.ast = p.MAIN, p.stmt_list, p.return_stmt
        return self.ast
         
    @_('expr')
    def program(self, p):
        return p.expr
       
    @_('stmt stmt_list')
    def stmt_list(self, p):
        return p.stmt, p.stmt_list
        
    @_('stmt')
    def stmt_list(self, p):
        return p.stmt

    @_('INT ID ASSIGN expr SEMI')
    def stmt(self, p):
        return('=', p.ID, p.expr)
        
    @_('LPAREN expr RPAREN')
    def stmt(self, p):
        return p.expr

    @_('RETURN factor SEMI')
    def return_stmt(self, p):
        self.ast = ('return', p.factor)
        return self.ast

    @_('factor "+" expr',
       'factor "-" expr',
       'factor "*" expr', 
       'factor "/" expr')
    def expr(self, p):
        return (p[1], p.factor, p.expr)

    @_('factor')
    def expr(self, p):
        return p.factor

    @_('NUM')
    def factor(self, p):
        return p.NUM
        
    @_('ID')
    def factor(self, p):
        return p.ID



