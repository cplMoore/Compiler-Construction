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
        ('left', "*", "/")
    
    )

    def __init__(self):
        super().__init__()
        self.symbol_table = {}
        self.ast = None
        self.three_address_code = []

    def error(self, t):
        print(f"Syntax error at line {t.lineno}, position {t.index}: Unexpected token '{t.value}'")
        sys.exit(1)

    # Grammar rules and actions
    # The last match action is the first grammar rule.
    # i.e. stmt -> expr | INT ID ASSIGN NUM SEMI.
    @_('INT ID LPAREN RPAREN LCB stmt_list return_stmt RCB')
    def program(self, p):
        self.ast = ('Function Definition', p.ID, p.stmt_list, p.return_stmt)
        return self.ast
        
    @_('stmt stmt_list')
    def stmt_list(self, p):
        return [p.stmt] + p.stmt_list
        
    @_('stmt')
    def stmt_list(self, p):
        return [p.stmt]

    @_('INT ID ASSIGN NUM SEMI')
    def stmt(self, p):
        self.ast = ('Variable Assignment', p.ID, p.NUM)
        return self.ast
        
    @_('expr')
    def stmt(self, p):
        return p.expr

    @_('RETURN factor SEMI')
    def return_stmt(self, p):
        self.ast = ('Return Statement', p.factor)
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

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr

    @_('ID')
    def factor(self, p):
        try:
            value = self.symbol_table[p.ID]
            self.ast = ('Variable', p.ID)
            return self.ast
        except LookupError:
            print(f'Undefined name {p.ID!r}')
            return 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 parser.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        c_code = file.read()

    lexer = Tokenizer()
    parser = MyParser()

    result = parser.parse(lexer.tokenize(c_code))

    if parser.ast:
        print("Abstract Syntax Tree:")
        print(parser.ast)


    def generate_3_address_code(ast):
        if ast:
            if isinstance(ast, tuple):
                if ast[0] in ['Function Definition', 'Variable Assignment', 'Return Statement']:
                    print(ast[0], ast[1])
                    generate_3_address_code(ast[2])
                else:
                    print(ast[0], ast[1], ast[2], ast[3])
                    generate_3_address_code(ast[1])
                    generate_3_address_code(ast[2])
            elif isinstance(ast, int):
                print(ast)

    if parser.ast:
        print("3-Address Code:")
        generate_3_address_code(parser.ast)


