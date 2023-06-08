class Ticket:

    def __init__(self, number, price, show, time, ticket_holder):
        self.number = number
        self.price = price
        self.show = show
        self.time = time
        self.ticket_holder = ticket_holder

    def update_price(self, new_price):
        self.price = new_price

    def update_time(self, new_time):
        self.time = new_time

    def update_ticket_holder(self, new_ticket_holder):
        self.ticket_holder = new_ticket_holder

    def print_ticket(self):
        print(f"Ticket number: {self.number}\n"
              f"Ticket holder: {self.ticket_holder}\n"
              f"Show: \n{self.show}\n"
              f"Time : {self.time}\n"
              f"Price: £{self.price}")
        


class Calculator:

    def plus(num1, num2):
        pass

    def minus(num1, num2):
        pass

    def multiply(num1, num2):
        pass

    def convert_meter_to_yard(value):
        pass
