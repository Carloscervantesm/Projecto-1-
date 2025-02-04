while True :
    contraseña = input("Ingrese una contraseña: ")
    if contraseña[0].isalpha():
       print ("La contraseña debe iniciar con un numero")
    else :
        print("contraseña valida")
        break

while True:
    contraseña_2 = input ("Escriba de nuevo la contraseña: ")
    if contraseña != contraseña_2 :
        print ("Las contraseñas no coinciden")
    else :
        print ("Las contraseñas coinciden. \nFin del Programa ")
        break