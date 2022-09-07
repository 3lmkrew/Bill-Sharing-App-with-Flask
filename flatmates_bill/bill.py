# This is the bill & Roommate classes (OOP)

class Bill:
    """
    object that contains data about a bill, such as
    total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

    def __str__(self):
        return f"Total amount {self.amount} for period of {self.period}"


class Roommate:
    """
    Creates a roommate (person) who lives in the hose
    and pays a share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pay_rate(self, bill, roommate):
        return round ((self.days_in_house / (self.days_in_house + roommate.days_in_house)) * bill.amount, 2)

