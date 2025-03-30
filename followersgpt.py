import random
import data
from load_save_data import load, save
from util import checkValidYear, enter, getBool, getValidChoice, getYear, isValidInt, printMenuFromList

def followersMenu2021(year):
    if not checkValidYear(year):
        return
    print("\n--Followers Menu--")
    print("1. View Followers")
    print("2. Get Follower")
    print("3. Use Follower's Ability")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 3)
    if choice == 1:
        printFollowers()
    elif choice == 2:
        # get Followers
        getFollower2021(year)
    elif choice == 3:
        # use Follower's Ability
        pass
    elif choice == 0:
        # save()
        return
    followersMenu2021(year)

def crewmateMenu():
    print("\n--Crewmate Management Menu--")
    print("1. Get Crewmate")
    print("2. Change Crewmates")
    print("3. Lose Crewmates")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 3)
    if choice == 1:
        getCrewmate()
    elif choice == 2:
        changeCrewmateMenu()
    elif choice == 3:
        loseCrewmate()
    elif choice == 0:
        return
    crewmateMenu()
    
def followersMenu2024(year):
    pass

def printFollowers():
    print("\n--Followers--")
    if len(data.followers) == 0:
        print("(None)")
        return
    for follower in data.followers:
        printOneFollower(follower)

def getFollower2021(year):
    print()
    follower_names = {f[0] for f in data.followers}
    offers, count = printMenuFromList(data.all_followers[str(year)][""], follower_names, printOneFollower)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    f = offers[choice-1]
    if f[0] == "Young Demon":
        if data.virtue > 5:
            print("The Young Demon refuses to join you because your Virtue is too high.")
            return
    data.followers.append(f)

def getCrewmate():
    """Menu to select a crewmate from the available pool."""
    print()
    owned_crewmates = {c[0] for comp in data.ship.values() for c in comp[3] if c[0] != "None"}
    owned_crewmates.update({c[0] for c in data.crewmate_reserve})
    offers, count = printMenuFromList(data.all_followers["2023"][""], owned_crewmates, printOneFollower)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    addCrewmate(offers[choice-1])
    if getBool(f"Would you like to assign {offers[choice-1][0]} to a compartment?"):
        assignCrewmate(offers[choice-1])

def addCrewmate(crewmate):
    """Adds a crewmate to the reserve."""
    data.crewmate_reserve.append(crewmate)
    print(f"{crewmate[0]} has joined the crew.")
    save()

def assignCrewmateMenu():
    """Menu to assign a crewmate to a compartment."""
    print()
    if not data.crewmate_reserve:
        print("No available crewmates to assign.")
        return
    _, count = printMenuFromList(data.crewmate_reserve)
    choice = getValidChoice("Select crewmate to assign: ", count)
    if choice == 0:
        return
    crewmate = data.crewmate_reserve.pop(choice-1)
    assignCrewmate(crewmate)

def assignCrewmate(crewmate):
    """Assigns a crewmate to a compartment, with swap confirmation if necessary."""
    print()
    compartments = list(data.ship.keys())
    compartment_list = [(comp, data.ship[comp][3][0][0] if data.ship[comp][3] and data.ship[comp][3] != ["None"] else "None") for comp in compartments]
    _, count = printMenuFromList([f"{comp} - {crew}" for comp, crew in compartment_list])
    choice = getValidChoice("Select a compartment: ", count)
    if choice == 0:
        data.crewmate_reserve.append(crewmate)
        return
    comp = compartment_list[choice-1][0]
    if data.ship[comp][3] and data.ship[comp][3] != ["None"]:
        print(f"{comp} already has {data.ship[comp][3][0][0]} assigned.")
        if getBool("Would you like to swap?"):
            removed = data.ship[comp][3].pop()
            data.crewmate_reserve.append(removed)
            print(f"{removed[0]} has been moved to the reserve.")
        else:
            data.crewmate_reserve.append(crewmate)
            return
    data.ship[comp][3] = [crewmate]
    data.crewmate_reserve.remove(crewmate)
    print(f"{crewmate[0]} assigned to {comp}.")
    save()

def changeCrewmateMenu():
    """Menu to move or remove a crewmate from a compartment."""
    print()
    compartments = [comp for comp in data.ship if data.ship[comp][3] and data.ship[comp][3] != ["None"]]
    if not compartments:
        print("No assigned crewmates to move or remove.")
        return
    _, count = printMenuFromList(compartments)
    choice = getValidChoice("Select a compartment: ", count)
    if choice == 0:
        return
    comp = compartments[choice-1]
    _, count = printMenuFromList(data.ship[comp][3])
    choice = getValidChoice("Select a crewmate: ", count)
    if choice == 0:
        return
    crewmate = data.ship[comp][3].pop(choice-1)
    print("1. Reassign")
    print("2. Remove")
    print("0. Cancel")
    choice = getValidChoice("Selection: ", 2)
    if choice == 1:
        assignCrewmate(crewmate)
    elif choice == 2:
        removeCrewmate(crewmate)
    else:
        data.ship[comp][3].append(crewmate)

