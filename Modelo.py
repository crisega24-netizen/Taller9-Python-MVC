class Numero:
    def __init__(self):
        self.numero = " "
        
    def getNumero(self):
        return self.numero
    
    def setNumero(self, nuevoNumero):
        self.numero = nuevoNumero
        
    def validarPar(self):
        if self.numero % 2 == 0:
            paridad = "par"
        else:
            paridad = "impar"
        
        
        if self.numero > 0:
            signo = "positivo"
        elif self.numero < 0:
            signo = "negativo"
        else:
            signo = "neutro"
        
        mensaje = f"El número {self.numero} es {paridad} y {signo}."
        return mensaje
