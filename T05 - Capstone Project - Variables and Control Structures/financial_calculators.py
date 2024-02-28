<<<<<<< HEAD
import math
import sys



"""
The investor should choose which calculation they
wish to carry out - either:
the interest they earn on an invstment or
the monthly repayments on a loan.
"""

print("investment\t- to calculate the amount of interest you'll earn on your invstment")
print("bond\t\t- to calculate the amount you'll have to pay on a home loan")
print("")
invest = False
bond = False
while True:
    invest_or_bond = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
    invest_or_bond = invest_or_bond.lower()
    if invest_or_bond == "investment" or invest_or_bond == "'investment'": # correct input
        invest = True
        break
    elif invest_or_bond == "bond" or invest_or_bond == "'bond'": # correct input
        bond = True
        break
    elif invest_or_bond == "exit":
        sys.exit()
    else:
        print("input investment or bond - type exit to terminate the program.")

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
    
    interest = "compound"
    print("\nYou can have simple or compound interest.")
    print("I remind you that Einstein called Compound Interest 'the eighth wonder of the world.' (reputedly)")
    answer = input("\nDo you want compound interest? Default is yes: ")
    answer = answer.lower()
    if answer == "no" or answer == "n":
        interest = "simple"
    
    if interest == "simple":
        print(f"\nYou've chosen simple interest. You know that Einstein wasn't stupid, don't you.")
        final_capital = amount_to_invest *(1 + actual_rate*years_to_hold)
        print(f"Your total capital, starting with {amount_to_invest:,.2f} after {years_to_hold} years at {interest_rate:.2f}% interest will be:")
        print(f"${final_capital:,.2f}")
    elif interest == "compound":
        print("You will get compound interest. Good, Einstein knew what he was doing.")
        print("Remember that the interest is added once a year.")
        print("You should try and persuade them to add the interest at the end of each day.")
        print(f"You would be a lot richer after {years_to_hold} years!")
        final_capital = amount_to_invest * math.pow((1 + actual_rate), years_to_hold)
        print(f"Your total capital, starting with ${amount_to_invest:,.2f} after {years_to_hold} years at {interest_rate:.2f}% interest will be:")
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
    
    time_exponent = months_to_repay * -1  # make sure the exponent is -ve
    print(f"\nYou want to repay the loan of ${amount_of_loan:,.2f} in {months_to_repay} months.")
    
    repayment = (interest_per_month * amount_of_loan)/(1 - (1 + interest_per_month)**(time_exponent))
    print(f"\nYour payment each month will be ${repayment:,.2f} in order to repay the loan of ${amount_of_loan:,.2f}")
    print(f"over {months_to_repay} months at an interest rate of {interest_rate:,.2f}%")
    total_amount = repayment * months_to_repay
    print(f"You will pay a total of ${total_amount:,.2f}")
    
=======
import math
import sys

"""
The investor should choose which calculation they
wish to carry out - either:
the interest they earn on an invstment or
the monthly repayments on a loan.
"""

print("investment\t- to calculate the amount of interest you'll earn on your invstment")
print("bond\t\t- to calculate the amount you'll have to pay on a home loan")
print("")
invest = False
bond = False
while True:
    invest_or_bond = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
    invest_or_bond = invest_or_bond.lower()
    if invest_or_bond == "investment" or invest_or_bond == "'investment'": # correct input
        invest = True
        break
    elif invest_or_bond == "bond" or invest_or_bond == "'bond'": # correct input
        bond = True
        break
    elif invest_or_bond == "exit":
        sys.exit()
    else:
        print("input investment or bond - type exit to terminate the program.")

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
    
    interest = "compound"
    print("\nYou can have simple or compound interest.")
    print("I remind you that Einstein called Compound Interest 'the eighth wonder of the world.' (reputedly)")
    answer = input("\nDo you want compound interest? Default is yes: ")
    answer = answer.lower()
    if answer == "no" or answer == "n":
        interest = "simple"
    
    if interest == "simple":
        print(f"\nYou've chosen simple interest. You know that Einstein wasn't stupid, don't you.")
        final_capital = amount_to_invest *(1 + actual_rate*years_to_hold)
        print(f"Your total capital, starting with {amount_to_invest:,.2f} after {years_to_hold} years at {interest_rate:.2f}% interest will be:")
        print(f"${final_capital:,.2f}")
    elif interest == "compound":
        print("You will get compound interest. Good, Einstein knew what he was doing.")
        print("Remember that the interest is added once a year.")
        print("You should try and persuade them to add the interest at the end of each day.")
        print(f"You would be a lot richer after {years_to_hold} years!")
        final_capital = amount_to_invest * math.pow((1 + actual_rate), years_to_hold)
        print(f"Your total capital, starting with ${amount_to_invest:,.2f} after {years_to_hold} years at {interest_rate:.2f}% interest will be:")
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
    
    time_exponent = months_to_repay * -1  # make sure the exponent is -ve
    print(f"\nYou want to repay the loan of ${amount_of_loan:,.2f} in {months_to_repay} months.")
    
    repayment = (interest_per_month * amount_of_loan)/(1 - (1 + interest_per_month)**(time_exponent))
    print(f"\nYour payment each month will be ${repayment:,.2f} in order to repay the loan of ${amount_of_loan:,.2f}")
    print(f"over {months_to_repay} months at an interest rate of {interest_rate:,.2f}%")
    total_amount = repayment * months_to_repay
    print(f"You will pay a total of ${total_amount:,.2f}")
    
>>>>>>> e00b911e54bdd3797756bc6ef730baf0f687a528
