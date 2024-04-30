#Prompt user for 1st number

var1 = int(input("Input 1st number: "))

#Promt user for 2nd number

var2 = int(input("Input 2st number: "))

#Promt user for the operation

operation = input("Input operation ( + , - , * , / ) : ")

if operation == '+':
    result = var1 + var2
elif operation =='-':
    result = var1-var2
elif operation =='*':
    result = var1*var2
elif operation == '/':
    # check for division by zero
    if var2 !=0:
        result = var1 / var2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"

print("\nResult : ", result)

