
import numpy as np
import math

def calc_annuity():
    print("\n-- Annuity Calculator --")
    growth_type = input("Choose growth type - 'monthly' or 'continuous': ").lower()
    try:
        p = float(input("Enter starting principal: "))
        r = float(input("Enter annual interest rate (e.g., 0.06): "))
        t = float(input("Enter time in years: "))
        monthly = float(input("Enter monthly contribution: "))

        if growth_type == 'monthly':
            annuity = p
            for a in range(int(12*t)):
                annuity = (annuity + monthly) * (1 + r/12)
        elif growth_type == 'continuous':
            annuity = (p + monthly * 12 * t) * np.exp(r * t)
        else:
            print("Invalid growth type selected.")
            return

        print("\nFuture Value =", round(annuity, 2))
        print("Annual Interest Income =", round(annuity * r, 2))
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def calc_mortgage():
    print("\n-- Mortgage Payment Calculator --")
    try:
        p = float(input("Enter loan amount (principal): "))
        r = float(input("Enter annual interest rate (e.g., 0.05): "))
        t = float(input("Enter term in years: "))

        monthly_rate = r / 12
        n = 12 * t
        numerator = monthly_rate * (1 + monthly_rate) ** n
        denominator = (1 + monthly_rate) ** n - 1
        payment = round(p * numerator / denominator, 2)

        total_paid = round(payment * n, 2)
        interest_paid = round(total_paid - p, 2)

        print(f"\nMonthly Payment: ${payment}")
        print(f"Total Paid Over {int(t)} Years: ${total_paid}")
        print(f"Total Interest Paid: ${interest_paid}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def doubling_time():
    print("\n-- Doubling Time Calculator --")
    try:
        r = float(input("Enter annual interest rate (as decimal, e.g. 0.07): "))
        t = np.log(2) / r
        print(f"Money will double in approximately {round(t, 2)} years.")
    except ValueError:
        print("Invalid input.")

def solve_log():
    print("\n-- Logarithmic Equation Solver --")
    try:
        a = float(input("Enter base a (for log_a(x) = y): "))
        x = float(input("Enter x (value you're taking log of): "))
        y = math.log(x, a)
        print(f"log base {a} of {x} is {round(y, 4)}")
    except ValueError:
        print("Invalid input or math domain error.")

def convert_sci():
    print("=== Scientific Notation Converter ===")
    choice = input("Choose: 1) To Scientific  2) From Scientific  >>> ")

    if choice == "1":
        try:
            num = float(input("Enter a number: "))
            sci = "{:.2e}".format(num)
            print("Scientific Notation:", sci)
        except ValueError:
            print("Invalid number input.")

    elif choice == "2":
        try:
            sci_input = input("Enter scientific notation (e.g. 5.23e+06): ").strip()
            num = float(sci_input)
            print("Decimal Form:", num)
        except ValueError:
            print("Invalid scientific notation format. Try something like 5.2e+06.")
    else:
        print("Invalid choice.")

def main_menu():
    while True:
        print("\n==== Financial App Menu ====")
        print("1. Calculate Annuity (Monthly/Continuous)")
        print("2. Calculate Monthly Mortgage Payment")
        print("3. Estimate Time to Double Investment")
        print("4. Solve Logarithmic Equation")
        print("5. Convert to/From Scientific Notation")
        print("6. Quit")

        choice = input("Choose an option (1-6): ")
        if choice == '1':
            calc_annuity()
        elif choice == '2':
            calc_mortgage()
        elif choice == '3':
            doubling_time()
        elif choice == '4':
            solve_log()
        elif choice == '5':
            convert_sci()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


main_menu()
