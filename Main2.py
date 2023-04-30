#Inicio del Programa
print("Porcentaje de cada Inversion")
print("")
in1 = float(input("Introduzca Inversion 1: "))
print(f"Total de la Primera Inversion es de: {in1}$")
in2 = float(input("Introduzca Inversion 2: "))
print(f"Total de la Primera Inversion es de: {in2}$")
in3 = float(input("Introduzca Inversion 3: "))
print(f"Total de la Primera Inversion es de: {in3}$")

print("")
IT = (in1+in2+in3)
print(f"La Inversion Total es de: {IT}")

print("")
print("Porcentaje de Cada Inversion")
pin1 = (in1*100)/IT
print(f"Porcentaje de la Primera Inversion es de: {pin1}%")
pin2 = (in2*100)/IT
print(f"Porcentaje de la Segunda Inversion es de: {pin2}%")
pin3 = (in3*100)/IT
print(f"Porcentaje de la Tercera Inversion es de: {pin3}%")
#Fin del Programa