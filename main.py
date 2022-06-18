from calcIMC import *

print("\t\tBody Mass Index / Índice de Massa Corporal\n")
print("************************************************************************************")
print("\n\tHeight and weight must be separated by a dot (.) and not a comma (,).")
print("\tAltura e peso devem ser separados por ponto (.) e não por vírgula (,).\n")
print("************************************************************************************\n")

# Dados 
print("\tData for the calculation:\n")
name = input("Name (Nome): ")
biologicalSex_str = input("Biological Sex - (F or M): ")
biologicalSex = biologicalSex_str.upper();
age = int(input("Age: "))
height_str = input("Height (m): ")
height_q = height_str.count(".") == 1 and height_str or height_str.replace(",",".")
height = float(height_q)
weight_str = input("Weight (Kg): ")
weight_q = weight_str.count(".") == 1 and weight_str or weight_str.replace(",",".")
weight = float(weight_q)

print("\n************************************************************************************\n")

result_imc = CalcIMC(name, age, height, weight, biologicalSex)

print(f"Resultado :\n\t{result_imc.get_resultIMC()}\n\n")
