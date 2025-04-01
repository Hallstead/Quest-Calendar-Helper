
import data
import followers
import ship
from util import enter, getBool, getValidChoice, printMenuFromList

def crewmateMenu():
    print("\n--Crewmate Management Menu--")
    print("1. Get Crewmate")
    print("2. Assign Crewmate")
    print("3. Unassign Crewmate")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 3)
    if choice == 1:
        getCrewmate()
    elif choice == 2:
        assignCrewmateSelect()
    elif choice == 3:
        unassignCrewmateSelect()
    elif choice == 0:
        return
    crewmateMenu()

def getCrewmate():
    """Function to get a new crewmate based on available crewmates."""
    print()
    owned_crewmates = {comp[3][0] for comp in data.ship.values() if comp[3][0] != "None"}
    owned_crewmates.update({c[0] for c in data.crew_reserve})
    offers, count = printMenuFromList(data.all_followers["2023"], owned_crewmates, followers.printOneFollower)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    crewmate = offers[choice-1]
    reserveCrewmate(crewmate)
    if getBool(f"Would you like to assign {crewmate[0]} to a compartment?"):
        comp = ship.getComp(3)
        acrew = data.ship[comp][3]
        if not comp:
            return
        elif acrew[0] == "None":
            assignCrewmate(comp, len(data.crew_reserve) - 1)
        else:
            if confirmSwapCrewmates(comp, len(data.crew_reserve) - 1):
                swapCrewmates(comp, len(data.crew_reserve) - 1)
            else:
                print("\nDid not confirm. Leaving Crewmates as assigned.")
                enter()
                return

def reserveCrewmate(crewmate):
    data.crew_reserve.append(crewmate)

def unassignCrewmateSelect():
    """Function to unassign a crewmate."""
    comps_with_assigned_crewmates = [comp for comp in data.ship.keys() if data.ship[comp][3][0] != "None"]  # Get the assigned compartments
    if not comps_with_assigned_crewmates:
        print("No crewmates to unassign.")
        return
    print("\nSelect a crewmate to unassign:")
    comp = ship.getComp(3, comps_with_assigned_crewmates)
    if comp:
        unassignCrewmate(comp)

def assignCrewmateSelect():
    """Function to equip a new crewmate from the reserve."""
    # Extract crewmates that are considered available for equipping
    available_crewmates = [f for f in data.crew_reserve]
    if not available_crewmates:
        print("No available crewmates to assign.")
        return
    print("\nSelect a crewmate to Assign:")
    _, count = printMenuFromList(available_crewmates, None, followers.printOneFollower)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    comp = ship.getComp(3)
    acrew = data.ship[comp][3]
    if not comp:
        return
    elif acrew[0] == "None":
        assignCrewmate(comp, len(data.crew_reserve) - 1)
    else:
        if confirmSwapCrewmates(comp, len(data.crew_reserve) - 1):
            swapCrewmates(comp, len(data.crew_reserve) - 1)
        else:
            print("\nDid not confirm. Leaving Crewmates as assigned.")
            enter()
            return

def assignCrewmate(comp, index):
    """Function to equip a selected crewmate."""
    crewmate = data.crew_reserve.pop(index)  # Getting the selected crewmate from reserve list
    data.ship[comp][3] = crewmate  # Add the selected crewmate to the current compartment's crewmates
    print(f"Assigned {crewmate[0]} to {comp}.")

def unassignCrewmate(comp):
    """Function to unassign a selected crewmate."""
    crewmate = data.ship[comp][3] # Remove from the equipped list in the specified compartment
    reserveCrewmate(crewmate)  # Add back to reserve
    data.ship[comp][3] = ["None"]
    print(f"Unassigned {crewmate[0]}.")

def confirmSwapCrewmates(comp, uIndex):
    print(f"\Compartent -{comp}- already has an assigned crewmate:")
    followers.printOneFollower(data.ship[comp][3])
    print("Attempting to replace them with: ")
    followers.printOneFollower(data.crew_reserve[uIndex])
    return getBool("Would you like to make the swap?")

def swapCrewmates(comp, uIndex):
    e = unassignCrewmate(comp)
    u = assignCrewmate(comp, uIndex)

def loseCrewmate(comp):
    crewmate = data.ship[comp][3]
    if crewmate[0] != "None":
        print(f"Crewmate -{crewmate[0]}- has been lost.")
        data.ship[comp][3] = ["None"]
