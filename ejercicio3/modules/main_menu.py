from modules.corefiles import check_file, get_info, json_update, clear_screen
import sys

def main_menu():
    check_file()
    data = get_info()
    title = """
    ++++++++++++++++++++++++++
    +  TIENDA JHOL-VERDURAS  +
    ++++++++++++++++++++++++++
    """
    print(title)
    info_prod(data)

def info_prod(data:dict):
    try:
        id = int(input("Ingrese el id del nuevo producto: "))
        while id < 0:
            print("El identificador no puede ser negativo")
            id = int(input("Ingrese el id del nuevo producto: "))
        name = input("Ingrese el nombre del producto: ").upper()
        first_name = name.split(" ")[0]
        unit_price = float(input(f"Ingrese el valor de {first_name}: "))
        min_stock = int(input("Cuánto es el stock mínimo? "))
        max_stock = int(input("Cuánto es el stock máximo? "))
        while max_stock < min_stock:
            print("El stock máximo no puede ser menor que el stock minimo")
            min_stock = int(input("Cuánto es el stock mínimo? "))
            max_stock = int(input("Cuánto es el stock máximo? "))
        dicc = {
            "ID": id,
            "Nombre": name,
            "ValorUnitario": unit_price,
            "StockMinimo": min_stock,
            "StockMaximo": max_stock
        }
        data.update({id:dicc})
        json_update(data)
        input(f"Se ha añadido {name} con Id {id}.")
        option = input("Desea agregar otro producto? S(si) Enter(no)").upper()
        if option == "S":
            info_prod()
        elif option == "":
            sys.exit("Hasta luego")
    except ValueError:
        input("La tierra Jhol-verduras no acepta ese tipo de valores")
        clear_screen()
        info_prod(data)