# Compiler with different flag options for output
# Author Ben Hulsey
# Author Jacob Moore
 

import argparse
from tokenizer import Tokenizer
from my_parser import MyParser
from tac import TAC
import optimizer
import pprint

lexer = Tokenizer()
my_parser = MyParser()
pp = pprint.PrettyPrinter(indent=4, width=45)

parser = argparse.ArgumentParser(prog='compiler.py',
                                 description='Command line interface for compiler.py that will intake a .c file.',
                                 epilog='War Eagle!')
    
# Positional Arguments.
# Must intake a .c file.
parser.add_argument('input_file', metavar='input.c', nargs='?', type=argparse.FileType('r'),
                    help='Input a .c file')

# Optional Arguments
# Flags for command line interface and what they will do.
parser.add_argument('-t', '--tokenizer', action='store_true', help='tokenizer program')
parser.add_argument('-p', '--parser', action='store_true', help='parser program')
parser.add_argument('-a', '--tac', action='store_true', help='This flag should print out the Three Address Code.')
parser.add_argument('-o', '--optimizer', action='store_true', help='optimizer program')
    
args = parser.parse_args()

c_code = args.input_file.read()


tokens = lexer.tokenize(c_code)



if args.tokenizer:
    for token in iter(tokens):
        print(token)  
      
ast = my_parser.parse(tokens)
if args.parser:
    pp.pprint(ast)
     
    
ir = generate_3_address_code(ast)
if args.tac:
    print(ir)


