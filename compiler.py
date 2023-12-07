# Compiler with different flag options for output
# Author Ben Hulsey
# Author Jacob Moore
 

import argparse
from tokenizer import Tokenizer
from my_parser import MyParser
from TAC import TACGenerator
from optimizer import Optimizer
from amble import PreamblePostambleGenerator
from X import X86CodeGenerator
import pprint

lexer = Tokenizer()
my_parser = MyParser()
tac = TACGenerator()
opt = Optimizer()
preamble = PreamblePostambleGenerator()
postamble = PreamblePostambleGenerator()
xasm = X86CodeGenerator()

ppar = pprint.PrettyPrinter(indent=4, width=45)
ptac = pprint.PrettyPrinter(indent=4, width=25)
popt = pprint.PrettyPrinter(indent=4, width=50)



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
parser.add_argument('-3c', '--tac', action='store_true', help='This flag should print out the Three Address Code.')
parser.add_argument('-o', '--optimizer', action='store_true', help='optimizer program')
parser.add_argument('-a', '--amble', action='store_true', help='Calling conventions')
parser.add_argument('-x', '--x86', action='store_true', help='Print X86 assembly language.')
    
args = parser.parse_args()

c_code = args.input_file.read()

tokens = lexer.tokenize(c_code)

if args.tokenizer:
    for token in iter(tokens):
        print(token)  
      
ast = my_parser.parse(tokens)

if args.parser:
    ppar.pprint(ast)
 
tac_code = tac.generate_tac(ast)

if args.tac:
    ptac.pprint(tac_code)
    

if args.optimizer:
    opt_code = opt.optimize(tac_code)
    popt.pprint(opt_code)
    
if args.amble:
    cc = preamble.generate_tac_with_preamble_postamble(tac_code)
    print(cc)
    
if args.x86:
    asm = xasm.generate_x86_code(tac_code)
    print(asm)
    


