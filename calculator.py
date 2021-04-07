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

def printResults(userConversionInput, userInput, calcValue):
    if userConversionInput == '1':
        #set first value to in and second value to mm
        conversionUnit = 'in'
        convertedUnit = 'mm'
    if userConversionInput == '2':
        #set first value to mm and second value to in
        conversionUnit = 'mm'
        convertedUnit = 'in'
    print('The answer is: ', userInput, conversionUnit, '=', calcValue, convertedUnit)

calcValue = calculate(userNumber, userConversionInput)
printResults(userConversionInput,userInput, calcValue)


# Print ex: The answer is 1 in = 25.4mm or 2 in = 50.8 mm











