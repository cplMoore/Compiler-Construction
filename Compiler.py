#Compiler.py for COMP 5210 project.
#Author Ben Hulsey
#Author Jacob Moore

import tokenizer
import parser

def main():
    print("Compiler Construction")
    while True:
        print("Options:")
        print("-t Tokenizer")
        print("-p Parser")
        print("-q Exit")

        choice = input("Select an option: ")

        if choice == "-t":
            data = "1 + 2 * (3 - 4)"  # Replace with your code to tokenize
            lexer = tokenizer.Tokenizer()
            tokens = []
            for tok in lexer.tokenize(data):
                tokens.append((tok.type, tok.value))
            print(tokens)

        elif choice == "-p":
            data = "1 + 2 * (3 - 4)"  # Replace with your code to parse
            lexer = tokenizer.Tokenizer()
            parsers = parser.MyParser() 
            result = parsers.parse(lexer.tokenize(data))
            print(result)

        elif choice == "-q":
            print("Thanks!")
            break

        else:
            print("Error: Invalid option")

if __name__ == "__main__":
    main()
