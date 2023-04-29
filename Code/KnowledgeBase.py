from Graph import nodes

# Creates the list of neighboring zones


def createNeighborZonesList():
    neighborZonesList = {}
    neighborZonesList["1.11.2"] = True
    neighborZonesList["1.11.3"] = True
    neighborZonesList["1.31.2"] = True
    neighborZonesList["1.32.2"] = True
    neighborZonesList["2.12.2"] = True
    neighborZonesList["2.23.1"] = True
    neighborZonesList["2.23.2"] = True
    neighborZonesList["3.13.2"] = True
    neighborZonesList["3.14.1"] = True
    neighborZonesList["4.14.2"] = True
    neighborZonesList["4.24.3"] = True

    return neighborZonesList


neighborZonesList = createNeighborZonesList()

# Returns the list with the pollution values for each zone


def createPollutionValuesList():
    pollutionValuesList = {}
    for i in range(len(nodes)):
        pollution = nodes[i].pollution
        string = (nodes[i].name + "_" + str(pollution))
        pollutionValuesList[string] = True
    return pollutionValuesList


pollutionValuesList = createPollutionValuesList()

# Finds the pollution value for a specific zone


def findPollutionValueForZone(zone_pollution: str):
    if (pollutionValuesList.get(zone_pollution) == None):
        return False
    else:
        return True

# Finds zones with very high pollution value


def findVeryHighPollutionZones():
    veryHighPollutionZones = []
    for i in range(len(nodes)):
        if (nodes[i].pollution == 'veryHigh'):
            veryHighPollutionZones.append(nodes[i].name)
    return veryHighPollutionZones

# Finds zones with high pollution value


def findHighPollutionZones():
    highPollutionZones = []
    for i in range(len(nodes)):
        if (nodes[i].pollution == 'high'):
            highPollutionZones.append(nodes[i].name)
    return highPollutionZones

# Finds zones with moderate pollution value


def findModeratePollutionZones():
    moderatePollutionZones = []
    for i in range(len(nodes)):
        if (nodes[i].pollution == 'moderate'):
            moderatePollutionZones.append(nodes[i].name)
    return moderatePollutionZones

# Finds zones with low pollution value


def findLowPollutionZones():
    lowPollutionZones = []
    for i in range(len(nodes)):
        if (nodes[i].pollution == 'low'):
            lowPollutionZones.append(nodes[i].name)
    return lowPollutionZones

# Finds zones with very low pollution value


def findVeryLowPollutionZones():
    veryLowPollutionZones = []
    for i in range(len(nodes)):
        if (nodes[i].pollution == 'veryLow'):
            veryLowPollutionZones.append(nodes[i].name)
    return veryLowPollutionZones

# Returns the list of pollution levels that the zones could have


def createPollutionList():
    pollutionList = []

    pollutionList.append('veryLow')
    pollutionList.append('low')
    pollutionList.append('moderate')
    pollutionList.append('high')
    pollutionList.append('veryHigh')

    return pollutionList


pollutionList = createPollutionList()

# Checks if the pollution level exists


def checkPollutionLevel(pollution: str):
    for i in range(len(pollutionList)):
        if (pollutionList[i] == pollution):
            return True
    return False

# Verifies that a zone does not have a very high pollution value


def notVeryHighPollution(zone: str):
    if (pollutionValuesList.get(zone + "_veryHigh") == None):
        return True
    else:
        return False

# Verifies the existence of a zone


def zoneExists(zone: str):
    for i in range(len(nodes)):
        if (nodes[i].name == zone):
            return True
    return False


# Check a specific level of pollution for a specific area.
def pollutionZoneQuery(zone: str, pollution_level: str):
    if not zoneExists(zone):
        print("The entered zone does not exist. Please enter a valid zone.")
        return
    if not checkPollutionLevel(pollution_level):
        print("The entered pollution level does not exist. Please enter a valid pollution level.")
        return
    string = zone.capitalize() + "_" + pollution_level
    answer = findPollutionValueForZone(string)
    if answer:
        print("YES")
    else:
        print("NO")
    while True:
        user_input = input(
            "Type (how) for an explanation or (exit) to terminate: ")
        if user_input.lower() == "exit":
            break
        if user_input.lower() == "how":
            print(
                f"Pollution({zone.capitalize()},{pollution_level}) <=> {string}")
            while True:
                user_input = input(
                    "To go into detail, type (how i), with i being the number of the atom, or type (exit) to terminate: ")
                if user_input.lower() == "exit":
                    break
                if user_input.lower() == "how 1":
                    print(f"{string} <=> {answer}")
                elif user_input.lower() not in ["how 1", "exit"]:
                    print(
                        "Attention: you should type (how 1) or (exit) if you want to terminate.")
        elif user_input.lower() not in ["how", "exit"]:
            print("Attention: you should type (how) or (exit) if you want to terminate.")


