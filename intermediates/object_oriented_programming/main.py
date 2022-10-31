from Invoice import InvoiceCalculator as Invoice
import datetime
import random

from prettytable import PrettyTable


if __name__ == "__main__":
    
    # collect invoice details
    print("-------- COMPANY DETAILS --------")
    receipt_no = random.random()
    company_name = input("Enter your company name: ")
    company_address = input("Enter your company address: ")
    company_phone_number = input("Enter your company phone number: ")
    company_attendant = input("Enter attendant name: ")
    purchased_date = datetime.datetime.now()
    

    # instance object
    receipt = Invoice(receipt_no,company_name,company_address,company_phone_number,purchased_date,company_attendant)


    # create a table
    table = PrettyTable(["QTYS", "ITEMS", "UNITS", "AMOUNTS"])

    print("-------- PRODUCTS DETAILS --------")
    while True:
        item = input("Enter product name: ")

        if item != 'q':
            qty = int(input("Enter quantity: "))
            unit = float(input("Enter price of the item: "))
            amount = qty * unit

            # add a row
            table.add_row([qty, item, unit, amount])
            receipt.total_amount += amount
        elif item == 'q':
            break
    
    # add total amount row
    table.add_row(["TOTAL",None, None, amount])
    
    # reciept details
    print("\n")
    print("-------- RECEIPT --------")
    # display company profile
    receipt.display_company_details()

    # display table
    print(table)

    print('\nThanks for shopping with us :)')
    print('Your total bill amount is ', amount, '/-')



    