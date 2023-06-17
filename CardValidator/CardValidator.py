#Algoritmo de lhun
class Tarjeta:
    def __init__(self, numero):
        self.numero = numero

<<<<<<< HEAD
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

    



    


=======
    def ValidarTarjeta(self):
        tarjetaInvertida = self.numero[::-1]  # Se invierte el número de la tarjeta
>>>>>>> 4c9490a3847f87e8b537b3797179311c29be2963

        valorAValidar = 0
        for i in range(len(tarjetaInvertida)):
            digito = int(tarjetaInvertida[i])
            if i % 2 == 1:  # Multiplicar por 2 los dígitos en posición impar
                numeroMultiplicado = digito * 2
                if numeroMultiplicado > 9:
                    numeroMultiplicado = numeroMultiplicado - 9  # Restar 9 si el resultado es mayor a 9
                valorAValidar += numeroMultiplicado
            else:
                valorAValidar += digito

        if valorAValidar % 10 == 0:
            return "Tarjeta valida."
        else:
            return "Tarjeta no valida."

# Ejemplo de uso
tarjeta = Tarjeta("4111889809629279") #Ingresar nro de tarjeta
resultado = tarjeta.ValidarTarjeta()
print(resultado)
