class ContabilidadNegocio:
    def __init__(self):
        self.ingresos = 0
        self.gastos = 0

    def registrar_ingreso(self, monto):
        self.ingresos += monto
        print(f"Ingreso registrado: +${monto}")

    def registrar_gasto(self, monto):
        self.gastos += monto
        print(f"Gasto registrado: -${monto}")

    def calcular_balance(self):
        return self.ingresos - self.gastos

    def mostrar_resumen(self):
        print("\nResumen de contabilidad:")
        print(f"Ingresos totales: +${self.ingresos}")
        print(f"Gastos totales: -${self.gastos}")
        print(f"Balance actual: ${self.calcular_balance()}\n")


# Ejemplo de uso
if __name__ == "__main__":
    negocio = ContabilidadNegocio()

    while True:
        print("1. Registrar Ingreso")
        print("2. Registrar Gasto")
        print("3. Mostrar Resumen")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto del ingreso: "))
            negocio.registrar_ingreso(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto del gasto: "))
            negocio.registrar_gasto(monto)
        elif opcion == "3":
            negocio.mostrar_resumen()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")