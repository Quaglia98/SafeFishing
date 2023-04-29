from Grafo import lista

#Crea la lista delle zone confinanti
def creaListaZoneConfinanti():
    listaConfini = {}
    listaConfini["1.11.2"] = True
    listaConfini["1.11.3"] = True
    listaConfini["1.31.2"] = True
    listaConfini["1.32.2"] = True
    listaConfini["2.12.2"] = True
    listaConfini["2.23.1"] = True
    listaConfini["2.23.2"] = True
    listaConfini["3.13.2"] = True
    listaConfini["3.14.1"] = True
    listaConfini["4.14.2"] = True
    listaConfini["4.24.3"] = True
    
    return listaConfini


listaConfiniZone = creaListaZoneConfinanti()


#Restituisce la lista con i valori di inquinamento per ogni zona
def creaListaInquinamentiZone():
    listaInquinamenti = {}
    for i in range(len(lista)):
        inquinamento = lista[i].inquinamento
        stringa = (lista[i].name + "_" + inquinamento)
        listaInquinamenti[stringa] = True
    return listaInquinamenti


listaInquinamentiZone = creaListaInquinamentiZone()

#Trova il valore di inquinamento relativo ad una specifica zona
def trovaInquinamentoZona(zona_inquinamento: str):
    if (listaInquinamentiZone.get(zona_inquinamento) == None):
        return False
    else:
        return True

#Trova le zone con valore inquinamento molto alto
def trovaZoneMoltoAlto():
    listaInquinamentoMoltoAlto = []
    for i in range(len(lista)):
        if (lista[i].inquinamento == 'moltoAlto'):
            listaInquinamentoMoltoAlto.append(lista[i].name)
    return listaInquinamentoMoltoAlto

#Trova le zone con valore inquinamento alto
def trovaZoneAlto():
    listaInquinamentoAlto = []
    for i in range(len(lista)):
        if (lista[i].inquinamento == 'alto'):
            listaInquinamentoAlto.append(lista[i].name)
    return listaInquinamentoAlto

#Trova le zone con valore inquinamento moderato
def trovaZoneModerato():
    listaInquinamentoModerato = []   
    for i in range(len(lista)):
        if (lista[i].inquinamento == 'moderato'):
            listaInquinamentoModerato.append(lista[i].name)
    return listaInquinamentoModerato

#Trova le zone con valore inquinamento basso
def trovaZoneBasso():
    listaInquinamentoBasso = []
    for i in range(len(lista)):
        if (lista[i].inquinamento == 'basso'):
            listaInquinamentoBasso.append(lista[i].name)
    return listaInquinamentoBasso

#Trova le zone con valore Inquinamento molto basso
def trovaZoneMoltoBasso():
    listaInquinamentoMoltoBasso = []
    for i in range(len(lista)):
        if (lista[i].inquinamento == 'moltoBasso'):
            listaInquinamentoMoltoBasso.append(lista[i].name)
    return listaInquinamentoMoltoBasso

#Restituisce la lista dei livelli di inquinamento che le zone potrebbero avere
def creaListaInquinamenti():
    listaInquinamenti = []

    listaInquinamenti.append('moltoBasso')
    listaInquinamenti.append('basso')
    listaInquinamenti.append('moderato')
    listaInquinamenti.append('alto')
    listaInquinamenti.append('moltoAlto')

    return listaInquinamenti


listaInquinamenti = creaListaInquinamenti()

#Controlla se esiste il livello di inquinamento
def controlloInquinamento(inquinamento: str):
    for i in range(len(listaInquinamenti)):
        if (listaInquinamenti[i] == inquinamento):
            return True
    return False

#Verifica che una zona non abbia valore inquinamento molto alto
def notInquinamentoMoltoAlto(zona: str):
    if (listaInquinamentiZone.get(zona + "_moltoAlto") == None):
        return True
    else:
        return False

#Verifica l'esistenza di una Zona
def zonaEsiste(zona: str):
    for i in range(len(lista)):
        if (lista[i].name == zona):
            return True
    return False

