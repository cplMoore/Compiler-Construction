#Compiler.py for COMP 5210 project.
#Author Ben Hulsey
#Author Jacob Moore


import Parser  # Import your parser.py
import Tokenizer  # Import your Tokenizer.py

#used chat gpt for basic layout
def main():
    print("Compiler Construction")
    while True:
        print("Options:")
        print("-t Tokenizer")
        print("-p Parser")
        print("-q Exit")

        choice = input("Select an option:")

        if choice == "-t":
            with open ("test.c") as file:
	            file_content = file.read()
            with open("tokens.txt", 'a') as tokens:
	            tokens.write(str(Token))
                
        #Still working on below this
        elif choice == "-p":
            source_code = input("Enter code to Parse: ")
            ast = parser.parse(source_code)
            
        #Choose C to close program
        elif choice == "-q":
            print("Thanks!")
            break
            
        #If an invalid option was inputed
        else:
            print("Error Choose doesn't exist")

if __name__ == "__main__":
    main()
