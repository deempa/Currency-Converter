from tkinter import *
import config
import requests
from currency_api import CurrencyAPI
from customtkinter import *


def main():
    response = requests.request("GET", r"https://api.exchangerate-api.com/v4/latest/USD").json()
    current_list = list(response["rates"].keys())
    currency_api = CurrencyAPI(config.CURRENCY_DATA_API_KEY)

    def convert():
        amount = from_entry.get()
        from_currency = from_currency_box.get()
        to_currency = to_currency_box.get()
        converted_amount = currency_api.convert_currency(from_currency, to_currency, amount)
        to_label_amount.configure(text=converted_amount, font=('Arial', 20))

    window = Tk()
    window.resizable(width=FALSE, height=FALSE)
    window.geometry('500x300')
    window.title("Currency Convertor")
    set_default_color_theme("green")

    logo = Label(text="Currency Convertor", font=('Arial', 35))
    logo.pack(pady=30)

    from_label = Label(window, text="From", font=('Arial', 20))
    from_label.place(x=130, y=100)

    from_entry = CTkEntry(width=100, bg="white", fg="black", justify="center",
                                        placeholder_text="Enter Amount")
    from_entry.place(x=108, y=160)

    to_label = Label(window, text="To", font=('Arial', 20))
    to_label.place(x=350, y=100)

    to_label_amount = CTkLabel(window, text="Result Here", text_font=('Arial', 20), justify="center")
    to_label_amount.place(x=310, y=160)

    choices = current_list
    variable = StringVar()
    variable.set(choices[0])
    combobox_var = StringVar(value="ILS")
    from_currency_box = CTkComboBox(values=choices, width=100)
    to_currency_box = CTkComboBox(values=choices, width=100, variable=combobox_var)
    from_currency_box.place(x=108, y=130)
    to_currency_box.place(x=330, y=130)

    convert_button = CTkButton(text="Convert", text_font=('Arial', 22), width=200, height=50, command=convert)
    convert_button.place(x=150, y=230)

    window.mainloop()


if __name__ == '__main__':
    main()
