conversionUnit = 129
currencyName = "Ksh"


def usd_to_ksh (amount):
    return (f"{amount} USD is equal to {currencyName}.{amount * conversionUnit}.")


my_var = usd_to_ksh(400)
print (my_var)