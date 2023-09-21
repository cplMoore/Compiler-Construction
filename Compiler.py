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
	
	#if you choose tokenizer
        if choice == "-t":
            for tok in lexer.tokenize(data):
	   	tokens.append((tok.type, tok.value))
                
        #if you select parser
        elif choice == "-p":
            result = parser.parse(file_content)
		print(result)
            
        #Choose Exit to close program
        elif choice == "-q":
            print("Thanks!")
            break
            
        #If an invalid option was inputed
        else:
            print("Error Choose doesn't exist")

if __name__ == "__main__":
    main()
