import Parser  # Import your parser.py
import Tokenizer  # Import your tokenizer.py

#used chat gpt for basic layout
def main():
    print("Compiler Construction")
    while True:
        print("Options:")
        print("A. Tokenizer")
        print("B. Parser")
        print("C. Exit")

        choice = input("Select an option:")

        if choice == "A":
            with open ("test.py") as file:
	            file_content = file.read()
            with open("tokens.txt", 'a') as tokens:
	            tokens.write(str(Token))
                
        #Still working on below this
        elif choice == "B":
            source_code = input("Enter code to Parse: ")
            ast = parser.parse(source_code)
            
        #Choose C to close program
        elif choice == "C":
            print("Thanks!")
            break
            
        #If an invalid option was inputed
        else:
            print("Error Choose doesn't exist")

if __name__ == "__main__":
    main()
