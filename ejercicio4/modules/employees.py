def handle_position():
    clear_screen()
    cargo = ""
    clear_screen()
    cargos = [["1.","Almacenista"],["2.","JefeIt"],["3.","Administrador"],["4.","Mensajero"],["5","Gerente"]]
    print(tabulate(cargos, tablefmt="fancy_grid"))
    position = input("Por favor seleccione el cargo de manera muy cuidadosa: ")
    if position == "1":
        cargo = "Almacenista"
    elif position == "2":
        cargo = "Jefe It"
    elif position == "3":
        cargo = "Administrador"
    elif position == "4":
        cargo = "Mensajero"
    elif position == "5":
        cargo = "Gerente"
    else:
        handle_position()
    return cargo

def add_employee(data:dict):
    try:
        print(data)
        id = int(input("Ingresa el numero de id del trabajador: "))
        if str(id) in data.keys():
            input("Ese id ya está registrado")
            main_menu()
        name = input("Por favor ingrese el nombre completo del trabajador: ").title()
        first_name = name.split(" ")[0]
        cargo = handle_position()
        monthly_pay = float(input(f"Cuánto es el pago mensual de {first_name}: "))
        dicc = {
            "Id": id,
            "Nombre": name,
            "Posicion": cargo,
            "Pago Mensual": monthly_pay
        }
        data.update({id: dicc})
        json_update(data, "employees.json")
    except ValueError:
        input("Jholversoft no usa esos valores")