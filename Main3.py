#Inicio del Program
print("Aumento del Sueldo")

print("")
valorsueldo = float(input("Introduzca Sueldo Actual: "))
print(f"Sueldo Actual es de: {valorsueldo}Bs")

print("")
aumento = float(input("Introduzca Porcentaje del Aumento: "))
totalaumento = (valorsueldo*aumento)/100
print(f"Porcentaje del Aumento en Bolivares es de: {totalaumento}Bs")

print("")
sueldototal = valorsueldo + totalaumento
print(f"Total del Sueldo a pagar es de: {sueldototal}Bs")
#Fin del Programa