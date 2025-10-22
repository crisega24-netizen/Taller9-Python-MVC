class Numero:
    def __init__(self):
        self.numero = " "
        
    def getNumero(self):
        return self.numero
    
    def setNumero(self, nuevoNumero):
        self.numero = nuevoNumero
        
    def validarPar(self):
        if self.numero % 2 == 0:
            mensaje = "El número es par"
        else:
            mensaje = "El número es impar"
        return mensaje