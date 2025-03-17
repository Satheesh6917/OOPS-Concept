# Base Bank Account

class BaseBankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BaseBankAccount):
    def __init__(self, account_number, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest earned: {interest}")
        return interest


class CurrentAccount(BaseBankAccount):
    def __init__(self, account_number, balance=0.0, min_balance=500):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() - self.min_balance:
            super().withdraw(amount)
        else:
            print("Withdrawal denied. Minimum balance requirement not met.")


savings = SavingsAccount("SA12345", 1000, 0.05)
savings.deposit(500)
savings.withdraw(200)
savings.calculate_interest()

current = CurrentAccount("CA67890", 1000, 500)
current.deposit(1000)
current.withdraw(1200)
current.withdraw(400)


# Employee Management

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.calculate_salary()}"


class RegularEmployee(Employee):
    def __init__(self, name, base_salary, benefits=0):
        super().__init__(name, base_salary)
        self.benefits = benefits

    def calculate_salary(self):
        return self.base_salary + self.benefits


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Manager(Employee):
    def __init__(self, name, base_salary, bonus=0):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


regular_emp = RegularEmployee("Satheesh", 90000, 10000)
contract_emp = ContractEmployee("Pawan", 100, 900)
manager = Manager("Ruthvik", 90000, 20000)

for emp in [regular_emp, contract_emp, manager]:
    print(emp)


# vehicle Rental

class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, duration):
        return self.rental_rate * duration

    def __str__(self):
        return f"Vehicle Model: {self.model}, Rental Cost: {self.calculate_rental(1)} per day"


class Car(Vehicle):
    def __init__(self, model, rental_rate, fuel_type):
        super().__init__(model, rental_rate)
        self.fuel_type = fuel_type

    def calculate_rental(self, duration):
        return self.rental_rate * duration * 1.1  # Cars have a 10% surcharge


class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_included):
        super().__init__(model, rental_rate)
        self.helmet_included = helmet_included

    def calculate_rental(self, duration):
        return self.rental_rate * duration * 0.9  # Bikes get a 10% discount


class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity

    def calculate_rental(self, duration):
        return self.rental_rate * duration * 1.2  # Trucks have a 20% surcharge


car = Car("Sedan", 100, "Petrol")
bike = Bike("Sport Bike", 50, True)
truck = Truck("Heavy Truck", 200, 5000)

duration = 5  # Rental duration in days
for vehicle in [car, bike, truck]:
    print(f"{vehicle.model} Rental Cost for {duration} days: {vehicle.calculate_rental(duration)}")
