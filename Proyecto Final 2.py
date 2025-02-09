while True :
    palabra = input("Ingresa una constraseña: ")
    longitud_palabra = len(palabra)
    if longitud_palabra  < 4 :
        print (f"La palabra ingresada solo tiene {longitud_palabra} palabras, faltan {8 - longitud_palabra} \
letras mas, vuelve a intertarlo. ")

    elif longitud_palabra > 8: 
        print (f"La palabra ingresada es muy larga, tiene {longitud_palabra} letras, lo correcto es solo 8 letras \
, vuelve a intentarlo.")
    
    else:
        print ("Contraseña ingresada correctamente.")
        break
    
    
