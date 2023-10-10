#Compiler with different flag options for output
#Author Ben Hulsey
#Author Jacob Moore

#new  compiler source code with args parse.

import argparse


parser = argparse.ArgumentParser(description='Comand line interface for compiler.py')

parser.add_argument('-t', '--tokenizer', nargs='?', type=argparse.FileType('tokenizer.py'), help='tokenizer program')
parser.add_argument('-p', '--parser', nargs='?', type=argparse.FileType('parser.py'), help='parser program')


parser.print_usage()



#old compiler source code.

#import tokenizer
#import parser
#from pprint import pprint
#
#file_path = "test.c" #read in a file needs to be dynamic
#with open(file_path, "r") as file:
#        file_contents = file.read()
#
#def main():
#    print("Compiler Construction")
#    while True:
#        print("Options:")       # ask you if you want to use the tokenizer or parser
#        print("-t Tokenizer") 
#        print("-p Parser")
#        print("-q Quit")
#
#        choice = input("Select an option: ")
#
#
#        if choice == "-t":
#            data = file_contents
#            lexer = tokenizer.Tokenizer()
#            tokens = []
#            for tok in lexer.tokenize(data):    #outputs the tokenizer
#                tokens.append((tok.type, tok.value))
#            pprint(tokens)
#
#        elif choice == "-p":
#            data = file_contents
#            file_contents 
#            lexer = tokenizer.Tokenizer()
#            parsers = parser.MyParser()
#
#            try:
#                result = parsers.parse(lexer.tokenize(data))
#                print(result)
#            except SyntaxError as e:
#                print(e)
#
#        elif choice == "-q":
#            print("Thanks!")
#            break
#
#        else:
#            print("Error: Invalid option")
#
#if __name__ == "__main__":
#    main()
