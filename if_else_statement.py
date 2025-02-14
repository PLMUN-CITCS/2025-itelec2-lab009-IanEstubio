# IAN JAY P. ESTUBIO 
# Week 04 - Conditional Statements
# Laboratory # 09 - Guided Coding Exercise: Simple if Statement in Python

def main():
    """Main function to check the if the number is even or odd."""

    user_input = input("Enter a number: ")
    
    try:
        
    
       number = int(user_input)
    

        #code here
       if number % 2 == 0:
           print("The number", number, "is Even.")
       else:
           print("The number", number, "is Odd.")
             
    except ValueError:
           print("Invalid input. Please enter an integer.")
    
if __name__ == "__main__":
    main()
