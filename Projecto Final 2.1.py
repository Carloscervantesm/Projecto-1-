while True:
    cordenada_1 = int(input ("Ingrese el valor de x:"))
    cordenada_2 = int (input ("Ingrese el valor de y:"))
    
    if cordenada_1 and cordenada_2 == 0 :
        print ("El valor de las dos coordenadas no puede ser igual a 0")
        break
    elif cordenada_1 > 0  and cordenada_2  > 0 :
        print ("Las coordenadas se encuentran en el sector 1")
        break
    elif cordenada_1 < 0  and cordenada_2  > 0 :
        print ("Las coordenadas se encuentran en el sector 2")
        break
    elif cordenada_1 < 0 and cordenada_2 < 0 :
        print ("Las coordenadas se encuentran en el sector 3")
        break
    elif cordenada_1 > 0 and cordenada_2 < 0 :
        print ("Las coordenadas se encuentran en el sector 4")
        exit