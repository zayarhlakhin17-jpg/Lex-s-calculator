print("Welcome to Lex's Calculator")
while True:
    try:
        #STEP1: INPUT NUM
        num1=float(input("Enter the first number : "))
        num2=float(input("\nEnter the second number : "))


        #STEP2: INPUT OPERATOR
        print("Choose an operator: +, -, *, /, %, **")
        operator = input("\nFirst Operator : ")


        
    
    
        if operator == "+" and "-":
            result = (num1 + num2 )


        elif operator == "-" :
            result = (num1 - num2) 


        elif operator == "*" :
            result = (num1 * num2)

        elif operator == "/" :
            if num2 != 0:
                result = (num1 / num2)
            else:
                result = "Error! Cannot divide by zero"
        elif operator == "%":
            result = num1 % num2
        
        elif operator == "**":
            result = num1 ** num2
        
        else:
            result = "Invalid operator!"
        

        #STEP3: SHOW RESULT
        print("\nResult : ", result)

    except ValueError:
        print("\nInvalid input! Please enter numberic valuess")
    

    #STEP5: ASK USERS TO CONTINUE
    again = input("Do you want to calculate again? ")
    if again != "yes":
        print("Thank you for using calculator.")
        break

