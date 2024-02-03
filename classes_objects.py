# This program demonstrates classes and objects in Python.

# Define a simple class
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

# Create an instance of the Dog class
dog1 = Dog(name="Buddy", age=3)

# Access instance attributes
print(f"{dog1.name} is {dog1.age} years old.")

# Access class attribute
print(f"{dog1.name} belongs to the {Dog.species} species.")

# Call an instance method
dog1.bark()

# Inheritance
class GoldenRetriever(Dog):
    # Additional attribute specific to GoldenRetriever
    breed = "(Golden Retriever)"

    # Overriding the bark method
    def bark(self):
        print(f"{self.name} {self.breed} says Woof! Woof!")

# Create an instance of the GoldenRetriever class
golden_retriever1 = GoldenRetriever(name="Max", age=2)

# Access inherited attributes
print(f"{golden_retriever1.name} is a {golden_retriever1.age}-year-old {golden_retriever1.breed}.")

# Call the overridden method
golden_retriever1.bark()

# Encapsulation
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self._balance = balance  # Private attribute (convention with a single underscore)

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited ${amount}. New balance: ${self._balance}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self._balance

# Create an instance of the BankAccount class
account1 = BankAccount(account_holder="Alice", balance=1000)

# Access public and private attributes
print(f"Account holder: {account1.account_holder}")
print(f"Balance: ${account1.get_balance()}")

# Deposit and withdraw
account1.deposit(500)
account1.withdraw(200)

# Try to access the private attribute directly (not recommended)
# print(account1._balance)

# Polymorphism
def make_sound(animal):
    animal.make_sound()

class Cat:
    def make_sound(self):
        print("Meow!")

class Duck:
    def make_sound(self):
        print("Quack!")

# Create instances of different classes
cat = Cat()
duck = Duck()

# Call the function with different objects
make_sound(cat)
make_sound(duck)