def removeCrewmate(crewmate):
    """Removes a crewmate from the crew."""
    print(f"{crewmate[0]} has left the crew.")
    save()

def loseCrewmate():
    """Menu to select a crewmate to lose."""
    print()
    all_crewmates = [(comp, c) for comp in data.ship for c in data.ship[comp][3] if c != ["None"]] + [("Reserve", c) for c in data.crewmate_reserve if c != ["None"]]
    if not all_crewmates:
        print("No crewmates to lose.")
        return
    offers, count = printMenuFromList([c[1] for c in all_crewmates])
    choice = getValidChoice("Select crewmate to lose: ", count)
    if choice == 0:
        return
    comp, crewmate = all_crewmates[choice-1]
    if comp == "Reserve":
        data.crewmate_reserve.remove(crewmate)
    else:
        data.ship[comp][3].remove(crewmate)
    removeCrewmate(crewmate)


def printOneFollower(f):
    if f[0] == "None":
        print("(None)")
        return
    fname = f[0]
    year = f[1]
    skill1 = f[2]
    skill2 = f[3]
    condition = f[4]
    print(fname)
    if year == "2024":
        skill, suits, val = skill1.split(":")
        print(f"      {skill}: {suits} >= {val}")
        if skill2:
            skill, suits, val = skill2.split(":")
            print(f"      {skill}: {suits} >= {val}")
        if condition:
            print(f"      {condition}")
    else:
        if "+" in skill1:
            print(f"      {skill1}")
        else:
            print(f"      {skill1}: {data.skills_dict[skill1][0]}")
        if skill2:
            print(f"      {skill2}: {data.skills_dict[skill2][0]}")
        if condition:
            print(f"      {condition}")

def printAllFollowers(year = None):
    print("\n--Followers--")
    if year:
        print(year)
        for key in data.all_followers[str(year)]:
            for f in data.all_followers[str(year)][key]:
                printOneFollower(f)
        return
    else:
        for year in data.all_followers:
            print(year)
            for key in data.all_followers[str(year)]:
                for f in data.all_followers[str(year)][key]:
                    printOneFollower(f)

def bodyGuardTakesDamage(val: int):
    if val < 0:
        print("The Body Guard cannot be healed.")
        return
    print("here")
    for i, f in enumerate(data.followers):
        if f[0] != "Body Guard":
            continue
        desc = f[-1].split(" ")
        desc[7] = str(int(desc[7])-val)
        data.followers[i][-1] = " ".join(desc)

def loseFollower(fname, year = None):
    for i in range(len(data.followers)):
        if data.followers[i][0] == fname and not year:
            data.followers.pop(i)
            return True
        elif data.followers[i][0] == fname and year == data.followers[i][1]:
            data.followers.pop(i)
            return True
    return False

def loseAtDeathFollowers():
    for follower in data.followers:
        fname = follower[0]
        if fname == "Burglars":
            # TODO: Generic currency
            data.gold = 0
            print("The Burglars have run off with all your gold.")
            loseFollower(fname, "2021")
        if follower[0] == "Minstrel" and follower[1] == "2021":
            print("The Mintrel has left your group.")
            loseFollower(fname)
        if follower[0] == "Priestess":
            print("The Priestess has left your group.")
            loseFollower(fname)

def loseAtRestFollowers():
    for follower in data.followers:
        fname = follower[0]
        if fname == "Arificer" and follower[1] == "2021":
            if not getBool("Have you used the Arificer's Gadget ability since your last Rest?"):
                print("The Arificer has left your group.")
                loseFollower(fname)
        if fname == "Baby Dragon":
            if "Meal Rations" in data.inventory and data.inventory["Meal Rations"] >= 4:
                if getBool(f"You have {data.inventory['Meal Rations']}x Meal Rations.\nWill you feed 4 of them to the Baby Dragon?"):
                    data.inventory['Meal Rations'] -= 4
                    print("4 Meal Rations were fed to the Baby Dragon.")
                else:
                    print("You did not feed the Baby Dragon, so it left.")
                    loseFollower(fname)
            else:
                print("You did not have enough Meal Rations to feed the Baby Dragon, so it left.")
                loseFollower(fname)
        if fname in ["Thief", "Warrior", "Tracker", "Raiders", "Sentry", "Sorceress", "Bodyguard", "Mage"]:
            upkeep = int(follower[-1].split(": ")[1].split(" ")[0])
            if data.gold >= upkeep:
                if getBool(f"You have {data.gold} gold.\nWill you pay the {upkeep} gold upkeep cost for the {fname}?"):
                    data.gold -= upkeep
                    print(f"You paid the upkeep cost to keep the {fname}.")
                else:
                    print(f"You did pay the upkeep cost for the {fname}, so they left.")
                    loseFollower(fname)
            else:
                print(f"You did not have enough gold to pay the upkeep cost for the {fname}, so they left.")
                loseFollower(fname)

def loseAtVirtueFollowers():
    if data.virtue > 5:
        for follower in data.followers:
            if follower[0] == "Young Demon":
                print("Your virtue is too high for the Young Demon to stay with you. It leaves.")
                loseFollower("Young Demon")
                return

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
    crewmateMenu()
