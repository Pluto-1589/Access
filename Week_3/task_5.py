from decimal import Decimal, ROUND_HALF_UP
import math


# Standard tax rate is 8.1%
def standard_tax(amount):
    return float(Decimal(amount) * Decimal("0.081"))


# Reduced tax rate is 2.5%
def reduced_tax(amount):
    return float(Decimal(amount) * Decimal("0.025"))


# Accommodation tax rate is 3.7%
def accommodation_tax(amount):
    return float(Decimal(amount) * Decimal("0.037"))


# Helper function to round the tax to the nearest 0.05 increment.
def round_tax(tax):

    tax = Decimal(tax)
    return tax.quantize(Decimal("0.05"), rounding=ROUND_HALF_UP)


# Main function
def calculate_tax(amount, tax_type):

    if amount <= 0:
        return 0.0

    tax = tax_type(amount)
    tax = round_tax(tax)
    return tax


print(calculate_tax(101, standard_tax))
print(calculate_tax(101, reduced_tax))
print(calculate_tax(101, accommodation_tax))
