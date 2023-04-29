import pandas as pd
import os.path
from sklearn import tree
from sklearn.model_selection import cross_val_score

script_dir = os.path.dirname(os.path.abspath(__file__))


#Chiede i dati all'utente per poter classificare il nuovo esempio e restituisce la previsione
def classificatore():
    pesce = ""
    zona = ""


    while(pesce !='acciuga' and pesce !='merluzzo' and pesce !='sgombro' and pesce !='pesce_spada' and pesce !='palamita' and pesce !='rana_pescatrice' and pesce !='sardina' and pesce !='lampuga' and pesce !='alaccia' and pesce !='cernia' and pesce !='triglia' and pesce !='tonno'):
            pesce = input("Inserisci il pesce che vorresti pescare (es: tonno): ")
            if(pesce !='acciuga' and pesce !='merluzzo' and pesce !='sgombro' and pesce !='pesce_spada' and pesce !='palamita' and pesce !='rana_pescatrice' and pesce !='sardina' and pesce !='lampuga' and pesce !='alaccia' and pesce !='cernia' and pesce !='triglia' and pesce !='tonno'):
                print("Inserisci un pesce tra: acciuga, merluzzo, sgombro, pesce_spada, palamita, rana_pescatrice, sardina, lampuga, alaccia, cernia, triglia, tonno\n")
            if (pesce == 'acciuga'):
                parametroPesce = 1
            if (pesce == 'merluzzo'):
                parametroPesce = 2
            if (pesce == 'sgombro'):
                parametroPesce = 3
            if (pesce == 'pesce_spada'):
                parametroPesce = 4
            if (pesce == 'palamita'):
                parametroPesce = 5
            if (pesce == 'rana_pescatrice'):
                parametroPesce = 6
            if (pesce == 'sardina'):
                parametroPesce = 7
            if (pesce == 'lampuga'):
                parametroPesce = 8
            if (pesce == 'alaccia'):
                parametroPesce = 9
            if (pesce == 'cernia'):
                parametroPesce = 11
            if (pesce == 'triglia'):
                parametroPesce = 12
            if (pesce == 'tonno'):
                parametroPesce = 13

            
    while(zona!='1.1' and zona!='1.2' and zona!='1.3' and zona!='2.1' and zona!='2.2' and zona!='3.1' and zona!='3.2' and zona!='4.1' and zona!='4.2' and zona!='4.3'):
        zona = input("Inserisci la zona FAO dove vuoi pescare (es: 1.1): ")
        if(zona!='1.1' and zona!='1.2' and zona!='1.3' and zona!='2.1' and zona!='2.2' and zona!='3.1' and zona!='3.2' and zona!='4.1' and zona!='4.2' and zona!='4.3'):
            print("Inserisci una zona FAO valida.")
        if(zona == '1.1'):
            parametroZona= 1
        if(zona == '1.2'):
            parametroZona= 2 
        if(zona == '1.3'):
            parametroZona= 3
        if(zona == '2.1'):
            parametroZona= 4
        if(zona == '2.2'):
            parametroZona= 5
        if(zona == '3.1'):
            parametroZona= 6
        if(zona == '3.2'):
            parametroZona= 7
        if(zona == '4.1'):
            parametroZona= 8
        if(zona == '4.2'):
            parametroZona= 9
        if(zona == '4.3'):
            parametroZona= 10

    probabilita = classificazione(parametroZona, parametroPesce)
    for i in range(len(probabilita)):
        print("la probabilità di pescare quel pesce in quella zona è circa (%): ", probabilita[i])

#Classificatore (albero di decisione)
def classificazione(parametroZona:int, parametroPesce:int):
    
    dataset = pd.read_csv(os.path.join(script_dir, 'probpesca.csv'))


    X = dataset.drop(columns=['prob'])
    y = dataset['prob']

    classificatore = tree.DecisionTreeClassifier()
    classificatore.fit(X.values, y.values)
    probabilita = classificatore.predict([[parametroZona, parametroPesce]])

    return probabilita

#Valutazione classificatore
def valutazione():
    dataset = pd.read_csv(os.path.join(script_dir, 'probpesca.csv'))
    X = dataset.drop(columns=['prob'])
    y = dataset['prob']

    classificatore = tree.DecisionTreeClassifier()
    classificatore.fit(X.values, y.values)
    
    score = cross_val_score(classificatore, X.values, y.values, scoring = 'r2', cv = 5)

    print("%0.2f di accuratezza, con una deviazione standard di %0.2f" % (score.mean(), score.std()))


    

