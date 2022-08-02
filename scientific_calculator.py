# Inports the necessary modules
import math
import random 

def calculator():
    # contains the current version of the calculator
    calculator_version="1.1"

    # Introduction to calculator
    print("Welcome to Shubham's calculator!")
    print("This is currently a work in progress.")
    Name=input("Enter your name please:")
    print("Hello" + Name + "!")
    print("I hope you enjoy using this calculator:")

    #Display option for the user
    def options():
        print("\nOptions")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'more' to see a list of more operations avaliable")
        print("Enter 'info' for more information and help")
        print("Enter 'quit' to end the program")

    options()    

    # Allows calculator to be used
    while True:
        user_input = input("\nPlease input your command:")

        #Displays option again for the user
        if user_input == "option":
            pass
        
        #Display a list of more operation 
        elif user_input == "more":
            print("\nList of more operations")
            print("Enter 'powers' to raise a number to the power of another")
            print("Enter 'sqrt' to find the square root of the number ")
            print("Enter 'percent' to calculate percentage of a number ")
            print("Enter 'pi' to return value for pi")
            print("Enter 'e' to return value for e")
            print("Enter 'sin' to find sine of a number ")
            print("Enter 'cos' to find cosine of a number")
            print("Enter 'tan' to find tangent of the number")
            print("Enter 'rand' to return a random number between 0 to 1")
            print("Enter 'randint' to return a random number between two numbers")
            continue

        #Display more information for the user
        elif user_input == "info":
            print("\nInformation")
            print("Your name is currently saved as ' " + Name + '"')
            print("Enter 'name' to change your saved name ")
            print("Enter 'option' to view option again")
            print("If an error has occured it means you have not input the correct data type")
            print("You are able to use negative and decimal numbers in this calculator")
            print("More informaton and help coming soon")
            print("Current version: " + calculator_version)
            continue

        #Exits the user from the calculator
        elif user_input == "quit":
            print("\nThank you for using this calculator " + Name + "!")
            break

        #Allow user to change their saved name
        elif user_input == "name":
            change = ("\nWould you like to change your name? Yes or No: ")
            if change == "Yes":
                Name = input("Enter your name please:")
                print("Thank you" + Name + "!")
            elif change == "No":
                print("Okay"+Name + "!" )
            else:
                print("Unkown input")

        # Adds two numbers
        elif user_input == "add":
            try:
                num1 = float(input("Enter the first number:"))     
                num2 = float(input("Enter the second number:"))
                result = str(num1+num2)
                print("\nThe answer is" +  result)
            except (ValueError,TypeError):
                print("Error occurred")   

        # Subtract two numbers
        elif user_input == "subtract":
            try:
                num1 = float(input("Enter the first number:"))     
                num2 = float(input("Enter the second number:"))
                result = str(num1-num2)
                print("\nThe answer is" +  result)
            except (ValueError,TypeError):
                print("Error occurred")   

        # Multiplies two numbers
        elif user_input == "multiply":
            try:
                num1 = float(input("Enter the first number:"))     
                num2 = float(input("Enter the second number:"))
                result = str(num1*num2)
                print("\nThe answer is" +  result)
            except (ValueError,TypeError):
                print("Error occurred")  

        # Divides two numbers
        elif user_input == "divide":
            try:
                num1 = float(input("Enter the first number:"))     
                num2 = float(input("Enter the second number:"))
                result = str(num1/num2)
                print("\nThe answer is" +  result)
            except ZeroDivisionError:
                print("an error has occured due to zero division")    
            except (ValueError,TypeError):
                print("Error occurred")  

        #Finds the squre root of a number
        elif user_input == "sqrt":
            try:
                num1 = float(input("Enter a number:"))     
                result = str(math.sqrt(num1))
                print("\nThe answer is" +  result)
            except (ValueError,TypeError):
                print("Error occurred")   

        #Calculates percentage of a number
        elif user_input == "percent":
            try:
                num1 = float(input("Enter a number:"))     
                result = str(num1/100)
                print("\nThe answer is" +  result)
            except (ValueError,TypeError):
                print("Error occurred") 

        # Return value for pi
        elif user_input == "pi":
            result = str(math.pi)
            print("\nThe answer is " +  result)

        #Return value for e  
        elif user_input == "e":
            result=str(math.e)
            print("\nThe answer is" +  result)  

        # Finds the sine of a number
        elif user_input == "sin":
            try:
                num1 = float(input("Enter a number :"))
                result = str(math.sin(num1))
                print("\nThe answer is " +  result)    
            except(ValueError,TypeError):
                print("Error occured")

        # Finds the cosine of a number
        elif user_input == "cos":
            try:
                num1 = float(input("Enter a number :"))
                result = str(math.cos(num1))
                print("\nThe answer is " +  result)    
            except(ValueError,TypeError):
                print("Error occured")

        # Finds the tangent of a number
        elif user_input == "tan":
            try:
                num1 = float(input("Enter a number :"))
                result = str(math.tan(num1))
                print("\nThe answer is " +  result)    
            except(ValueError,TypeError):
                print("Error occured")

        #Return a random number between 0 to 1
        elif user_input == "rand":
            result = str(random.random())
            print("\nThe answer is " +  result)   

        #Return a random number between two numbers
        elif user_input == "randint":
            try :
                num1 = float(input("enter the first number:"))    
                num2 = float(input("enter the second number:"))
                result = str(random.randint(num1,num2))
                print("\nThe answer is " +  result)
            except (ValueError,TypeError):
                print("An error occurred")  

        # Is displayed when an unkown input is entered
        else:
            print("Unknown input")

        # Displays the option for the user 
        options()

# Runs the calculator
calculator()            
