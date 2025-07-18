conversionUnit = 129
currencyName = "Ksh"


def usd_to_ksh (amount):
    if amount > 0:
        return (f"{amount} USD is equal to {currencyName}.{amount * conversionUnit}.")


userInput = input ("Kindly insert amount in Dollars to be converted. \nAmount    :   ")
userInputNumber = int (userInput)
converted_usd_to_ksh = usd_to_ksh(userInputNumber)

print(converted_usd_to_ksh)