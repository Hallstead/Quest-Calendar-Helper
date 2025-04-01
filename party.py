
import random
import data
import followers
from load_save_data import load, save
import ship
from util import enter, getBool, getValidChoice, printMenuFromList


def partyMenu():
    print("\n--Party Management Menu--")
    print("1. View Party")
    print("2. Get Party Member")
    print("3. Change Paety")
    print("4. Lose Party Member")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 4)
    if choice == 1:
        printParty()
    elif choice == 2:
        pb = getPartyBugsSelect()
        if pb != None:
            getPartyMember(pb)
    elif choice == 3:
        assignCrewmateSelect()
    elif choice == 4:
        removePartyMemberSelect()
    elif choice == 0:
        return
    partyMenu()

def printParty():
    print("\n--Party--")
    i = 1
    for p in data.party:
        print(f"Slot {i}: ", end="")
        followers.printOneFollower(p)
        i += 1
    for x in range(i, data.party_limit + 1):
        print(f"Slot {x}: None")
    i = 1
    for b in data.bugs:
        print(f"Bug {i}: ", end="")
        followers.printOneFollower(b)
        i += 1
    for x in range(i, data.bugs_limit + 1):
        print(f"Bug {x}: None")

def isPartyMember(pm: list):
    if len(pm) < 4:
        raise Exception(f"Party member {pm} is not a valid follower.")
    if pm[3]:
        return True
    return False

def getPartyBugsSelect():
    menu_options = ["Party Member", "Bug"]
    _, limit = printMenuFromList(menu_options)
    choice = getValidChoice("Selection: ", limit)
    if choice == 0:
        return None
    elif choice == 1:
        return True
    elif choice == 2:
        return False

def getPartyMember(isPM: bool):
    """Function to get a new crewmate based on available crewmates."""
    print()
    owned = {member[0] for member in data.party}
    owned.update({member[0] for member in data.party_reserve})
    offers = [member for member in data.all_followers["2024"] if isPartyMember(member) == isPM]
    offers, count = printMenuFromList(offers, owned, followers.printOneFollower)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    member = offers[choice-1]
    reservePartyMember(member)
    if getBool(f"Would you like to add {member[0]} to your party?"):
        if checkRoomInParty(isPM):
            addToParty(isPM, len(data.party_reserve) - 1)
        else:
            pIndex = selectPartyMemberIndex(isPM)
            if pIndex == -1:
                return
            elif confirmSwapPartyMembers(isPM, pIndex, len(data.party_reserve) - 1):
                swapPartyMembers(isPM, pIndex, len(data.party_reserve) - 1)
            else:
                print("\nDid not confirm. Leaving Party as is.")
                enter()
                return

def selectPartyMemberIndex(isPM: bool):
    party = data.party if isPM else data.bugs
    offers, limit = printMenuFromList(party, None, followers.printOneFollower)
    choice = getValidChoice("Selection: ", limit)
    return choice - 1

def checkRoomInParty(isPM: bool):
    return len(data.party) < data.party_limit if isPM else len(data.bugs) < data.bugs_limit

def reservePartyMember(pm):
    data.party_reserve.append(pm)

def removePartyMemberSelect():
    party = data.party
    party.extend(data.bugs)
    if not party:
        print("No party members or bugs to remove.")
        return
    print("\nSelect a party member or bug to remove:")
    comp = ship.getComp(3, party)
    if comp:
        removeFromParty(comp)

def assignCrewmateSelect():
    """Function to equip a new crewmate from the reserve."""
    # Extract crewmates that are considered available for equipping
    available_crewmates = [f for f in data.party_reserve]
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
        addToParty(comp, len(data.party_reserve) - 1)
    else:
        if confirmSwapPartyMembers(comp, len(data.party_reserve) - 1):
            swapPartyMembers(comp, len(data.party_reserve) - 1)
        else:
            print("\nDid not confirm. Leaving Party as is.")
            enter()
            return

def addToParty(isPM: bool, index: int) -> None:
    if not checkRoomInParty(isPM):
        print("Not enough room in the party")
        return
    member = data.party_reserve.pop(index)  # Getting the selected crewmate from reserve list
    if isPM:
        data.party.append(member)
    else:
        data.bugs.append(member)
    print(f"Added {member} to the party.")

def removeFromParty(isPM: bool, index: int):
    """Function to unassign a selected crewmate."""
    crewmate = data.ship[3] # Remove from the equipped list in the specified compartment
    reservePartyMember(crewmate)  # Add back to reserve
    data.ship[3] = ["None"]
    print(f"Unassigned {crewmate[0]}.")

def confirmSwapPartyMembers(isPM: bool, pIndex: int, rIndex: int):
    pm = data.party[pIndex] if isPM else data.bugs[pIndex]
    rm = data.party_reserve[rIndex]
    print(f"\nAttempting to swap the current party member:")
    followers.printOneFollower(pm)
    print("with this member: ")
    followers.printOneFollower(rm)
    return getBool("Would you like to make the swap?")

def swapPartyMembers(isPM: bool, pIndex: int, uIndex: int):
    removeFromParty(isPM, pIndex)
    addToParty(isPM, uIndex)

def loseCrewmate(comp):
    crewmate = data.ship[comp][3]
    if crewmate[0] != "None":
        print(f"Crewmate -{crewmate[0]}- has been lost.")
        data.ship[comp][3] = ["None"]

def drawCard():
    colors = ["Red", "Black"]
    suits = {"Red": ["Hearts", "Diamonds"], "Black":["Clubs", "Spades"]}
    color = random.choice(colors)
    num = random.randint(0, 26)
    if num == 0:
        print(f"You drew the {color} Joker.")
        return {"color": color, "val": 14, "suit": "J"}
    else:
        val = (num - 1) % 13 + 1
        suit = suits[color][(num-1)//13]
        cardName = ""
        if val == 1:
            cardName = "Ace"
        elif val == 11:
            cardName = "Jack"
        elif val == 12:
            cardName = "Queen"
        elif val == 13:
            cardName = "King"
        else:
            cardName = str(val)
        print(f"You drew the {cardName} of {suit}.")
        return {"color": color, "val": val, "suit": suit[0]}

def followerAbilityActivates(card: dict, targetVal: int, targetSuit: str) -> bool:
    if card["suit"] == "J":
        if card["color"] == "Red" and ("D" in targetSuit or "H" in targetSuit):
            return True
        elif card["color"] == "Black" and ("S" in targetSuit or "C" in targetSuit):
            return True
        else:
            return False
    else:
        if card["suit"] in targetSuit and card["val"] >= targetVal:
            return True
        return False
    
def followerTakesDamage(card: dict) -> bool:
    if card["val"] >= 11:
        return True
    return False
    
if __name__ == "__main__":
    load()
    partyMenu()
    save()