from modules.corefiles import check_file, clear_screen, get_info
from modules.employees import add_employee
from modules.payment import add_payment, payment_report
from tabulate import tabulate
import sys

def main_menu():
    clear_screen()
    check_file()
    employees = get_info("employees.json")
    payments = get_info("payments.json")
    title = """
    +++++++++++++++++
    +  JHOLVERSOFT  +
    +++++++++++++++++
    """
    print(title)
    menu = [["1.","Registrar empleado"],["2.","Registrar pago"],["3.", "Colilla de pago"],["4.", "Salir"]]
    print(tabulate(menu, tablefmt="fancy_grid"))
    option = input("\n>> ")
    if option == "1":
        add_employee(employees)
        main_menu()
    elif option == "2":
        add_payment(employees, payments)
        main_menu()
    elif option == "3":
        payment_report(payments)
        main_menu()
    elif option == "4":
        sys.exit("Tenga un buen día!")
    else:
        main_menu()
