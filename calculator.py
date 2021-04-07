# Get information from the user about conversion
# TODO User input validation for menu
# TODO User input validation for number
# user input on the type of conversion
# Menu system 1-inches to mm 2-mm to inches
userConversionInput = input('What type of conversion? \n\t 1-inches to mm \n\t 2-mm to inches: \n')

userInput = input('What is the number: ')
print('Your number is:', userInput) # TODO remove for production
userNumber = float(userInput) 

def calculate(userNumber, conversionType):
    if conversionType == '1':
        userAnswer = userNumber * 25.4
    if conversionType == '2':
        userAnswer = userNumber / 25.4
    return userAnswer

calcValue = calculate(userNumber, userConversionInput)


# Print out the answer to user
print('The answer is:', calcValue)