# 'def' keyword used to define a function We can call the function whatever we want, but it must obey python naming
# rules (no spaces, start with a letter, only letters, numbers and underscores) Also, try to name it something
# different to any of your variables. Python lets you do this, but it doesn't mean you should!
# 'return' keyword comes before the value to be returned.
# Here, the returned value is the result of the expression to the right of 'return'
# All statements that are part of the function are indented. Python REQUIRES THIS. Its part of the syntax!
# 'price' is a single parameter, it's the input required for the function to do its job
def add_vat(price):
    return price * 1.2


# So far, we have only defined the function to be used. Actual program execution starts here.
# Note that this code is in the global execution scope (i.e. it's not indented).
# Because the function we defined returns a value, we can assign a variable, 'twenty_quid_plus_vat', to a call to it.
# We are passing in the value of '20' as the parameter to be used for 'price'.
twenty_quid_plus_vat = add_vat(20)
print(twenty_quid_plus_vat)


# This function has 2 parameters, price and vat. It can be used to add vat of the caller's choosing.
# Note that when we call it, we will need to pass in price and vat in the same order as they are defined in the function
def add_specific_vat(price, vat):
    return price * (1 + (vat / 100))


twenty_quid_plus_old_vat = add_specific_vat(20, 17.5)
print(twenty_quid_plus_vat)


# This example shows how some function params can have a default.
# Default params to not need to be passed by the caller
# Default params need to come after any non-default params (e.g. after 'price') in the comma separated list
# This is because python will not know which params have been provided
def add_specific_vat_with_default(price, vat=20.0):
    return price * (1 + (vat / 100))


print(add_specific_vat_with_default(5))  # Use the default vat
print(add_specific_vat_with_default(5, 17.5))  # Provide 17.5 as the vat


# I actually lied about needing to provide params in order!
# You can provide in any order but must use the following syntax:
print(add_specific_vat_with_default(vat=17.5, price=5))
