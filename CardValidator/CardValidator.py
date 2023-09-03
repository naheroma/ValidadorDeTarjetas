#Algoritmo de Lhun
class Tarjeta:
    def __init__(self, numero_de_tarjeta):
        self.numero_de_tarjeta = numero_de_tarjeta
        
    def validar_tarjeta(self):
        tarjeta_invertida = self.numero_de_tarjeta[::-1]#Invierte la cadena
        numero_a_validar = 0
        #Valida si la tarjeta tiene los digitos minimos o maximos
        if not (14 <= len(tarjeta_invertida) <= 19):
            return "Tarjeta no valida."
            
        for x in range(len(tarjeta_invertida)):
            numero = int(tarjeta_invertida[x])
            
            if x % 2 != 0:  # Analiza los numeros en posicion impar
                numero_multiplicado = numero * 2
                if numero_multiplicado > 9:
                    numero_multiplicado -= 9
                numero_a_validar += numero_multiplicado
            else:
                numero_a_validar += numero
                
        if numero_a_validar % 10 == 0:
            return "Tarjeta válida."
        else:
            return "Tarjeta no válida."

