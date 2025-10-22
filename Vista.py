class VistaFormulario:
    def __init__(self):
        self.nombreModulo = "Modulo validar numeros"
        self.textoPregunta = "Dígite el número"
        self.campoNumero = ""
        
    def hacerCampo(self):
        print(self.nombreModulo)
        print(self.textoPregunta)
        self.campoNumero = int(input())
        return self.campoNumero
    
    def imprimirResultado(self, datoMensaje):
        print(datoMensaje)