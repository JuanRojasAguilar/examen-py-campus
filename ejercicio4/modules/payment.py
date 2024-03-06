from modules.corefiles import json_update
import json

def get_employee(employee_data:dict):
    try:
        id = input("Ingrese el id del empleado a pagar: ")
        for key, value in employee_data.items():
            if key == id:
                return value
    except:
        input("Id ingresado no valido")

def add_payment(employee_data:dict, pay_data:dict):
    try:
        month = input("Sobre qué mes se está generando el pago? ")
        date = input("Cual es la fecha en la que se genera el pago (dd/mm/yyyy)? ")
        employee = get_employee(employee_data)
        worked_days = int(input("Ingrese los días trabajados: "))
        extra_hours = int(input("Ingrese las horas extras realizadas: "))
        day_worth = employee["Pago Mensual"]/26
        cafeteria_disc = float(input("Hubo descuento por cafetería? "))
        if not isinstance(cafeteria_disc, float):
            cafeteria_disc = 0
        loan_cuote = float(input("Ingrese la cuota por prestamo: "))
        if not isinstance(loan_cuote, float):
            loan_cuote = 0
        total = ((day_worth * worked_days) + (extra_hours * 5500)) - cafeteria_disc - loan_cuote
        dicc = {
            "Month": month,
            "Fecha de generado": date
            "Sueldo base": employee["Pago Mensual"],
            "Valor Total horas extra": extra_hours * 5500,
            "Cuota Prestamo": loan_cuote,
            "Descuento cafeteria": cafeteria_disc,
            "Total a pagar": f"{total:.2f}"
        }
        ticket = dict({month:dicc})

        if str(employee["Id"]) in pay_data.keys():
            pay_data[str(employee["Id"])].append(ticket)
        else:
            pay_data.update({employee["Id"]: [ticket]})
        json_update(pay_data, "payments.json")
        input(f"Pago de {total:.2f} realizado por exito")
    except ValueError:
        input("Ha ingresado datos incorrectos, por su seguridad será enviado al menu principal")

def payment_report(payments):
    try:
        total = 0
        id = input("Ingrese el id del empleado a revisar: ")
        for key, value in payments.items():
            if key == id:
                for _, value2 in enumerate(value):
                    input(json.dumps(value2, indent=2))
                    for value3 in value2.values():
                        total += float(value3["Total a pagar"])
                input(f"El total pagado es: {total:.2f}")
    except:
        input("roto")