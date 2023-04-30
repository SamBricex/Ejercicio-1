#Inicio del Programa
print("Asistencia de Alumnos")
print("")
C1R = float(input("Ingrese Cantidad de Alumnos en la Clase de Redes: "))
print("")
C2A = float(input("Ingrese Cantidad de Alumnos en la Clase de Arquitectura: "))
print ("")
C3P = float(input("Ingrese Cantidad de Alumnos en la Clase de Programacion: "))
print("")
TA = (C1R+C2A+C3P)
print(f"Total de Alumnos que asistieron al Colegio el dia de hoy: {TA} Alumnos")

#Porcentajes
print("")
PAC1 = (C1R*100)/TA
print(f"Porcentaje de Alumons en la Clase de Redes es de: {PAC1}%")
print("")
PAC2 = (C2A*100)/TA
print(f"Porcentaje de Alumons en la Clase de Redes es de: {PAC2}%")
print("")
PAC3 = (C3P*100)/TA
print(f"Porcentaje de Alumons en la Clase de Redes es de: {PAC3}%")
#Fin del Programa