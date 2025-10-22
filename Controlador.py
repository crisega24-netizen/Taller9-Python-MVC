class Controlador:
    def __init__(self, objVista, objModelo):
        #Composición es el constructor
        self.objFormulario = objVista
        self.objNumero = objModelo
        
    def hacerPregunta(self):
        numero = self.objFormulario.hacerCampo()
        self.objNumero.setNumero(numero)
        datoMensaje = self.objNumero.validarPar()
        self.objFormulario.imprimirResultado(datoMensaje)