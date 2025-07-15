conversionUnit = 129
currencyName = "Ksh"


def usd_to_ksh (amount):
    return (f"{amount} USD is equal to {currencyName}.{amount * conversionUnit}.")


userInput = input ()