#Verifica un determinato valore di inquinamento per una specifica zona
def domandaInquinamentoZona(zona: str, inquinamento: str):

    verifica = False

    if (zonaEsiste(zona)==False):
        print("La zona inserita non esiste, inserire una zona valida")
        return
    if (not controlloInquinamento(inquinamento)):
        print("Il valore di inquinamento inserito non esiste, inserire un Inquinamento valido")
        return

    stringa = zona + "_" + inquinamento
    risposta = trovaInquinamentoZona(stringa)
    if (risposta):
        print("YES")
    else:
        print("NO")

    zona = zona.capitalize()
    while (verifica == False ):
        inputUtente = input("Digitare (how) per la spiegazione o (esci) per terminare: ")
        if (inputUtente.lower() == "esci"):
            verifica = True
        if (inputUtente.lower() == "how"):
            print("Inquinamento(" + zona + "," + inquinamento + ") <=> " + stringa)
            while (verifica == False and inputUtente.lower() != "how 1"):
                inputUtente = input("Per entrare nel dettaglio, digita (how i), con i numero dell'atomo"
                                        ", oppure digita (esci) per terminare: ")
                if (inputUtente.lower() == "esci"):
                    verifica = True
                if (inputUtente.lower() == 'how 1'):
                    print(stringa + " <=> ", risposta)
                elif (inputUtente.lower() != "how 1" and inputUtente.lower() != "esci"):
                    print("Attento: dovresti digitare (how 1) o (esci) se vuoi terminare.")
        elif (inputUtente.lower() != "how" and inputUtente.lower() != "esci"):
            print("Attento: dovresti digitare (how) o (esci) se vuoi terminare.")

