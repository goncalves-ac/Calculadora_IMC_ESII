from calcIMC import *

print("\t\tBody Mass Index / Índice de Massa Corporal\n")
print("************************************************************************************")
print("\tHeight and weight must be separated by a dot (.) and not a comma (,).")
print("************************************************************************************\n")

# Dados 
print("\tData for the calculation:\n")
name = input("Name (Nome): ")
biologicalSex = input("Biological Sex - (F or M): ")
age = int(input("Age: "))
height = float(input("Height (m): "))
weight = float(input("Weight (Kg): "))

print("\n************************************************************************************\n")

result_imc = CalcIMC(name, age, height, weight, biologicalSex)

print(f"Resultado :\n\t{result_imc.get_resultIMC()}\n\n")
