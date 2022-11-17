from currency_api import CurrencyAPI
import config


def main():
    currency_api = CurrencyAPI(config.CURRENCY_DATA_API_KEY)
    print("""
Welcome to the Currency Kingdom
What are you want to do?
    1) Convert from Currency to Another Currency.
    2) Check if currency exist.
    3) Exit
""")

    option_chose = input("What option do you want to choose? ")
    match option_chose:
        case "1":
            from_currency = input("From Currency: ")
            to_currency = input("To Currency: ")
            amount = input("Amount: ")
            print(currency_api.convert_currency(from_currency, to_currency, int(amount)))

        case "2":
            currency_name = input("Currency name: ")
            result = currency_api.is_currency_exist(currency_name)
            if result:
                print(f"{result} = {currency_name}")
            else:
                print("Not exists!")

        case "3":
            print("Bye Bye.")


if __name__ == '__main__':
    main()
