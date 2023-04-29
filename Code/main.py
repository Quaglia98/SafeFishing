import BaseConoscenza as KB
import Classificatore as clas
import Grafo as graph
import os.path
from PIL import Image 

#path assoluto per l'apertura dell'immagine
script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir, 'FAO37_sottozone.png'))


def menu(inputUtente):


    if(inputUtente == "classificazione"):
        clas.classificatore()
    elif(inputUtente == "valutazioneClassificatore"):
        clas.valutazione()
    elif(inputUtente == "mostraZoneFAO"):
        im.show()
    elif(inputUtente == "trovaZoneInquinamentoMoltoBasso"):
        lista = KB.trovaZoneMoltoBasso()
        print(lista)
    elif(inputUtente == "trovaZoneInquinamentoBasso"):
        lista = KB.trovaZoneBasso()
        print(lista)
    elif(inputUtente == "trovaZoneInquinamentoModerato"):
        lista = KB.trovaZoneModerato()
        print(lista)
    elif(inputUtente == "trovaZoneInquinamentoAlto"):
        lista = KB.trovaZoneAlto()
        print(lista)
    elif(inputUtente == "trovaZoneInquinamentoMoltoAlto"):
        lista = KB.trovaZoneMoltoAlto()
        print(lista)
    elif(inputUtente == "visualizzaListaInquinamenti"):
        lista = KB.creaListaInquinamenti()
        print(lista)
    elif(inputUtente == "trovaPercorso"):
        zonaPartenza = input("Inserisci la zona FAO di partenza (es. 1.1): ")
        zonaArrivo = input("Inserisci la zona FAO di destinazione (es 1.2): ")
        graph.trovaPercorso(zonaPartenza, zonaArrivo)
    elif(inputUtente == "verificaPassaggio"):
        zonaPartenza = input("Inserisci l'zona da dove vuoi partire (es. 1.1): ")
        zonaArrivo = input("Inserisci l'zona in cui vuoi arrivare (es. 1.2): ")
        KB.domandaPassaggio(zonaPartenza, zonaArrivo)
    elif(inputUtente == "verificaInquinamentoZona"):
        zona = input("Inserisci l'zona di cui vuoi verificare il livello di inquinamento (es. 1.1): ")
        inquinamento = input("Scegli il livello di inquinamento da provare (moltoBasso/basso/moderato/alto/moltoAlto): ")
        KB.domandaInquinamentoZona(zona, inquinamento)
    elif(inputUtente == "esci"):
        print("-------------------------------------------------------------------------\n")
        return 0

if __name__ == '__main__':
    print("-------------------------------------------------------------------------")
    print("Benvenuto in SafeFishing\n")
    print("Comandi disponibili: \n")
    print("- classificazione;\n- valutazioneClassificatore;\n- mostraZoneFAO;\n- trovaZoneInquinamentoMoltoBasso;\n- trovaZoneInquinamentoBasso;\n- trovaZoneInquinamentoModerato;\n- trovaZoneInquinamentoAlto;\n- trovaZoneInquinamentoMoltoAlto;\n- visualizzaListaInquinamenti;\n- trovaPercorso;\n- verificaPassaggio;\n- verificaInquinamentoZona;\n- esci.\n")

    inputUtente = None
    while (inputUtente != "esci"):
        inputUtente = input("Inserire comando: ")
        menu(inputUtente)

