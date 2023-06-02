from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "66d581e071500056f753"

printer = PrettyPrinter()

def get_currencies():

    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()

    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']

        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(curr1, curr2):
    endpoint = f"api/v7/convert?q={curr1}_{curr2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)

    data = response.json()

    if len(data) == 0:
        print("Invalid currencies.")
        return

    rate = list(data.values())[0]
    print(f"{curr1} to {curr2} = {rate}")

    return rate

def convert(curr1, curr2, amount):
    rate = exchange_rate(curr1, curr2)
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return
    
    converted_amount = rate * amount

    print(f"{amount} {curr1} is equal to {converted_amount} {curr2}")
    return converted_amount
    
def main():
    currencies = get_currencies()

    print("Currency Converter")
    print("List - list all the currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            curr1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {curr1}: ")
            curr2 = input("Enter a currency to convert to: ").upper()
            convert(curr1, curr2, amount)
        elif command == "rate":
            curr1 = input("Enter a base currency: ").upper()
            curr2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(curr1, curr2)
        else:
            print("Invalid command.")

main()