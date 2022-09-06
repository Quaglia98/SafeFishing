# SafeFishing
A project realized for the course of ICon (Knowledge Engineering) UNIBA.

The objective is to monitor and regulate the fishing activity in the Zones of Food and Agriculture Organization of the United Nations (FAO), a total of 10 zones spread across Mediterranean and Red Sea, in particular the aim of the project is to provide information about the pollution of the FAO zones, and the user will be able to check which zone has the lowest pollution level, and also which zone is the best for fishing.

The user can insert as input the fish and the zone, then the system will automatically predict which is the probability of fishing that fish in that zone. 
The zones are represented as nodes in a graph for creating the paths.

Topics covered:
- Knowledge Base with interrogations
- Classification tree and K-Fold cross valutation
- Graph with A* searching algorithm

Python libraries:
- Pillow
- Pandas
- Scikit-learn
- Numpy

System features:
- classificazione: Executes the decision tree classifier
- valutazioneClassificatore: Exectutes valutation of the classifier
- mostraZoneFAO: Shows the FAO zones
- trovaZoneInquinamentoMoltoBasso: Shows the zones with a very low pollution level
- trovaZoneInquinamentoBasso: Shows the zones with a low pollution level
- trovaZoneInquinamentoModerato: Shows the zones with a mid pollution level
- trovaZoneInquinamentoAlto: Shows the zones with a high pollution level
- trovaZoneInquinamentoMoltoAlto: Shows the zones with very high pollution level
- visualizzaListaInquinamenti: Shows the list of all the pollution levels
- trovaPercorso: Finds a path from a Zone A to a Zone B
- verificaPassaggio: Verifies the possibility of a transition between zone A and zone B
- verificaInquinamentoZona: Verifies the pollution level of a zone 
- esci: Exit





