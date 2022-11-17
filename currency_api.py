import requests
import datetime


class CurrencyAPI:
    def __init__(self, api_key):
        self.payload = {}
        self.header = {
            "apikey": api_key
        }

    def convert_currency(self, from_currency="USD", to_currency="ILS", amount=1):
        url = f"https://api.apilayer.com/currency_data/convert?to={to_currency.upper()}&from={from_currency.upper()}&amount={amount}"
        response = requests.request("GET", url, headers=self.header, data=self.payload).json()
        amount_converted = response["result"]
        return amount_converted

    def is_currency_exist(self, currency_name="USD"):
        url = "https://api.apilayer.com/currency_data/list"
        response = requests.request("GET", url, headers=self.header, data=self.payload).json()
        currency_name = currency_name.upper()
        if currency_name in response["currencies"]:
            full_currency_name = response["currencies"][currency_name]
            return full_currency_name
        else:
            return False

    def convert_specific_date_currency(self, from_currency="USD", to_currency="ILS", amount=1, date=datetime.date.today()):
        url = f"https://api.apilayer.com/currency_data/convert?to={to_currency}&from={from_currency}&amount={amount}\
        &date={date}"
        response = requests.request("GET", url, headers=self.header, data=self.payload).json()
        print(response)