#Check if it is possible to move from a Zone A to a Zone B
def requestPassage(startingZone: str, destinationZone: str):
    # Check if starting zone exists
    if (not zoneExists(startingZone)):
        print("The starting zone entered does not exist. Please enter a valid zone.")
        return
     # Check if destination zone exists
    if (not zoneExists(destinationZone)):
        print("The destination zone entered does not exist. Please enter a valid zone.")
        return

    failDict = {}
    compareString1 = startingZone + destinationZone
    compareString2 = destinationZone + startingZone
    userInput = ""
    verified = False

    # Check if there's a boundary between starting zone and destination zone
    if (neighborZonesList.get(compareString1) == None or neighborZonesList.get(compareString2) == None):
        failDict[1] = True
    else:
        failDict[1] = False
        
    # Check if starting zone has not very high pollution
    failDict[2] = notVeryHighPollution(startingZone)
    # Check if destination zone has not very high pollution
    failDict[3] = notVeryHighPollution(destinationZone)

    # Print YES if all conditions are met, else print NO
    if (failDict.get(1) == True and failDict.get(2) == True and failDict.get(3) == True):
        print("YES")
    else:
        print("NO")

    # Provide explanation upon request
    while verified is False and userInput.lower() != "how":
        userInput = input(
            "Type (how) for an explanation or (exit) to terminate: ")
        if userInput.lower() == "exit":
            verified = True
        if userInput.lower() == "how":
            print("requestPassage(" + startingZone + ", " + destinationZone + ") <=> boundary(" + startingZone + ","
                  + destinationZone + ") and notVeryHighPollution(" + startingZone + ") and notVeryHighPollution(" + destinationZone + ")")
            
            # Provide more detailed explanation for each condition
            while verified is False and userInput.lower() != "how 1" and userInput.lower() != "how 2" and userInput.lower() != "how 3":
                userInput = input("To get into detail, type (how i), with i being the number of the atom,"
                                  "or type (exit) to terminate: ")
                if (userInput.lower() == "exit"):
                    verified = True
                if (userInput.lower() == 'how 1'):
                    print("boundary(" + startingZone + "," +
                          destinationZone + ") <=>", failDict.get(1))
                else:
                    if (userInput.lower() == 'how 2'):
                        print(
                            "notVeryHighPollution(" + startingZone + ") <=> " + startingZone + " Very low pollution or " +
                            startingZone + " Low pollution or " + startingZone + " Moderate pollution or " + startingZone + " High pollution")
                        while verified is False and userInput.lower() != "how 1" and userInput.lower() != "how 2" and userInput.lower() != "how 3" and userInput.lower() != "how 4":
                            userInput = input(
                                "To get into detail, type (how i), with i being the number of the atom"
                                ",or type (exit) to terminate: ")
                            if userInput == "exit":
                                verified = True
                            if userInput.lower() == "how 1":
                                print(startingZone + " Very low pollution <=> ",
                                      findPollutionValueForZone(startingZone + "_veryLow"))
                            else:
                                if userInput.lower() == "how 2":
                                    print(startingZone + " Low pollution <=> ",
                                          findPollutionValueForZone(startingZone + "_low"))
                                else:
                                    if userInput.lower() == "how 3":
                                        print(startingZone + "_Moderate pollution <=> ",
                                              findPollutionValueForZone(startingZone + "_moderate"))
                                    else:
                                        if userInput.lower() == "how 4":
                                            print(startingZone + "_High pollution <=> ",
                                                  findPollutionValueForZone(startingZone + "_high"))
                                        elif (userInput.lower() != "how 1" and userInput.lower() != "exit" and userInput.lower() != "how 2" and userInput.lower() != "how 3" and userInput.lower() != "how 4"):
                                            print(
                                                "Attention: You should enter (how 1) or (how 2) or (how 3) or (how 4) or (exit) to terminate.")
                                        else:
                                            if (userInput.lower() == 'how 3'):
                                                print(
                                                    "notHighPollution(" + destinationZone + ") <=> " + destinationZone + " Low pollution or " +
                                                    destinationZone + " Moderate pollution or " + destinationZone + " High pollution")
                                            while (verified == False and userInput.lower() != "how 1" and userInput.lower() != "how 2"
                                                and userInput.lower() != "how 3" and userInput.lower() != "how 4"):
                                                userInput = input(
                                                    "To enter details, enter (how i), with i as the number of the atom, or enter (exit) to terminate: ")
                                                if (userInput.lower() == "exit"):
                                                    verified = True
                                                if (userInput.lower() == "how 1"):
                                                    print(destinationZone + "_Low pollution <=> ",
                                                        findPollutionValueForZone(destinationZone + "_low"))
                                                else:
                                                    if (userInput.lower() == "how 2"):
                                                        print(destinationZone + "_Moderate pollution <=> ",
                                                            findPollutionValueForZone(destinationZone + "_moderate"))
                                                    else:
                                                        if (userInput.lower() == "how 3"):
                                                            print(destinationZone + "_High pollution <=> ",
                                                                findPollutionValueForZone(destinationZone + "_high"))
                                                        elif (userInput.lower() != "how 1" and userInput.lower() != "exit"
                                                            and userInput.lower() != "how 2" and userInput.lower() != "how 3" and userInput.lower() != "how 4"):
                                                            print(
                                                                "Attention: You should enter (how 1) or (how 2) or (how 3) or (how 4) or (exit) to terminate.")
                                                        elif (userInput.lower() != "how 1" and userInput.lower() != "exit"
                                                            and userInput.lower() != "how 2" and userInput.lower() != "how 3"):
                                                            print("Attention: You should enter (how 1) or (how 2) or (how 3) or (exit) to terminate.")
                                                        elif (userInput.lower() != "how" and userInput.lower() != "exit"):
                                                            print(userInput)
                                                            print("Attention: You should enter (how) or (exit) to terminate.")