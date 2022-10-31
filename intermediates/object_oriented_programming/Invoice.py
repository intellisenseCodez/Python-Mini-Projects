
class InvoiceCalculator:

    total_amount = 0

    def __init__(self, number, name, address, phone_number, date, attendant, ):
        self.number = number
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.date = date
        self.attendant = attendant

    def totalAmount(self, **args):
        for arg in args:
            self.total_amount += arg
        return self.total_amount

    def display_company_details(self,):
        print(f"            {self.name.upper()}")
        print(f"            {self.address.upper()}")
        print(f"            {self.phone_number}\n")
        print(f"CHECK#: {self.number}")
        print(f"DATE/TIME: {self.date}")
        print(f"ATTENDANT: {self.attendant.upper()}")
    

