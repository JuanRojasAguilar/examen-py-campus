from tabulate import tabulate

def get_info():
    try:
        id = input("Ingrese el id del usuario: ")
        names = input("Por favor ingrese los nombres del usuario: ").title()
        last_names = input("Por favor ingrese los apellidos del usuario: ").title()
        name = names.split(" ")
        apellido = last_names.split(" ")
        place = input(f"Por favor ingrese la dirección de domicilio de {name[0]}: ")
        city = input(f"Por favor ingrese la ciudad de {name[0]}: ").capitalize()
        #Llamar una variable long no es lo más sabio de este mundo
        long = input(f"Por favor ingrese la longitud de {name[0]}: ")
        lat = input(f"Por favor ingrese la longitud de {name[0]}: ")
        email = input(f"Por favor ingresa el email de {name[0]}: ")
        age = int(input(f"Por favor ingresa la edad de {name[0]}: "))
        job = input(f"Por favor ingresa la ocupacion de {name[0]}: ")

        user_dicc = {
            "Id": id,
            "Nombres": names,
            "Apellidos": last_names,
            "Ubicacion": {
                "Direccion": place,
                "Ciudad": city,
                "Longitud": long,
                "Latitud": lat
            },
            "Email": email,
            "Edad": age,
            "Ocupacion": job
        }
        print(tabulate([user_dicc], headers="keys", tablefmt="fancy_grid"))

    except:
        sys.exit("Has ingresado un dato no válido")