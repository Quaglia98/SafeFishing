import KnowledgeBase as KB
import Classifier as clas
import Graph as graph
import os.path
from PIL import Image 

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir, 'FAO37_sottozone.png'))


def classify():
    clas.classifier()

def evaluate_classifier():
    clas.valutation()

def show_fao_zones():
    im.show()

def find_very_low_pollution_zones():
    zones = KB.findVeryLowPollutionZones()
    print(zones)

def find_low_pollution_zones():
    zones = KB.findLowPollutionZones()
    print(zones)

def find_moderate_pollution_zones():
    zones = KB.findModeratePollutionZones()
    print(zones)

def find_high_pollution_zones():
    zones = KB.findHighPollutionZones()
    print(zones)

def find_very_high_pollution_zones():
    zones = KB.findVeryHighPollutionZones()
    print(zones)

def list_pollutions():
    pollutions = KB.createPollutionList()
    print(pollutions)

def find_route():
    start_zone = input("Enter the starting FAO zone (e.g. 1.1): ")
    end_zone = input("Enter the destination FAO zone (e.g. 1.2): ")
    graph.findPath(start_zone, end_zone)

def check_passage():
    start_zone = input("Enter the starting zone (e.g. 1.1): ")
    end_zone = input("Enter the ending zone (e.g. 1.2): ")
    KB.requestPassage(start_zone, end_zone)

def check_zone_pollution():
    zone = input("Enter the FAO zone to check (e.g. 1.1): ")
    pollution_level = input("Choose the pollution level to test (very low/low/moderate/high/very high): ")
    KB.pollutionZoneQuery(zone, pollution_level)

def exit_program():
    print("-------------------------------------------------------------------------\n")
    return 0



def menu(user_input):
    commands = {
        "classification": classify,
        "classifierEvalutation": evaluate_classifier,
        "showFAOZones": show_fao_zones,
        "findVeryLowPollutionZones": find_very_low_pollution_zones,
        "findLowPollutionZones": find_low_pollution_zones,
        "findModeratePollutionZones": find_moderate_pollution_zones,
        "findHighPollutionZones": find_high_pollution_zones,
        "findVeryHighPollutionZones": find_very_high_pollution_zones,
        "displayPollutionList": list_pollutions,
        "findPath": find_route,
        "verifyPassage": check_passage,
        "verifyPollutionLevel": check_zone_pollution,
        "exit": exit_program
    }
    
    command = commands.get(user_input, None)
    if command is not None:
        command()
    else:
        print("Invalid command.")


if __name__ == '__main__':
    print("-------------------------------------------------------------------------")
    print("Welcome in SafeFishing\n")
    print("Available commands: \n")
    print("- classification\n- classifierEvalutation\n- showFAOZones\n- findVeryLowPollutionZone\n- findLowPollutionZone\n- findModeratePollutionZone\n- findHighPollutionZone\n- findVeryHighPollutionZone\n- displayPollutionList\n- findPath\n- verifyPassage\n- verifyPollutionLevel\n- exit\n")

    OptionInput = None
    while (OptionInput != "exit"):
        OptionInput = input("Enter command: ")
        menu(OptionInput)