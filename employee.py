"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, contract, comission=""):
        self.name = name
        self.contract = contract
        self.comission = comission

    def get_pay(self):
        comission_pay = 0
        if self.comission:
            comission_pay = self.comission.get_pay()
        return comission_pay + self.contract.get_pay()

    def __str__(self):
        return f"{self.name} works on a {self.contract}{self.comission}. Their total pay is {self.get_pay()}."


class MonthlyContract:
    def __init__(self, salary):
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f"monthly salary of {self.salary}"


class HourlyContract:
    def __init__(self, hourly_wage, hours_worked):
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_wage * self.hours_worked

    def __str__(self):
        return f"contract of {self.hours_worked} hours at {self.hourly_wage}/hour"


class FixedComission:
    def __init__(self, comission):
        self.comission = comission

    def get_pay(self):
        return self.comission

    def __str__(self):
        return f" and receives a bonus commission of {self.comission}"


class BonusComission:
    def __init__(self, contracts_landed, comission_per_contract):
        self.contracts_landed = contracts_landed
        self.comission_per_contract = comission_per_contract

    def get_pay(self):
        return self.contracts_landed * self.comission_per_contract

    def __str__(self):
        return f" and receives a commission for {self.contracts_landed} contract(s) at {self.comission_per_contract}/contract"


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", MonthlyContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", HourlyContract(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", MonthlyContract(3000), BonusComission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", HourlyContract(25, 150), BonusComission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", MonthlyContract(2000), FixedComission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", HourlyContract(30, 120), FixedComission(600))
