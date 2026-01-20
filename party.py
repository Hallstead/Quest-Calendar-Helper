
import random
import data
import followers
from load_save_data import load, save
from util import enter, getBool, getValidChoice, isValidInt, printMenuFromList

def partyMenu():
    print("\n--Party Management Menu--")
    menu_options = ["View Party", "Get Party Member", "Change Party", "Activate Party Member Ability", "Heal Party Member", "Lose Party Member"]
    _, limit = printMenuFromList(menu_options)
    choice = getValidChoice("Selection: ", limit)
    if choice == 1:
        printParty()
    elif choice == 2:
        pb = getPartyBugsSelect()
        if pb != None:
            getPartyMember(pb)
    elif choice == 3:
        changePartySelect()
    elif choice == 4:
        selectPartyMemberForAbility()
    elif choice == 5:
        member = selectPartyMember("to heal")
        healPartyMemberValue(member)
    elif choice == 6:
        losePartyMemberSelect()
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
        print(f"{'Bug' if data.year == 2024 else 'Pet'} {i}: ", end="")
        followers.printOneFollower(b)
        i += 1
    for x in range(i, data.bugs_limit + 1):
        print(f"{'Bug' if data.year == 2024 else 'Pet'} {x}: None")

    printReserve()

def printReserve():
    if len(data.party_reserve) != 0:
        print("\n--Party Reserve--")
        for p in data.party_reserve:
            followers.printOneFollower(p)

def isPartyMember(pm: list):
    if len(pm) < 4:
        raise Exception(f"Party member {pm} is not a valid follower.")
    if pm[3]:
        return True
    return False

def getPartyBugsSelect():
    menu_options = ["Party Member", f"{'Bug' if data.year == 2024 else 'Pet' if data.year == 2026 else 'Bug/Pet'}"]
    _, limit = printMenuFromList(menu_options)
    choice = getValidChoice("Selection: ", limit)
    if choice == 0:
        return None
    elif choice == 1:
        return True
    elif choice == 2:
        return False

def getPartyMember(isPM: bool):
    """Function to get a new party member based on available party members."""
    if data.year == 2026:
        isPM = not isPM
    print()
    owned = {member[0] for member in data.party}
    owned.update({member[0] for member in data.party_reserve})
    offers = [member for member in data.all_followers[str(data.year)] if isPartyMember(member) == isPM]
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
            pIndex = selectPartyMemberIndexForSwap(isPM)
            if pIndex == -1:
                return
            elif confirmSwapPartyMembers(isPM, pIndex, len(data.party_reserve) - 1):
                swapPartyMembers(isPM, pIndex, len(data.party_reserve) - 1)
            else:
                print("\nDid not confirm. Leaving Party as is.")
                enter()
                return

def selectPartyMemberIndexForSwap(isPM: bool):
    party = data.party if isPM else data.bugs
    offers, limit = printMenuFromList(party, None, followers.printOneFollower)
    choice = getValidChoice("Selection: ", limit)
    return choice - 1

def selectPartyMember(text = ""):
    party = [f for f in data.party]
    party.extend(data.bugs)
    if not party:
        print("No party members or bugs to select.")
        return None
    print(f"\nSelect a party member or bug{' ' + text if text else ''}:")
    _, limit = printMenuFromList(party, None, followers.printOneFollower)
    choice = getValidChoice("Selection: ", limit)
    if choice == 0:
        return None
    index = choice - 1
    if index in range(0, len(data.party)):
        return data.party[index]
    else:
        return data.bugs[index - len(data.party)]

def checkRoomInParty(isPM: bool):
    return len(data.party) < data.party_limit if isPM else len(data.bugs) < data.bugs_limit

def reservePartyMember(pm):
    if "/" not in pm[4]:
        split = pm[4].split(" ")
        split[0] = split[0] + "/" + split[0]
        pm[4] = " ".join(split)
    data.party_reserve.append(pm)

def changePartySelect():
    print()
    options = ["To party from reserve", "To reserve from party"]
    _, limit = printMenuFromList(options)
    choice = getValidChoice("Selection: ", limit)
    if choice == 0:
        return
    elif choice == 1:
        addToPartySelect()
    elif choice == 2:
        removePartyMemberSelect()

