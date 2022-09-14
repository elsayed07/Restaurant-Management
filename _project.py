import sys
import csv
from tabulate import tabulate


def main():

    ...


def make_order():
    orders = {"item":"item", "number":"number"}
    while True:
        item = input("Order: ")
        if item == "":
            break
        else:
            if item in orders["item"]:
                orders["number"] += 1
            else:
                



def service(table, check):
    if table == "Small":
        tax = check/20
    elif table == "regular":
        tax = check/25
    elif table == "large":
        tax = check/40
    return tax


def taxes(check):
    return check/10


def assign_table():
    print("Welcome to La Dolce Vita resturant")
    persons_n = int(input("to assign the right table, how many persons are there: "))
    if persons_n >= 7:
        table = "large"
    elif persons_n <= 2:
        table = "small"
    else:
        table = "regular"
    return table


def check_cm_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()