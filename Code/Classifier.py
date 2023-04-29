import pandas as pd
import os.path
from sklearn import tree
from sklearn.model_selection import cross_val_score

script_dir = os.path.dirname(os.path.abspath(__file__))


#It asks the user for data in order to classify the new example and returns the prediction.
def classifier():
    fishes = {
        'anchovy': 1,
        'cod': 2,
        'mackerel': 3,
        'sword_fish': 4,
        'bonito': 5,
        'monk_fish': 6,
        'sardine': 7,
        'dolphin_fish': 8,
        'shad': 9,
        'grouper': 11,
        'red_mullet': 12,
        'tuna': 13
    }
    zones = {
        '1.1': 1,
        '1.2': 2,
        '1.3': 3,
        '2.1': 4,
        '2.2': 5,
        '3.1': 6,
        '3.2': 7,
        '4.1': 8,
        '4.2': 9,
        '4.3': 10
    }
    fish = ""
    zone = ""
    while fish not in fishes:
        fish = input("Enter the fish you would like to catch (e.g. tuna): ")
        if fish not in fishes:
            print("Enter a fish from the following: ", ", ".join(fishes.keys()))

    while zone not in zones:
        zone = input("Enter the FAO area where you want to fish (e.g. 1.1): ")
        if zone not in zones:
            print("Enter a valid FAO area.")

    probability = classification(zones[zone], fishes[fish])
    for prob in probability:
        print("The probability of catching that fish in that area is approximately (%): ", prob)


#classifier (albero di decisione)
def classification(paramZone:int, paramFish:int):
    
    dataset = pd.read_csv(os.path.join(script_dir, 'probfish.csv'))


    X = dataset.drop(columns=['prob'])
    y = dataset['prob']

    classifier = tree.DecisionTreeClassifier()
    classifier.fit(X.values, y.values)
    probability = classifier.predict([[paramZone, paramFish]])

    return probability

#Valutazione classifier
def valutation():
    dataset = pd.read_csv(os.path.join(script_dir, 'probfish.csv'))
    X = dataset.drop(columns=['prob'])
    y = dataset['prob']

    classifier = tree.DecisionTreeClassifier()
    classifier.fit(X.values, y.values)
    
    score = cross_val_score(classifier, X.values, y.values, scoring = 'r2', cv = 5)

    print("%0.2f of accuracy, with a standard deviation of %0.2f" % (score.mean(), score.std()))


    