def removePartyMemberSelect():
    member = selectPartyMember("to remove")
    removeFromParty(member)

def addToPartySelect():
    """Function to equip a party member from the reserve."""
    # Extract crewmates that are considered available for equipping
    available_members = [f for f in data.party_reserve]
    if not available_members:
        print("No available reserved party members or bugs.")
        return
        
    print("\nSelect a party member to Assign:")
    _, count = printMenuFromList(available_members, None, followers.printOneFollower)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    index = choice - 1
    member = available_members[index]
    isPM = isPartyMember(member)
    if checkRoomInParty(isPM):
        addToParty(isPM, index)
    else:
        pIndex = selectPartyMemberIndexForSwap(isPM)
        if pIndex == -1:
            return
        elif confirmSwapPartyMembers(isPM, pIndex, index):
            swapPartyMembers(isPM, pIndex, index)
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
    print(f"Added {member[0]} to the party.")

def removeFromParty(member: list):
    """Function to unassign a selected party member."""
    if isPartyMember(member):
        data.party.pop(data.party.index(member))
    else:
        data.bugs.pop(data.bugs.index(member)) 
    reservePartyMember(member)  # Add back to reserve
    print(f"Removed {member[0]} from the party.")

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

def losePartyMemberSelect():
    losePartyMember(selectPartyMember("to lose"))

def losePartyMember(member):
    isPM = isPartyMember(member)
    if isPM:
        data.party.pop(data.party.index(member))
    else:
        data.bugs.pop(data.party.index(member))

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
        if card["suit"] in targetSuit and card["val"] >= int(targetVal):
            return True
        return False
    
def followerTakesDamage(card: dict) -> bool:
    if card["val"] >= 11:
        return True
    return False
    
def selectPartyMemberForAbility():
    member = selectPartyMember("to activate")
    confirmUsePartyMemberAbility(member)

def confirmUsePartyMemberAbility(member):
    followers.printOneFollower(member)
    if getBool("Would you like to attempt to activate an ability from this party member?"):
        activatePartyMemberAbilities(member)

def activatePartyMemberAbilities(member):
    skill1 = member[2].split("/")
    skill2 = "" if not member[3] else member[3].split("/")
    card = drawCard()
    name, suits, target = skill1
    canUseSkill1 = followerAbilityActivates(card, target, suits)
    canUseSkill2 = False
    if skill2:
        name, suits, target = skill2
        canUseSkill2 = followerAbilityActivates(card, target, suits)
    if canUseSkill1 or canUseSkill2:
        print(f"{member[0]} can use an ability:")
        if canUseSkill1:
            print(f"{skill1[0]}{': ' + str(data.skills_dict[skill1[0]][0]) if skill1[0] in list(data.skills_dict.keys()) else ''}")
        if canUseSkill2:
            print(f"{skill2[0]}{': ' + str(data.skills_dict[skill2[0]][0]) if skill2[0] in list(data.skills_dict.keys()) else ''}")
    else:
        print(f"{member[0]} failed to use an ability.")
    if followerTakesDamage(card):
        damagePartyMember(member)
    enter()

def damagePartyMember(member):
    condition = member[4].split("/")
    condition[0] = str(int(condition[0]) - 1)
    print(f"{member[0]} took a point of damage.")
    member[4] = "/".join(condition)
    if condition[0] == "0":
        print(f"{member[0]} has died.")
        losePartyMember(member)

def healPartyMemberValue(member):
    val = input(f"\nHow much to heal {member[0]}: ")
    if not isValidInt(val):
        return
    val = int(val)
    healPartyMember(member, val)

def healPartyMember(member, val: int):
    condition = member[4].split("/")
    hp = condition[0]
    max_hp = condition[1].split(" ")[0]
    hp = str(min(int(hp) + val, int(max_hp)))
    condition[0] = hp
    print(f"{member[0]} healed. They now have {hp}/{max_hp} health.")
    member[4] = "/".join(condition)

def partyRest():
    for member in data.party:
        healPartyMember(member, 100)
    for member in data.bugs:
        healPartyMember(member, 100)
    for member in data.party_reserve:
        healPartyMember(member, 100)

if __name__ == "__main__":
    load()
    partyMenu()
    save()