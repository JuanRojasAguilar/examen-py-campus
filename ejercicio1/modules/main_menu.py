from tabulate import tabulate
import sys
import os

from modules.money_converter import cop_usd, cop_eur, eur_cop, cop_yen

def clear_screen():
    if sys.platform == "linux":
        os.system("clear")
    else:
        os.system("cls")

def main_menu():
    clear_screen()
    def wrapper(func):
        func()
        main_menu()

    title = """
    +++++++++++++++++++++++++++++++++
    +  CASA DE CAMBIOS JHOLV-EUROS  +
    +++++++++++++++++++++++++++++++++
    """
    print(title)
    menu = [["1.", "COP to USD"],["2.", "COP to EUR"], ["3.", "EUR to COP"], ["4.", "COP to YEN"], ["5.", "Salir"]]
    print(tabulate(menu, tablefmt="fancy_grid"))
    option = input("\n>> ")
    if option == "1":
        wrapper(cop_usd)
    elif option == "2":
        wrapper(cop_eur)
    elif option == "3":
        wrapper(eur_cop)
    elif option == "4":
        wrapper(cop_yen)
    elif option == "5":
        sys.exit("Borrando system 32...")
    else:
        main_menu()