#Inicio del Programa
print("Convertidor de Peso")
print("")
peso = float(input("Introduzca el Peso del Paciente: "))

#Libras
print("")
libras = 0.453592
print(f"Equivalente en Libras en Kilos es de: {libras}")

#Peso de Kilos a Libras
print("")
TLi = peso*libras
print(f"Peso Total en Libras es de: {TLi} Li")

#Peso de Kilos a Gramos
print("")
TGr = peso*1000
print(f"Peso Total en Gramos es de: {TGr} Gr")

#Peso de Libras a Kilos
print("")
TKi = TLi/libras
print(f"Peso Total de Libras a Kilos es de: {TKi} Kg")

#Resultado
print(f"{peso} Kilos - {TGr} Gramos - {TLi} Libras ")
#Fin del Programa