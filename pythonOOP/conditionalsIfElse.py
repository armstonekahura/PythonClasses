conversionUnit = 129
currencyName = "Ksh"


def usd_to_ksh (amount):
    if amount > 0:
        return (f"{amount} USD is equal to {currencyName}.{amount * conversionUnit}.")
    elif amount == 0:
        return "⚠️  You entered a 0, kindly input a valid amount"
    

def validate_and_execute():
    if userInput.isdigit():
        userInputNumber = int (userInput)
        converted_usd_to_ksh = usd_to_ksh(userInputNumber)
        print(converted_usd_to_ksh)
    else:
        print("⚠️   You didn't insert a number as the amount")
 

userInput = input ("Kindly insert amount in Dollars to be converted. \nAmount    :   ")
validate_and_execute()

