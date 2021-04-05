# Get information from the user about conversion
# TODO User input validation for menu
# TODO User input validation for number
# user input on the type of conversion
# Menu system 1-inches to mm 2-mm to inches
userConversionInput = input('What type of conversion? \n\t 1-inches to mm \n\t 2-mm to inches: \n')

userInput = input('What is the number: ')
print('Your number is:', userInput) # TODO remove for production
userNumber = float(userInput) 

# Perform the conversion
# Convert in to mm 25.4 mm in every 1 in

#Conditional statement that determines 1 or 2
if userConversionInput == '1':
    # Convert from in to mm (userNumber * 25.4) (1 * 25.4) = 25.4 mm
    print ('in to mm')
    userAnswer = userNumber * 25.4
if userConversionInput == '2':
    # Convert from mm to in (userNumber/ 25.4 ) 1/25.4 = 0.394
    print ('mm to in')
    userAnswer = userNumber/25.4

# Print out the answer to user
print('The answer is:', userAnswer)