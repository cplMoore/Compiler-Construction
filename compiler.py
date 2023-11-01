# Compiler with different flag options for output
# Author Ben Hulsey
# Author Jacob Moore
 
import argparse
import subprocess

# JM: had a hard time with trying to call the programs with argparse. 
# ChatGPT recommended using the subprocess module to run the programs.
if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='Command line interface for compiler.py. Intakes .c files.',
                                     epilog='War Eagle!')
    
    # Positional Arguments.
    # Must intake a .c file.
    parser.add_argument('input_file', help='Input a .c file')

    # Optional Arguments
    # Flags for command line interface and what they will do.
    parser.add_argument('-t', '--tokenizer', action='store_true', help='tokenizer program')
    parser.add_argument('-p', '--parser', action='store_true', help='parser program')
    parser.add_argument('-o', '--optimize', action='store_true', help='optimizer program')
    args = parser.parse_args()
    
    if args.tokenizer:
        #Call tokenizer.py and outputs tokens.
        subprocess.run(['python3', 'tokenizer.py', args.input_file], check=True, capture_output=False)
    
    elif args.parser:
        # Call parser.py
        subprocess.run(['python3', 'parser.py', args.input_file], check=True, capture_output=False)
