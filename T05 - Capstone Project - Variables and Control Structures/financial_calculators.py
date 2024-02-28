import math
import sys

"""
The investor should choose which calculation they
wish to carry out - either:
the interest they earn on an invstment or
the monthly repayments on a loan.
"""

class Investment:
    def __init__(self, principal, rate, years):
        self.principal = principal
        self.rate = rate
        self.years = years

    def simple_interest(self):
        return self.principal * (1 + self.rate * self.years)

    def compound_interest(self):
        return self.principal * (1 + self.rate) ** self.years

class LongTermLoan:
    def __init__(self, loan_amount, years, interest_rate):
        self.loan_amount = loan_amount
        self.years = years
        self.interest_rate = interest_rate

    def total_interest(self):
        return self.loan_amount * self.interest_rate * self.years

    def monthly_repayment(self):
        months = self.years * 12
        monthly_interest_rate = self.interest_rate / 12
        monthly_payment = (self.loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)
        return monthly_payment

    def total_paid_back(self):
        months = self.years * 12
        monthly_payment = self.monthly_repayment()
        total_paid = monthly_payment * months
        return total_paid, months

print("investment\t- to calculate the amount of interest you'll earn on your invstment")
print("bond\t\t- to calculate the amount you'll have to pay on a home loan")
print("")
invest = False
bond = False

while True:
    invest_or_bond = input("Enter either 'i' or 'b' from the menu above to proceed: ")
    invest_or_bond = invest_or_bond.lower()
    if invest_or_bond == "i" or invest_or_bond == "'i'": # correct input
        invest = True
        break
    elif invest_or_bond == "b" or invest_or_bond == "'b'": # correct input
        bond = True
        break
    elif invest_or_bond == "exit":
        sys.exit()
    else:
        print("input i or b - type exit to terminate the program.")

if invest == True:
    try:
        amount_to_invest = float(input("\nHow much would you like to invest in USD? "))
    except ValueError as err:
        print("input a real number, do not include the $ symbol.")
        print(f"Do not include commas in the amount. {err}")
        sys.exit()
              
    print(f"You want to invest ${amount_to_invest:,.2f}")
    
    try:
        interest_rate = float(input("\nGive the percentage interest rate you expect to get: "))
    except ValueError as e:
        print(f"input a real number (has a decimal point). Do not include the % symbol. {e}")
        sys.exit()
        
    print(f"You would like {interest_rate:.2f}% interest per year.")
    actual_rate = interest_rate * 0.01 # real interest, not the percentage
    
    try:
        years_to_hold = float(input("\nHow many years do you want to hold this investment? "))
    except ValueError as e:
        print(f"input a whole number of years. Don't input any characters. {e}")
        sys.exit()
        
    print("Will make sure it's a whole number of years")
    years_to_hold = int(round(years_to_hold)) # round to nearest integer whole years
    
    print(f"You want to invest ${amount_to_invest:,.2f} for {years_to_hold} years.")
    investment = Investment(amount_to_invest, actual_rate, years_to_hold)
    
    interest = "compound"
    print("\nYou can have simple or compound interest.")
    answer = input("\nDo you want compound interest? Default is yes: ")
    answer = answer.lower()
    if answer == "no" or answer == "n":
        interest = "simple"
    
    if interest == "simple":
        print(f"\nYou've chosen simple interest.")
        final_capital = investment.simple_interest()
        print(f"Your total capital, starting with ${amount_to_invest:,.2f} after {years_to_hold} years at {interest_rate:.2f}% simple interest will be:")
        print(f"${final_capital:,.2f}")
    elif interest == "compound":
        print("You will get compound interest.")
        print("Remember that the interest is added once a year.")
        print("You should try and persuade them to add the interest at the end of each day.")
        print(f"You would be a lot richer after {years_to_hold} years!")
        final_capital = investment.compound_interest()
        print(f"Your total capital, starting with ${amount_to_invest:,.2f} after {years_to_hold} years at {interest_rate:.2f}% compound interest will be:")
        print(f"${final_capital:,.2f}")

elif bond == True:

    try:
        amount_of_loan = float(input("\nWhat is the current value of your house in USD? "))
    except ValueError as err:
        print("input a real number, do not include the $ symbol.")
        print(f"Do not include commas in the amount. {err}")
        sys.exit()

    print("You want to borrow the full value of your house.")
    print("We normally don't give 100% mortgages but in your case we'll make an acception.")
    print(f"\nSo you wish to borrow ${amount_of_loan:,.2f} in order to buy your house.")
    
    try:
        interest_rate = float(input("\nGive the percentage interest rate you expect to pay on the loan: "))
    except ValueError as e:
        print(f"input a real number (has a decimal point). Do not include the % symbol. {e}")
        sys.exit()
        
    print(f"\nYou expect to pay {interest_rate:.2f}% interest on the loan.")
    actual_rate = interest_rate * 0.01 # real interest, not the percentage
    interest_per_month = actual_rate / 12 # interest per month
    
    try:
        months_to_repay = float(input("\nIn how many months do you want to fully repay this loan? "))
    except ValueError as e:
        print(f"input a whole number of months. Don't input any characters. {e}")
        sys.exit()
        
    print("\nWill make sure it's a whole number of months")
    months_to_repay= int(round(months_to_repay)) # round to nearest whole months
    
    print(f"\nYou want to repay the loan of ${amount_of_loan:,.2f} in {months_to_repay} months.")
    loan = LongTermLoan(amount_of_loan, months_to_repay/12, actual_rate)
    monthly_payment = loan.monthly_repayment()
    total_paid, months = loan.total_paid_back()

    print(f"\nYour payment each month will be ${monthly_payment:,.2f} in order to repay the loan of ${amount_of_loan:,.2f}")
    print(f"over {months_to_repay} months at an annual interest rate of {interest_rate:,.2f}%")
    print(f"You will pay a total of ${total_paid:,.2f}")
    