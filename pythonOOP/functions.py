conversionUnit = 129
currencyName = "Ksh"


def usd_to_ksh(amount):
    print (f"\n ---------------CONVERTING {amount} USD into KSH---------------")
    print (f"|              {amount} USD is equal to {currencyName}.{amount * conversionUnit}.              |")
    print ("-----------------------------------------------------------")


usd_to_ksh(20)
usd_to_ksh(100)
usd_to_ksh(4025)
usd_to_ksh(12650)