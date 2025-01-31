import numpy as np

class Contador:
    def __init__(self, bloco):
        self.bloco = bloco
        self.dados = []
        self.device = {}
        self.browser = {}
        self.response = {}
        self.status = {}
        self.avgsize = 0
        self.sumsize = 0
        self.latency = 0.0
        self.referer = {}


    def add( self, item ):
        self.dados.append( item )

    def __str__( self ):
        return self.bloco + ". " + \
               str(len( self.dados )) + " itens | " + \
               str(self.latency) + " Device | " + \
               str(self.device) + " Browser | " + \
               str(self.browser) + " Response | " + \
               str(self.response) + " Status | " + \
               str(self.status) + " Size Media| " + \
               str(self.avgsize) + " Size Soma| " + \
               str(self.sumsize) + " Url Geral| " + \
               str(self.referer)

    def calculaMedia( self ):
        latencias = [ x.latency for x in self.dados ]
        self.latency = np.average( latencias )

    def contadorDeviceBrowser( self ):
        
        for registro in self.dados:
            indexD = registro.device
            indexB = registro.browser

            if indexD not in self.device:
                self.device[indexD] = 0
            self.device[ indexD ] = self.device[ indexD ] +1

            if indexB not in self.browser:
                self.browser[indexB] = 0
            self.browser[ indexB ] = self.browser[ indexB ] +1

    def contadorResponse( self ):
        
        for registro in self.dados:
            index = registro.response

            if index not in self.response:
                self.response[index] = 0
            self.response[ index ] = self.response[ index ] +1

    def contadorStatus( self ):
        
        for registro in self.dados:
            index = registro.status

            if index not in self.status:
                self.status[index] = 0
            self.status[ index ] = self.status[ index ] +1

    def calculaMediaScript( self ):
        script = [ x.size for x in self.dados ]
        self.avgsize = np.average( script )
        self.sumsize = np.sum( script )

    def contadorReferer( self ):
        
        for registro in self.dados:
            index = registro.referer

            if index not in self.referer:
                self.referer[index] = 0
            self.referer[ index ] = self.referer[ index ] +1
     