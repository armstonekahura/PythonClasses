conversionUnit = 129
currencyName = "Ksh"


def usd_to_ksh (amount):
    return (f"{amount} USD is equal to {currencyName}.{amount * conversionUnit}.")
    

def validate_and_execute():
    try:
        userInputNumber = int(userInput)
        if userInputNumber > 0:
             converted_usd_to_ksh = usd_to_ksh(userInputNumber)
             print(converted_usd_to_ksh)
        elif userInputNumber == 0:
            print("⚠️  You entered a 0, kindly input a valid amount")
    except ValueError:
        print("\n⚠️   You didn't insert a number as the amount")
 

userInput = input ("Kindly insert amount in Dollars to be converted. \nAmount    :   ")
validate_and_execute()

