# compiler.py

import parser  # Import your parser module
import tokenizer  # Import your tokenizer module

def main():
    print("Welcome to our Compiler Project!")
    while True:
        print("Choose an option:")
        print("1. Tokenize")
        print("2. Parse")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            source_code = input("Enter the source code to tokenize: ")
            tokens = tokenizer.tokenize(source_code)
            print("Tokens:")
            for token in tokens:
                print(token)
        elif choice == "2":
            source_code = input("Enter the source code to parse: ")
            ast = parser.parse(source_code)
            print("Abstract Syntax Tree (AST):")
            print(ast)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

