import sys
import csv
from tabulate import tabulate


def main():
    check_cm_arg()
    table = assign_table()
    orders = make_order()
    with open("order.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["item","price"])
        writer.writerow({"item":"Item", "price":"Price"})
        for order in orders:
            writer.writerow({"item":order, "price":item_price(order)})


    print("Order Summary")
    print(plot())
    check = calculate_check()
    check = ([eval(i) for i in check[1:]])
    check = sum(check)
    print(f"_____________________________________ Payment: ${check}")
    total = check + taxes(check) + service(table, check)
    print(f"Total Payment After Adding Service And Taxesx: ${total}")

def plot():
    _order = []
    with open("order.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            _order.append(row)
    return(tabulate(_order, headers="keys", tablefmt="grid"))


def service(table, check):
    service = 0
    if table == "small":
        service += 0
    elif table == "regular":
        service += check/20
    elif table == "large":
        service += check/10
        print(service)
    return round(service)


def taxes(check):
    return check/10


def assign_table():
    print('Welcome to La Dolce Vita restaurant ❤️❤️❤️❤️❤️❤️❤️')
    persons_n = int(input("to assign the right table, how many persons are there: "))
    if persons_n >= 7:
        table = "large"
    elif persons_n <= 2:
        table = "small"
    else:
        table = "regular"
    return table


def make_order():
    orders = []
    while True:
        order = input("order: ")
        if not order:
            break
        orders.append(order)
    return orders


def item_price(x):
    with open(sys.argv[1]) as file:
        for row in file:
            splited_name = row.strip().split(",")
            item = splited_name[0]
            price =splited_name[1]
            if x == item:
                return price


def calculate_check():
    total = []
    with open("order.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total.append(row[1])
    return total


def check_cm_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()