# SafeFishing
Safe-Fishing is a project that originated from the concept of utilizing various learning methods developed in the field of knowledge engineering, which are made available to monitor and regulate fishing activities in the Mediterranean Sea. The project takes into consideration the pollution present in the area.

The Safe-Fishing software uses the division of the Mediterranean and Black Sea into ten regions to simulate the pollution levels of each zone and predict fishing probabilities of certain fish species. It presents the best fishing zones and ideal routes to reach them while avoiding highly polluted areas. The software encourages users to prioritize less polluted zones and can find the least polluted path. Users can also verify routes and check pollution levels. The project was developed to address high data dynamism, and pollution values are randomly assigned to highlight the possibility of variability in real-life applications without reducing the software's reliability and capabilities.

## Topics developed:
* Knowledge base with queries;
* Classifier with decision tree and relative evaluation;
* Weighted graph with "A*" search algorithm.

## Tools and libraries used:
* Pillow;
* Pandas;
* Scikit-learn;
* Numpys

## Commands:
* classification: Executes the classifier.
* classifierEvaluation: Executes classifier evaluation.
* showFAOZones: Shows an image with FAO zones distributed on the map.
* findVeryLowPollutionZones: Finds FAO zones with "very low" pollution.
* findLowPollutionZones: Finds FAO zones with "low" pollution.
* findModeratePollutionZones: Finds FAO zones with "moderate" pollution.
* findHighPollutionZones: Finds FAO zones with "high" pollution.
* findVeryHighPollutionZones: Finds FAO zones with "very high" pollution.
* createPollutionList: Prints the list of possible pollution values that FAO zones can have.
* findPath: Finds an optimal path, if any, between the Start zone and Goal zone.
* requestPassage: Checks the passage from a Start zone to a Goal zone.
* pollutionZoneQuery: Checks if a particular zone has a certain pollution value.
* exit: Closes the program.
