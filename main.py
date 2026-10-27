"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    per_semester = annual_cost / SEMESTERS_PER_YEAR
    return per_semester


def cost_per_month(annual_cost):
    per_month = annual_cost / MONTHS_PER_YEAR
    return per_month


def cost_per_day(annual_cost):
    per_day = annual_cost / SEMESTERS_PER_YEAR / CLASS_DAYS_PER_SEMESTER
    return per_day


def cost_per_credit(annual_cost, credits):
    per_credit = cost_per_semester(annual_cost) / int(credits) 
    return per_credit


def cost_per_class(annual_cost, credits):
    per_class = cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return per_class


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    cost_per_year = input("What is the cost per on year: ")
    cost_per_year = float(cost_per_year)
    # Then ask for the credits this semester.
    credits_per_semester = input("How many credits this semester: ")
    credits_per_semester = float(credits_per_semester)
    
    
    while True:
        # Show your menu here.
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("Q. Quit")

        choice = input("Choose an option: ")
       

        if choice == "Q":
            break
        elif choice == "1":
            print(f"Cost per semester: {cost_per_semester(cost_per_year):.2f}")
        elif choice == "2":
                    print(f"Cost per month: {cost_per_month(cost_per_year):.2f}")
        elif choice == "3":
                    print(f"Cost per day: {cost_per_day(cost_per_year):.2f}")
        elif choice == "4":
                    print(f"Cost per credit: {cost_per_credit(cost_per_year, credits_per_semester):.2f}")
        elif choice == "5":
                    print(f"Cost per class: {cost_per_class(cost_per_year, credits_per_semester):.2f}")
        else:
              print("Error")  

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
