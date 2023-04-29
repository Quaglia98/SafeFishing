import KnowledgeBase as KB
import Classifier as clas
import Graph as graph
import os.path
from PIL import Image 

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir, 'FAO37_sottozone.png'))


def menu(OptionInput):
    options = {
        "classification": clas.classifier,
        "classifierEvalutation": clas.valutation,
        "showFAOZones": im.show,
        "findVeryLowPollutionZones": KB.findVeryLowPollutionZones,
        "findLowPollutionZones": KB.findLowPollutionZones,
        "findModeratePollutionZones": KB.findModeratePollutionZones,
        "findHighPollutionZones": KB.findHighPollutionZones,
        "findVeryHighPollutionZones": KB.findVeryHighPollutionZones,
        "createPollutionList": KB.createPollutionList,
        "findPath": graph.findPath,
        "requestPassage": KB.requestPassage,
        "pollutionZoneQuery": KB.pollutionZoneQuery,
        "exit": lambda: 0
    }

    if OptionInput in options:
        user_func = options[OptionInput]
        if OptionInput == "findPath":
            starting_zone = input("Insert the departure FAO zone (e.g., 1.1): ")
            destination_zone = input("Insert the destination FAO zone (e.g., 1.2): ")
            user_func(starting_zone, destination_zone)
        elif OptionInput == "verifyPassage":
            starting_zone = input("Insert the starting zone (e.g., 1.1): ")
            destination_zone = input("Insert the destination zone (e.g., 1.2): ")
            user_func(starting_zone, destination_zone)
        elif OptionInput == "verifyPollutionZone":
            zone = input("Insert the zone to check the pollution level (e.g., 1.1): ")
            pollution = input("Choose the pollution level to test (veryLow/low/moderate/high/veryHigh): ")
            user_func(zone, pollution)
        else:
            user_func()
    else:
        print(f"Invalid input: {OptionInput}")


if __name__ == '__main__':
    print("-------------------------------------------------------------------------")
    print("Welcome in SafeFishing\n")
    print("Available commands: \n")
    print("- classification\n- classifierEvalutation\n- showFAOZones\n- findVeryLowPollutionZone\n- findLowPollutionZone\n- findModeratePollutionZone\n- findHighPollutionZone\n- findVeryHighPollutionZone\n- displayPollutionList\n- findPath\n- verifyPassage\n- verifyPollutionLevel\n- exit\n")

    OptionInput = None
    while (OptionInput != "exit"):
        OptionInput = input("Enter command: ")
        menu(OptionInput)

