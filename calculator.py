# Get information from the user about conversion
# TODO User input validation for menu
# TODO User input validation for number
# user input on the type of conversion
# Menu system 1-inches to mm 2-mm to inches

def MMToin(userNumber):
    return userNumber / 25.4

def inToFt(userNumber):
    return userNumber / 12

def inToMM(userNumber):
    return userNumber * 25.4
        
def printResults(userConversionInput, userNumber):
    if userConversionInput == '1':
        #set first value to in and second value to mm
        conversionUnit = 'in'
        convertedUnit = 'mm'
        calcValue = inToMM(userNumber)
    if userConversionInput == '2':
        #set first value to mm and second value to in
        conversionUnit = 'mm'
        convertedUnit = 'in'
        calcValue = MMToin(userNumber)
    if userConversionInput == '3':
        #set first value to in and second value to ft
        conversionUnit = 'in'
        convertedUnit = 'ft'
        calcValue = inToFt(userNumber)
    print('Conversion --> ', userNumber, conversionUnit, '=', calcValue, convertedUnit)




while True:
    userConversionInput = input('What type of conversion? \n\t 1-inches to mm \n\t 2-mm to inches: \n\t 3-inches to feet\n\t Q-to Quit')
    if userConversionInput == 'Q':
        break
    userInput = input('What is the number: ')
    userNumber = float(userInput)  
    printResults(userConversionInput,userNumber)













