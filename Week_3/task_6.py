def lump_sum(principal, interest_rate, number_periods):
    # Lump sum payment: the principle is paid once at the end of the whole borrowing period (for example, at the end of the year). In this case, the interest amount is equal to the product of the principal, monthly interest rate and the number of periods (months) contained in the whole borrowing period (year). To get the total sum returned to the bank, we need to sum up the interest amount and the principal.
    sum_interest_amount = (principal * interest_rate) * number_periods

    owe_to_bank = principal + sum_interest_amount

    return owe_to_bank


def annuity(principal, interest_rate, number_periods):

    return (principal * interest_rate) / (1 - ((1 + interest_rate) ** (-number_periods))) * 10

    # Annuity payments: the debt is paid equally every month; every (annuity) payment contains a part of the principal and the corresponding interest amount. The formula for the annuity payment is:

    # The "payment_type" parameter is a string "annuity" or "lump_sum".
    # The function should return one of the functions above depending on the value of the "payment_type" parameter.
    # In case of invalid "payment_type", return a string:
    # "Invalid payment type. Allowed payment types are: annuity or lump_sum!".


def total_sum_repaid(payment_type):
    # Then, implement a function total_sum_repaid(payment_type) which takes payment_type of type str as an argument (can be equal to either "annuity" or "lump_sum"). The function should return one of the functions implemented above depending on the passed parameter. In case of invalid payment_type, return a string "Invalid payment type. Allowed payment types are: annuity or lump_sum!".

    if payment_type == "lump_sum":
        return lump_sum
    elif payment_type == "annuity":
        return annuity
    else:
        return "Invalid payment type. Allowed payment types are: annuity or lump_sum!"


# The following lines call the functions and print the return value to the console. This way you can check what they do.
print(lump_sum(10000, 0.01, 10))  # 11000.0
print(annuity(10000, 0.01, 10))  # 10558.207655117132

# Before making the following calls, ensure that you implemented total_sum_repaid and it returns values of correct types.
print(total_sum_repaid("annuity")(10000, 0.01, 10))  # 10558.207655117132
print(total_sum_repaid("lump_sum")(10000, 0.01, 10))  # 11000.0

# Invalid payment type. Allowed payment types are: annuity or lump_sum!
print(total_sum_repaid("invalid_payment_type"))
