# Parser for COMP 5210 compiler.py project.
# Author: Ben Hulsey
# Author: Jacob Moore

#https://sly.readthedocs.io/en/latest/sly.html#introduction

# https://stackoverflow.com/questions/62983856/in-lr-parsing-is-it-possible-to-construct-a-non-binary-ast
# Used stackoverflow to walk through AST uses with SLY to get a AST and TAC built

# https://docs.python.org/3/library/symtable.html#module-symtable
# for symbol table

from sly import Parser
from tokenizer import Tokenizer
import sys



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
        super().__init__()
        self.symbol_table = {}
        self.ast = None

    def error(self, t):
        print(f"Syntax error at line {t.lineno}, position {t.index}: Unexpected token '{t.value}'")
        sys.exit(1)

    # Grammar rules and actions
    # The last match action is the first grammar rule.
    # i.e. stmt -> expr | INT ID ASSIGN NUM SEMI.
    @_('INT MAIN LPAREN RPAREN LCB stmt_list return_stmt RCB')
    def program(self, p):
        self.ast = ('Function Definition',p.MAIN, p.stmt_list, p.return_stmt)
        return self.ast
         
    @_('expr')
    def program(self, p):
        return p.expr
       
    @_('stmt stmt_list')
    def stmt_list(self, p):
        return [p.stmt] + p.stmt_list
        
    @_('stmt')
    def stmt_list(self, p):
        return [p.stmt]

    @_('INT ID ASSIGN expr SEMI')
    def stmt(self, p):
        self.ast = ('=', p.ID, p.expr)
        return self.ast
        
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
        self.ast = (p[1], p.factor, p.expr)
        return self.ast

    @_('factor')
    def expr(self, p):
        return p.factor

    @_('NUM')
    def factor(self, p):
        return p.NUM
        
    @_('ID')
    def factor(self, p):
        try:
            value = self.symbol_table[p.ID]
            self.ast = (value)
            return self.ast
        except LookupError:
            print(f'Undefined name {p.ID!r}')
            sys.exit(1)

    def ast(self, ast):              
        if ast: 
            if isinstance(ast, tuple):
                if ast[0] in ['Function Definition', 'Variable Assignment', 'Return Statement']:
                    print(ast[1], ':', ast[2])
                    self.ast[2]
                else:
                    print('=', ast[1], ast[2])
                    self.ast[1]
                    self.ast[2]
            elif isinstance(ast, int):
                return ast

