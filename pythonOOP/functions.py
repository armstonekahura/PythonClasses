conversionUnit = 129
currencyName = "Ksh"
amount = 100


def usd_to_ksh():
    print (f"{amount} USD is equal to {currencyName}.{amount * conversionUnit}.")


usd_to_ksh()