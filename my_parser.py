# Parser for COMP 5210 compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction


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

#    def error(self, t):
#        print(f"Syntax error at line {t.lineno}, position {t.index}: Unexpected token '{t.value}'")


    # Grammar rules and actions
    # The last match action is the first grammar rule.
    # i.e. stmt -> expr | INT ID ASSIGN NUM SEMI.
    @_('main_method')
    def program(self, p):
        return p.main_method
    
    @_('fun_decl main_method')
    def program(self, p):
        return p.fun_decl, p.main_method
         
    @_('expr')
    def program(self, p):
        return p.expr
        
    @_('keyword ID LPAREN RPAREN LCB stmt_list RCB')
    def fun_decl(self,p):
        return p.keyword, p.ID, p.stmt_list
        
    @_('INT MAIN LPAREN RPAREN LCB stmt_list return_stmt RCB')
    def main_method(self, p):
        return p.MAIN, p.stmt_list, p.return_stmt
       
    @_('stmt stmt_list')
    def stmt_list(self, p):
        return p.stmt, p.stmt_list
        
    @_('stmt')
    def stmt_list(self, p):
        return p.stmt

    @_('INT ID ASSIGN expr SEMI',
       'LPAREN expr RPAREN')
    def stmt(self, p):
        return('=', p.ID, p.expr)

    @_('RETURN factor SEMI')
    def return_stmt(self, p):
        return ('return', p.factor)

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
        
    @_('INT',
       'IF',
       'ELSE',
       'VOID',
       'STATIC')
    def keyword(self, p):
        return p[0]
