import numpy as np

class Grafo:
    #Inizializza grafo
    def __init__(self, grafoDict=None, orientato=True):
        self.grafoDict = grafoDict or {}
        self.orientato = orientato
        if not orientato:
            self.conversioneNonOrientato()
    #Converte un grafo orientato in non orientato
    def conversioneNonOrientato(self):
        for a in list(self.grafoDict.keys()):
            for (b, dist) in self.grafoDict[a].items():
                self.grafoDict.setdefault(b, {})[a] = dist
    #Aggiunge un collegamento tra nodo A e B con un relativo peso, nel caso di grafo non orientato, aggiunge un ulteriore collegamento da nodo B a nodo A
    def connessione(self, A, B, distanza=1):
        self.grafoDict.setdefault(A, {})[B] = distanza
        if not self.orientato:
            self.grafoDict.setdefault(B, {})[A] = distanza
    #Prende i nodi adiacenti
    def get(self, a, b=None):
        collegamenti = self.grafoDict.setdefault(a, {})
        if b is None:
            return collegamenti
        else:
            return collegamenti.get(b)
    #Restituisce lista di nodi
    def nodi(self):
        s1 = set([k for k in self.grafoDict.keys()])
        s2 = set([k2 for v in self.grafoDict.values() for k2, v2 in v.items()])
        nodi = s1.union(s2)
        return list(nodi)
    #Rimuove dal grafo un nodo, ovvero una zona
    def rimuovi(self, listazone, nomezona):
        for i in range (len(listazone)):
            if(self.grafoDict[listazone[i].name].get(nomezona) != None):
               self.grafoDict[listazone[i].name].pop(nomezona)
        self.grafoDict.pop(nomezona)

class Nodo:
    #Inizializza un nodo
    def __init__(self, nome:str, genitore:str):
        self.nome = nome
        self.genitore = genitore
        #Distanza da nodo iniziale
        self.g = 0
        #Distanza da nodo obiettivo
        self.h = 0
        #Costo totale delle distanze
        self.f = 0
    #Effettua comparazione tra nodi
    def __eq__(self, other):
        return self.nome == other.nome
    #Ordina i nodi in base al costo
    def __lt__(self, other):
         return self.f < other.f
    #Stampa i nodi
    def __repr__(self):
        return ('({0},{1})'.format(self.nome, self.f))


class zona:
    # Initialize the class
    def __init__(self, name: str):
        self.name = name
        self.fattoriInquinanti = creaInquinamento()
        self.inquinamento = assegnaInquinamento(self.fattoriInquinanti)


def creaInquinamento():
    fattoriInquinanti = np.random.randint(100) #valore percentuale
    
    return fattoriInquinanti


def assegnaInquinamento(fattoriInquinanti):
    if (fattoriInquinanti <= 20):
        inquinamento = 'moltoBasso'
    if (fattoriInquinanti > 20 and fattoriInquinanti <= 40):
        inquinamento = 'basso'
    if (fattoriInquinanti > 40 and fattoriInquinanti <= 60):
        inquinamento = 'moderato'
    if (fattoriInquinanti > 60 and fattoriInquinanti <= 80):
        inquinamento = 'alto'
    if (fattoriInquinanti > 80):
        inquinamento = 'moltoAlto'

    return inquinamento

#Calcola il costo del percorso reale da un nodo A ad un nodo B
def calcoloCostoReale(partenza, target):
    costo = (partenza + target) / 2

    return costo

#Stima il costo del percorso da un nodo A ad un nodo B
def calcoloEuristica (partenza, target):
    euristica = (partenza + target) / 2

    return euristica

#Serve per trovare il percorso da una Zona A ad una Zona B nel grafo
#Restituisce un vettore che mantiene tutte le euristiche per le Zone che ci sono in mezzo tra A e B
def vettoreEuristiche (zona:zona, lista):
    euristiche = {}
    for i in range (len(lista)):
            euristiche[lista[i].name] = calcoloEuristica(zona.fattoriInquinanti, lista[i].fattoriInquinanti)
    return euristiche

#Verifica che un nodo adiacente sia stato inserito nella lista dei nodi ancora da esaminare (aperti)
def verificaAggiuntaVicino(open, vicino):
    for nodo in open:
        if (vicino == nodo and vicino.f > nodo.f):
            return False
    return True

