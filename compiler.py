#Compiler with different flag options for output
#Author Ben Hulsey
#Author Jacob Moore

import parser 
import argparse
import subprocess


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='Comand line interface for compiler.py. Intakes .c files.')
    
    # Positional Arguments.
    # Must intake a .c file.
    parser.add_argument('input_file', help='Input a .c file')

    # Optional Arguments
    # Flags for command line interface and what they will do.
    parser.add_argument('-t', '--tokenizer', action='store_true', default='tokenizer.py', help='tokenizer program')
    parser.add_argument('-p', '--parser', action='store_true', default='parser.py',help='parser program')
    



    args = parser.parse_args()
    if args.tokenizer:
        #Call tokenizer.py and outputs tokens.
        subprocess.run(['python3', 'tokenizer.py', args.input_file], check=True)
    
    elif args.parser:
        # Call parser.py
        subprocess.run(['python3', 'parser.py', args.input_file], check=True)
    
  
