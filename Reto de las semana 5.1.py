
while True :
    entrada_1 = input("Introduce el primer año: ").strip()
    if entrada_1 == "":
       print("No se ha ingresado ningun dato, intenta otra vez")
       continue
    try:
        año_1 = int(entrada_1)
        print (f"El año ingresado es: {año_1} ")
        break
    except ValueError:
        print ("No se ingreso el año en numero intenta otra vez.")


while True :
    entrada_2 = input("Introduce el segundo año: ").strip()
    if entrada_2 == "":
       print("No se ha ingresado ningun dato, intenta otra vez")
    elif entrada_1 == entrada_2:
        print ("Se ingreso el mismo año dos veces, elige otro año.")
        continue
    try:
        año_2 = int(entrada_2)
        print (f"El año ingresado es: {año_2} ")
        break
    except ValueError:
        print ("No se ingreso el año en numero intenta otra vez.")


 
if año_2 ==año_1+1 :
    print (f" Del año {año_1}  al {año_2} falta un solo un año.")
elif año_2 == año_1 -1 :
    print(f"Del año {año_1} al {año_2} ha pasado solo un año.")
elif año_1 > año_2 :
    print(f"Han pasado {año_1 - año_2} años del {año_1} al año {año_2}.")
elif año_1 < año_2 :
    print (f"Faltan {año_2 - año_1} años para año {año_1} del año {año_2}.")  

     













#Otra manera que econtre de hacer el projecto 


#  while True:
#     try:
#         entrada_1 = int(input("Introduce el año actual en numero: "))
#         if entrada_1 > 0:
#             print("You entered:", entrada_1)
#             break  # Exit the loop if input is a valid integer
#     except ValueError:
#         print("Invalid input. Por favor ingresa un numero valido.")




#years_diff = año_1 - año_2
# absolute_years_diff = abs(years_diff)
# print(f"La diferencia de años entre {año_1} y {año_2} son: {absolute_years_diff} año(s)")

# if years_diff <= 0:
#     print(f"Han pasado {absolute_years_diff} año(s) desde {año_1}")

# print(f"Faltan {absolute_years_diff} año(s) para el año {año_1}")   









   