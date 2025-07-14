conversionUnit = 129
currencyName = "Ksh"


def usd_to_ksh(amount):
    print ("\n ---------------CONVERTING USD into KSH---------------")
    print (f"|          {amount} USD is equal to {currencyName}.{amount * conversionUnit}.              |")
    print ("------------------------------------------------------")


usd_to_ksh(23)