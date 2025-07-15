conversionUnit = 129
currencyName = "Ksh"


def usd_to_ksh (amount):
    print (f"\n ---------------CONVERTING {amount} USD into KSH---------------")
    print (f"|              {amount} USD is equal to {currencyName}.{amount * conversionUnit}.              |")
    print ("-----------------------------------------------------------")


input("\n Kindly enter amount to be converted into Kenya shillings! ")