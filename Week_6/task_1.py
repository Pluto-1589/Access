

# The signatures of this class is required for the automated grading to work.
# You must not change its name.
# You must add the correct signatures for each missing method as outlined
# in the task instructions.
class BankAccount:

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        """Adds the given amount to the account balance. If the amount is less than or equal to zero, raise a ValueError with the message "Deposit amount must be positive"."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        else:
            self._balance += amount

        return self._balance

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        elif amount > self._balance:
            raise ValueError("Insufficient funds")
        else:
            self._balance -= amount

        return self._balance

    def __str__(self) -> str:
        return f"Account owner: {self._owner}\nAccount balance: CHF {self._balance}"

    def __repr__(self) -> str:
        return (f"BankAccount ({self._owner}, {self._balance})")

    # implement the necessary methods

# The following lines call the functionality
# This way you can check what it does.


her_account = BankAccount("Nes", 500)
her_account.deposit(250)
print(her_account.__repr__())

# my_account = BankAccount("Melon Tusk", 269800000000)
# my_account.withdraw(200000000000)
# print(my_account)
# print(repr(my_account))
