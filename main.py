# =========================
# PANEL FINANCIERO
# =========================

def guardar_ingreso(monto):
    archivo = open("ingresos.txt", "a")
    archivo.write(str(monto) + "\n")
    archivo.close()


def guardar_gasto(monto):
    archivo = open("gastos.txt", "a")
    archivo.write(str(monto) + "\n")
    archivo.close()


def ver_ingresos():
    try:
        archivo = open("ingresos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        ingresos = []
        for linea in lineas:
            ingresos.append(float(linea.strip()))

        return ingresos

    except FileNotFoundError:
        return []


def ver_gastos():
    try:
        archivo = open("gastos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        gastos = []
        for linea in lineas:
            gastos.append(float(linea.strip()))

        return gastos

    except FileNotFoundError:
        return []


# =========================
# PROGRAMA PRINCIPAL
# =========================

opcion = ""

while opcion != "4":

    print("\n" + "-" * 30)
    print("=== PANEL FINANCIERO ===")
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Ver balance")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        try:
            monto = float(input("Monto ingreso: "))
            guardar_ingreso(monto)
            print("Ingreso registrado")
        except ValueError:
            print("Error: debes ingresar un número válido")

    elif opcion == "2":
        try:
            monto = float(input("Monto gasto: "))
            guardar_gasto(monto)
            print("Gasto registrado")
        except ValueError:
            print("Error: debes ingresar un número válido")

    elif opcion == "3":
        ingresos = ver_ingresos()
        gastos = ver_gastos()

        total_ingresos = sum(ingresos)
        total_gastos = sum(gastos)

        balance = round(total_ingresos - total_gastos, 2)

        print("\n--- RESUMEN ---")
        print("Total ingresos:", total_ingresos)
        print("Total gastos:", total_gastos)
        print("Balance:", balance)

    elif opcion == "4":
        print("Saliendo...")

    else:
        print("Opción no válida")