#Proyectyo de Indice de Masa Corporal

#Recolectando Datos
while True:
    nombre = input("Ingresa tu nombre: ").strip()
    if nombre =="" :
        print("¡No se ingreso ningun dato!")
    else :
         print(f"Tu nombre es : {nombre}")
         break
while True:
    edad = input("Ingresa tu edad: ").strip()
    if edad =="" :
        print("¡No se ingreso ningun dato!")
    else :
        print(f"Tu edad es : {edad}")
        break
while True:
    altura = (input("Ingresa tu altura en metros: ")).strip()
    if altura =="" :
        print("¡No se ingreso ningun dato!")
        continue
    try:
        a= float(altura)
        print(f"Tu altura es : {altura}")
        break
    except ValueError:
        print("¡No se ingreso un numero!")
while True:
    peso = (input("Ingresa tu peso en kilos: ")).strip()
    if peso =="" :
        print("¡No se ingreso ningun dato!")
        continue
    try:
        p= int(peso)
        print(f"Tu peso es : {peso}")
        break
    except ValueError:
        print("¡No se ingreso un numero!")



#Concatenando para dar el IMS 

IMS = (p) / float (a**2)

print(f"Tu indice de masa muscular es: {IMS}")