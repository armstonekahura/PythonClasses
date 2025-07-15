conversionUnit = 129
currencyName = "Ksh"


def usd_to_ksh (amount):
    print (f"\n ---------------CONVERTING {amount} USD into KSH---------------")
    print (f"|              {amount} USD is equal to {currencyName}.{amount * conversionUnit}.              |")
    print ("-----------------------------------------------------------")


def scope_check (amount):
    myVar = "Variable inside a function"
    print (f"Global Variable: {conversionUnit}")
    print (f"Local Variable: {amount}")

scope_check(20)