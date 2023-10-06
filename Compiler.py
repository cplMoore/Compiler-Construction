# Compiler main for COMP 5210 compiler project.
# Author: Ben Hulsey
# Author: Jacob Moore

import tokenizer
import parser

file_path = "test.py" #read in a file 
with open(file_path, "r") as file:
        file_contents = file.read()

def main():
    print("Compiler Construction")
    while True:
        print("Options:")       # ask you if you want to use the tokenizer and the or parser
        print("-t Tokenizer") 
        print("-p Parser")
        print("-q Exit")

        choice = input("Select an option: ")

        if choice == "-t":
            data = file_contents
            lexer = tokenizer.Tokenizer()
            tokens = []
            for tok in lexer.tokenize(data):    #outputs the tokenizer
                tokens.append((tok.type, tok.value))
            print(tokens)

        elif choice == "-p":
            data = file_contents
            file_contents 
            lexer = tokenizer.Tokenizer()
            parsers = parser.MyParser()

            try:
                result = parsers.parse(lexer.tokenize(data))
                print(result)
            except SyntaxError as e:
                print(e)

        elif choice == "-q":
            print("Thanks!")
            break

        else:
            print("Error: Invalid option")

if __name__ == "__main__":
    main()