#Ricerca A*
def ricercaAStar(grafo, euristiche, partenza: zona, arrivo: zona):

    open = []
    closed = []
    nodoStart = Nodo(partenza.name, None)
    nodoTarget = Nodo(arrivo.name, None)
    open.append(nodoStart)

    while len(open) > 0:
        open.sort()
        nodoCorrente = open.pop(0)
        closed.append(nodoCorrente)

        if nodoCorrente == nodoTarget:
            path = []
            while nodoCorrente != nodoStart:
                path.append(nodoCorrente.nome)
                nodoCorrente = nodoCorrente.genitore
            path.append(nodoStart.nome)
            return path[::-1]
        vicini = grafo.get(nodoCorrente.nome)
        for key, value in vicini.items():
            vicino = Nodo(key, nodoCorrente)
            if (vicino in closed):
                continue
            vicino.g = (nodoCorrente.g + grafo.get(nodoCorrente.nome, vicino.nome)) / 2
            vicino.h = euristiche.get(vicino.nome)
            vicino.f = (vicino.g + vicino.h) / 2
            if (verificaAggiuntaVicino(open, vicino) == True):
                open.append(vicino)
    return None

lista = []
zona1_1 = zona("1.1")
lista.append(zona1_1)
zona1_2 = zona("1.2")
lista.append(zona1_2)
zona1_3 = zona("1.3")
lista.append(zona1_3)
zona2_1 = zona("2.1")
lista.append(zona2_1)
zona2_2 = zona("2.2")
lista.append(zona2_2)
zona3_1 = zona("3.1")
lista.append(zona3_1)
zona3_2 = zona("3.2")
lista.append(zona3_2)
zona4_1 = zona("4.1")
lista.append(zona4_1)
zona4_2 = zona("4.2")
lista.append(zona4_2)
zona4_3 = zona("4.3")
lista.append(zona4_3)


#Genera il grafo con le relative connessioni pesate tra i nodi
def generaGrafo():

    grafo = Grafo()

    grafo.connessione(zona1_1.name, zona1_2.name, calcoloCostoReale(zona1_1.fattoriInquinanti, zona1_2.fattoriInquinanti))
    grafo.connessione(zona1_1.name, zona1_3.name, calcoloCostoReale(zona1_1.fattoriInquinanti, zona1_3.fattoriInquinanti))
    grafo.connessione(zona1_2.name, zona1_3.name, calcoloCostoReale(zona1_2.fattoriInquinanti, zona1_3.fattoriInquinanti))
    grafo.connessione(zona1_3.name, zona2_2.name, calcoloCostoReale(zona1_3.fattoriInquinanti, zona2_2.fattoriInquinanti))
    grafo.connessione(zona2_1.name, zona2_2.name, calcoloCostoReale(zona2_1.fattoriInquinanti, zona2_2.fattoriInquinanti))
    grafo.connessione(zona2_2.name, zona3_1.name, calcoloCostoReale(zona2_2.fattoriInquinanti, zona3_1.fattoriInquinanti))
    grafo.connessione(zona2_2.name, zona3_2.name, calcoloCostoReale(zona2_2.fattoriInquinanti, zona3_2.fattoriInquinanti))
    grafo.connessione(zona3_1.name, zona3_2.name, calcoloCostoReale(zona3_1.fattoriInquinanti, zona3_2.fattoriInquinanti))
    grafo.connessione(zona3_1.name, zona4_1.name, calcoloCostoReale(zona3_1.fattoriInquinanti, zona4_1.fattoriInquinanti))
    grafo.connessione(zona4_1.name, zona4_2.name, calcoloCostoReale(zona4_1.fattoriInquinanti, zona4_2.fattoriInquinanti))
    grafo.connessione(zona4_2.name, zona4_3.name, calcoloCostoReale(zona4_2.fattoriInquinanti, zona4_3.fattoriInquinanti))


    grafo.conversioneNonOrientato()
    zone = lista.copy()
    i = 0

    while (i < (len(zone))):
        if (zone[i].inquinamento == "moltoAlto"):
            grafo.rimuovi(zone, zone[i].name)
            zone.pop(i)
            i = i - 1
        i = i + 1

    return grafo

#Trova percorso da nodo A a nodo B
def trovaPercorso(partenza, arrivo):
    zonaPartenza = None
    zonaArrivo = None
    for i in range(len(lista)):
        if lista[i].name.lower() == partenza.lower():
            zonaPartenza = lista[i]
        if lista[i].name.lower() == arrivo.lower():
            zonaArrivo = lista[i]

    if (zonaPartenza == None or zonaArrivo == None):
        print("Inserimento errato!")
        return
    grafo = generaGrafo()

    euristiche = vettoreEuristiche(zonaArrivo, lista)

    percorso = ricercaAStar(grafo, euristiche, zonaPartenza, zonaArrivo)
    print(percorso)