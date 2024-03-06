#constantes de cambio NO TOCAR
USD = 3944
YEN = 26.30
EUR = 4279


def cop_usd():
    try:
        user_pesos = float(input("Cuántos Pesos quiere cambiar? "))
        if user_pesos < 0:
            input("No se puede hacer un cambio con el valor ingresado")
            cop_usd()
        exchange = user_pesos/USD
        print(f"Su cambio será de {exchange:.2f} USD")
        input("Presione ENTER para volver...")
    except ValueError:
        input("Lo siento, eso no es una moneda de curso legal")

def cop_eur():
    try:
        user_pesos = float(input("Cuántos Pesos quiere cambiar? "))
        if user_pesos < 0:
            input("No se puede hacer un cambio con el valor ingresado")
            cop_usd()
        exchange = user_pesos/EUR
        print(f"Su cambio será de {exchange:.2f} EUR")
        input("Presione ENTER para volver...")
    except ValueError:
        input("Lo siento, eso no es una moneda de curso legal")
        
def eur_cop():
    try:
        user_pesos = float(input("Cuántos Euros quiere cambiar? "))
        if user_pesos < 0:
            input("No se puede hacer un cambio con el valor ingresado")
            cop_usd()
        exchange = user_pesos * EUR
        print(f"Su cambio será de {exchange:.2f} COP")
        input("Presione ENTER para volver...")
    except ValueError:
        input("Lo siento, eso no es una moneda de curso legal")

def cop_yen():
    try:
        user_pesos = float(input("Cuántos Pesos quiere cambiar? "))
        if user_pesos < 0:
            input("No se puede hacer un cambio con el valor ingresado")
            cop_usd()
        exchange = user_pesos/YEN
        print(f"Su cambio será de {exchange:.2f} YEN")
        input("Presione ENTER para volver...")
    except ValueError:
        input("Lo siento, eso no es una moneda de curso legal")