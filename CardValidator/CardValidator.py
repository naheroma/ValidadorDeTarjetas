#Algoritmo de lhun

import math
tarjeta = "55473"
par = ""
InvertidoMultiplicado = ""
valorAValidar = 0


tarjetaInvertida = ""
longitud = len(tarjeta)
if longitud < 13:
    print("No valida")
else:
    #Se invierte el string tarjeta
    for x in tarjeta:
        tarjetaInvertida = x + tarjetaInvertida

    #Multiplicar x2 salteando una vez por iteracion un elemento del string
    for i in range(0, len(tarjetaInvertida),2):
        par = tarjetaInvertida[i:i+2]
        try:
            numeroMultiplicado = int(par[1]) * 2
        except IndexError:
            numeroMultiplicado = 0
        
        #str numeroMultiplicado convierte en una cadena de texto
        #int digito convierte cada valor de esta cadena en un entero
        if numeroMultiplicado > 9:     
            numeroMultiplicado = sum(int(digito) for digito in str(numeroMultiplicado))    
            InvertidoMultiplicado += str(par[0]) + str(numeroMultiplicado)

    #Sumar todos los digitos
    for x in InvertidoMultiplicado:
        valorAValidar += int(x)
    #Si el resto del valor obtenido es 0, la tarjeta es valida.
    if valorAValidar % 10 == 0:
        print("Valida.")
    else:
        print("No valida.")

    



    





