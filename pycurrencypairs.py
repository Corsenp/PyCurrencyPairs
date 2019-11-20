from forex_python.converter import CurrencyRates
import sys

def prompt_rates_for_one_currency(rates, base_currency, currencies):
    print("\n%s :\n" % base_currency)
    for currency in currencies:
        try:
            print("%s %s" % (currency, rates.get_rate(base_currency, currency)))
        except:
            print("N/A")

def get_currencies(rates):
    currencies = []
    for argument in sys.argv:
        if len(argument) == 3:
            try:
                rates.get_rates(argument)
                currencies.append(argument)
            except:
                continue
    
    print('----')
    print(currencies)
    print('----')
    return currencies

def get_exchange_rate(currencies, rates):
    for currency in currencies:
        prompt_rates_for_one_currency(rates, currency, currencies)
          
def main():
    rates = CurrencyRates()
    currencies = get_currencies(rates)

    get_exchange_rate(currencies, rates)

main()