#Verifica l'esistenza di un passaggio da una Zona A ad una Zona B
def domandaPassaggio(zonaPartenza: str, zonaArrivo: str):

    if (not zonaEsiste(zonaPartenza)):
        print("La zona di partenza inserita non esiste, inserire una zona valida.")
        return
    if (not zonaEsiste(zonaArrivo)):
        print("La zona di arrivo inserita non esiste, inserire una zona valida.")
        return

    dizFail = {}
    compareString_1 = zonaPartenza + zonaArrivo
    compareString_2 = zonaArrivo + zonaPartenza
    inputUtente = ""
    verifica = False

    if (listaConfiniZone.get(compareString_1) == None or listaConfiniZone.get(compareString_2) == None):
        dizFail[1] = True
    else:
        dizFail[1] = False

    dizFail[2] = notInquinamentoMoltoAlto(zonaPartenza)
    dizFail[3] = notInquinamentoMoltoAlto(zonaArrivo)

    if (dizFail.get(1) == True and dizFail.get(2) == True and dizFail.get(3) == True):
        print("YES")
    else:
        print("NO")

    while(verifica == False and inputUtente.lower() != "how"):
        inputUtente = input("Digitare (how) per la spiegazione o (esci) per terminare: ")
        if(inputUtente.lower() == "esci"):
            verifica = True
        if (inputUtente.lower() == "how"):
            print(
                "passaggio(" + zonaPartenza + "," + zonaArrivo + ") <=> confine(" + zonaPartenza + ","
                + zonaArrivo + ") and notInquinamentoMoltoAlto(" + zonaPartenza + ") and notInquinamentoMoltoAlto(" + zonaArrivo + ")")
            while(verifica == False and inputUtente.lower() != "how 1" and inputUtente.lower() != "how 2"
                        and inputUtente.lower() != "how 3"):
                inputUtente = input("Per entrare nel dettaglio, digita (how i), con i numero dell'atomo"
                                       ", oppure digita (esci) per terminare: ")
                if (inputUtente.lower() == "esci"):
                    verifica = True
                if (inputUtente.lower() == 'how 1'):
                    print("confine(" + zonaPartenza + "," + zonaArrivo + ") <=>", dizFail.get(1))
                else:
                    if (inputUtente.lower() == 'how 2'):
                        print(
                            "notInquinamentoMoltoAlto(" + zonaPartenza + ") <=> " + zonaPartenza + " Inquinamento molto basso o " +
                            zonaPartenza + " Inquinamento basso o " + zonaPartenza + " Inquinamento moderato o " + zonaPartenza + " Inquinamento alto")
                        while(verifica == False and inputUtente.lower() != "how 1" and inputUtente.lower() != "how 2"
                        and inputUtente.lower() != "how 3" and inputUtente.lower() != "how 4"):
                            inputUtente = input(
                                "Per entrare nel dettaglio, digita (how i), con i numero dell'atomo"
                                ", oppure digita (esci) per terminare: ")
                            if (inputUtente == "esci"):
                                verifica = True
                            if (inputUtente.lower() == "how 1"):
                                print(zonaPartenza + " Inquinamento molto basso <=> ",
                                    trovaInquinamentoZona(zonaPartenza + "_moltoBasso"))
                            else:
                                if (inputUtente.lower() == "how 2"):
                                    print(zonaPartenza + "Inquinamento basso <=> ", trovaInquinamentoZona(zonaPartenza + "_basso"))
                                else:
                                    if (inputUtente.lower() == "how 3"):
                                        print(zonaPartenza + "_Inquinamento moderato <=> ",
                                            trovaInquinamentoZona(zonaPartenza + "_moderato"))
                                    else:
                                        if (inputUtente.lower() == "how 4"):
                                            print(zonaPartenza + "_Inquinamento alto <=> ",
                                                trovaInquinamentoZona(zonaPartenza + "_alto"))
                                        elif (inputUtente.lower() != "how 1" and inputUtente.lower() != "esci"
                                        and inputUtente.lower() != "how 2" and inputUtente.lower() != "how 3" and inputUtente.lower() != "how 4"):
                                            print("Attento: dovresti digitare (how 1) o (how 2) o (how 3) o (how 4) o (esci) se vuoi terminare.")
                    else:
                        if (inputUtente.lower() == 'how 3'):
                            print(
                                "notInquinamentoMoltoAlto(" + zonaArrivo + ") <=> " + zonaArrivo + " Inquinamento molto basso o " +
                                zonaArrivo + " Inquinamento basso o " + zonaArrivo + " Inquinamento moderato o " + zonaArrivo + " Inquinamento alto")
                            while (verifica == False and inputUtente.lower() != "how 1" and inputUtente.lower() != "how 2"
                                    and inputUtente.lower() != "how 3" and inputUtente.lower() != "how 4"):
                                inputUtente = input(
                                    "Per entrare nel dettaglio, digita (how i), con i numero dell'atomo"
                                    ", oppure digita (esci) per terminare: ")
                                if (inputUtente.lower() == "esci"):
                                    verifica = True
                                if (inputUtente.lower() == "how 1"):
                                    print(zonaArrivo + "_Inquinamento molto basso <=> ",
                                        trovaInquinamentoZona(zonaArrivo + "_moltoBasso"))
                                else:
                                    if (inputUtente.lower() == "how 2"):
                                        print(zonaArrivo + "_basso <=> ", trovaInquinamentoZona(zonaArrivo + "_basso"))
                                    else:
                                        if (inputUtente.lower() == "how 3"):
                                            print(zonaArrivo + "_moderato <=> ",
                                                trovaInquinamentoZona(zonaArrivo + "_moderato"))
                                        else:
                                            if (inputUtente.lower() == "how 4"):
                                                print(zonaArrivo + "_alto <=> ", trovaInquinamentoZona(zonaArrivo + "_alto"))
                                            elif (inputUtente.lower() != "how 1" and inputUtente.lower() != "esci"
                                            and inputUtente.lower() != "how 2" and inputUtente.lower() != "how 3" and inputUtente.lower() != "how 4"):
                                                print("Attento: dovresti digitare (how 1) o (how 2) o (how 3) o (how 4) o (esci) se vuoi terminare.")
                        elif (inputUtente.lower() != "how 1" and inputUtente.lower() != "esci"
                        and inputUtente.lower() != "how 2" and inputUtente.lower() != "how 3"):
                            print("Attento: dovresti digitare (how 1) o (how 2) o (how 3) o (esci) se vuoi terminare.")
        elif(inputUtente.lower() != "how" and inputUtente.lower() != "esci"):
            print(inputUtente)
            print("Attento: dovresti digitare (how) o (esci) se vuoi terminare.")
