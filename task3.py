from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * rate
    return converted_amount

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (e.g., USD, EUR, GBP): ").upper()
to_currency = input("Enter the currency to convert to (e.g., USD, EUR, GBP): ").upper()

result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")
