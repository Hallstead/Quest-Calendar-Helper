
import random
import data
import followers
from hp import modifyHP
from load_save_data import load, save
from util import enter, getBool, getValidChoice, getYear, isValidInt, modifyAttr, printMenuFromList

def shipMenu():
    print("\n--Ship Management Menu--")
    print("1. View Ship")
    print("2. Damage/Repair Compartment")
    print("3. Manage Ship Upgrades")
    print("4. Manage Crewmates")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 4)
    if choice == 1:
        # view ship compartments
        printShip()
        enter()
    elif choice == 2:
        # damage/repair a compartment
        compHPMenu()
    elif choice == 3:
        # manage ship upgrades
        upgradesMenu()
    elif choice == 4:
        # manage crewmates
        followers.crewmateMenu()
    elif choice == 0:
        return
    shipMenu()

def upgradesMenu():
    print("\n--Upgrades Menu--")
    print("1. Get Upgrade")
    print("2. Change Upgrade")
    print("3. Lose Upgrade")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 3)
    if choice == 1:
        getUpgrade(getComp())
    elif choice == 2:
        changeUpgrade()
    elif choice == 3:
        loseUpgradeSelect()
    elif choice == 0:
        return
    upgradesMenu()

def printShip():
    print("\n--Ship--")
    print(f"Aim: +{data.aim}")
    print(f"Evasion: +{data.evasion}")
    print(f"Shield: +{data.shield}\n")
    for comp in data.ship:
        printOneCompartmentFull(comp)
    if data.crewmate_reserve:
        print("\n--Crewmate Reserve--")
        for c in data.crewmate_reserve:
            followers.printOneFollower(c)
    
def printOneCompartmentFull(comp: list):
    chp = data.ship[comp][0]
    max_chp = data.ship[comp][1]
    upgrade = data.ship[comp][2]
    crewmate = data.ship[comp][3]
    print(comp + ": ", end="")
    print(f"{chp}/{max_chp} Integrity")
    print("   Upgrade: ", end="")
    printOneUpgrade(upgrade)
    print("   Follower: ", end="")
    followers.printOneFollower(crewmate)

def printOneCompartmentShort(comp: list):
    chp = data.ship[comp][0]
    max_chp = data.ship[comp][1]
    upgrade = data.ship[comp][2]
    crewmate = data.ship[comp][3]
    print(f"{comp} ({chp}/{max_chp}): ", end="")
    print(f"{upgrade[0]}/{crewmate[0]}")

def printOneUpgrade(upgrade: list):
    if upgrade[0] == "None":
        print("(None)")
        return
    print(f"{upgrade[0]}, {upgrade[1]}, {upgrade[2]}")

def compHPMenu():
    print("\n--Damage/Repair Compartment Menu--")
    print("1. Restore Integrity")
    print("2. Take Damage")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 2)
    if choice == 0:
        return
    elif choice == 1:
        repairComp()
    elif choice == 2:
        val = getShipDamage()
        if val:
            comps = getRandomComps(val)
            for comp in comps:
                damageComp(comp)
    compHPMenu()

def repairComp():
    print("\nSelect a compartment to repair:")

    def printCompartment(comp):
        chp, max_chp, _, _ = data.ship[comp]
        print(f"{comp}: {chp}/{max_chp} HP")

    comp_list = list(data.ship.keys())
    offers, count = printMenuFromList(comp_list, printOne=printCompartment)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    comp = offers[choice - 1]
    chp, max_chp, _, _ = data.ship[comp]
    if chp < max_chp:
        data.ship[comp][0] = min(chp + 1, max_chp)
        print(f"{comp} repaired to {data.ship[comp][0]}/{max_chp} HP.")
    else:
        print(f"{comp} is already at full integrity.")

def getRandomComps(val: int):
    return random.choices(list(data.ship.keys()), k=val)

def getShipDamage() -> int:
    val = input("How much damage did your ship take (after Shield): ")
    if not val.isnumeric() or int(val) < 0:
        print("Invalid value.")
        enter()
        return 0
    return int(val)

def damageComp(comp):
    hp = data.ship[comp][0]
    if hp > 0:
        hp -= 1
        print(f"{comp} took 1 damage.")
        data.ship[comp][0] = hp
        if hp == 0:
            destroyComp(comp)
    elif hp == 0:
        print(f"{comp} was already destroyed. You took 1 damage.")
        modifyHP(-1)

def destroyComp(comp):
    print(f"{comp} was destroyed.")
    upgrade = data.ship[comp][2]
    if upgrade != ["None"]:
        loseUpgrade(upgrade)
    followers.loseCrewmate(comp)

def getComp(index: int = None, given_comp_list: list = None):
    print()
    comp_list = None
    if given_comp_list:
        comp_list = [comp for comp in given_comp_list]
    else:
        comp_list = [comp for comp in data.ship.keys()]
    count = None
    if not index:
        _, count = printMenuFromList(comp_list)
    elif index == 2:
        _, count = printMenuFromList(comp_list, None, printCompAndUpgrade)
    elif index == 3:
        _, count = printMenuFromList(comp_list, None, printCompAndCrewmate)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return None
    else:
        return comp_list[choice-1]
    
def printCompAndUpgrade(comp):
    crewmate = data.ship[comp][3]
    if crewmate[0] == "None":
        print("None")
    else:
        print(f"{comp} - ", end = "")
        printOneUpgrade(data.ship[comp][2])
    
def printCompAndCrewmate(comp):
    crewmate = data.ship[comp][3]
    if crewmate[0] == "None":
        print(f"{comp} - None")
    else:
        print(f"{comp} - {data.ship[comp][3][0]} ({data.ship[comp][3][2]}, {data.ship[comp][3][3]})")
      
def getUpgrade(comp):
    print()
    owned_upgrades = [data.ship[comp][2][0]] if data.ship[comp][2][0] != "None" else []
    owned_upgrades += [u[0] for u in data.unequipped_ship_upgrades]
    offers, count = printMenuFromList(data.all_ship_upgrades[comp], owned_upgrades, printOneUpgrade)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    u = offers[choice-1]
    data.unequipped_ship_upgrades.append(u)
    if getBool(f"Would you like to attach {u[0]}?"):
        filled = checkForUpgradedCompartment(comp)
        if not filled:
            upgradeComp(comp, len(data.unequipped_ship_upgrades) - 1)
        else:
            if confirmSwapUpgrades(u[1], len(data.unequipped_ship_upgrades) - 1):
                swapUpgrades(comp, len(data.unequipped_ship_upgrades) - 1)
            else:
                print("\nDid not confirm. Leaving Ship as it is.")
                enter()
                return
                    
def changeUpgrade():
    print()
    print("1. Upgrade Compartment")
    print("2. Downgrade Compartment")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 2)
    if choice == 0:
        return
    elif choice == 1:
        upgradeSelect()
    elif choice == 2:
        downgradeSelect()
        
def downgradeSelect():
    print()
    #sortEquipment(data.equipment)
    upgrades = [data.ship[comp][2] for comp in data.ship if data.ship[comp][2] != ["None"]]
    _, count = printMenuFromList(upgrades, None, printOneUpgrade)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    downgradeComp(upgrades[choice-1][1])

def upgradeSelect():
    print()
    sortUpgrades(data.unequipped_ship_upgrades)
    _, limit = printMenuFromList(data.unequipped_ship_upgrades, None, printOneUpgrade)
    choice = getValidChoice("Selection: ", limit)
    if choice == 0:
        return
    comp = data.unequipped_ship_upgrades[choice-1][1]
    if checkForUpgradedCompartment(comp):
        swap = confirmSwapUpgrades(comp, choice-1)
        if not swap:
            print("\nDid not confirm. Leaving equipement as is.")
            enter()
            return
        swapUpgrades(comp, choice-1)
    else:
        upgradeComp(comp, choice-1)

def checkForUpgradedCompartment(comp):
    if data.ship[comp][2] != ["None"]:
        return True
    return False

def confirmSwapUpgrades(comp, uIndex):
    print(f"\nCompartment -{comp}- is already upgraded with: ")
    printOneUpgrade(data.ship[comp][2])
    print("Attempting to replace upgrade with: ")
    printOneUpgrade(data.unequipped_ship_upgrades[uIndex])
    return getBool("Would you like to make the swap?")

def swapUpgrades(comp, uIndex):
    downgradeComp(comp)
    upgradeComp(comp, uIndex)

def upgradeComp(comp, index):
    upgrade = data.unequipped_ship_upgrades.pop(index)
    data.ship[comp][2] = upgrade
    for i in range(2, len(upgrade)):
        if "+" in upgrade[i]:
            val = int(upgrade[i].strip("+").split(" ")[0])
            stat = upgrade[i].split(" ")[1].lower()
            if stat == "integrity":
                data.ship[comp][0] += val
                data.ship[comp][1] += val
            else:
                modifyAttr(stat, val)
    print(f"Added {upgrade[0]} to {comp}.")
    save()
    return upgrade

def getBonus(prompt: str, limit: int):
    entry = input(f"{prompt} (0-{limit}): ")
    if entry.isnumeric() and int(entry) >= 0 and int(entry) <= limit:
        return int(entry)
    print("Input is invalid.")
    print("Using 0 in place of invalid input.")
    return 0

def downgradeComp(comp):
    upgrade = data.ship[comp][2]
    data.ship[comp][2] = ["None"]
    data.unequipped_ship_upgrades.append(upgrade)
    for i in range(2, len(upgrade)):
        if "+" in upgrade[i]:
            val = int(upgrade[i].strip("+").split(" ")[0])
            stat = upgrade[i].split(" ")[1].lower()
            if stat == "integrity":
                data.ship[comp][0] -= val
                data.ship[comp][1] -= val
                if data.ship[comp][0] <= 0:
                    destroyComp(comp)
            else:
                modifyAttr(stat, -val)
    print(f"Removed {upgrade[0]} from {comp}.")
    save()
    return upgrade

def sortUpgrades(list):
    list.sort(key=lambda x: x[1])

def loseUpgrade(upgrade):
    """Finds and removes an upgrade from either data.ship or data.unequipped_ship_upgrades."""
    
    # Check if the upgrade is in the specified compartment
    comp = upgrade[1]  # Extract compartment from the upgrade
    if comp in data.ship:
        details = data.ship[comp]
        current_upgrade = details[2]  # Upgrade is stored at index 2 in the compartment list
        if current_upgrade[0] == upgrade[0]:  # Match by upgrade name
            downgradeComp(comp)  # Moves the upgrade to unequipped list
    
    # Check if the upgrade is in unequipped_ship_upgrades
    for i, u in enumerate(reversed(data.unequipped_ship_upgrades)):
        if u[0] == upgrade[0]:  # Match by upgrade name
            removed = data.unequipped_ship_upgrades.pop(i)
            print(f"{removed[0]} has been lost.")
            save()
            return
    
    print(f"Upgrade '{upgrade[0]}' not found.")  # If the upgrade doesn't exist

def loseUpgradeSelect():
    """Displays the menu for losing an upgrade and calls upgradeLost()."""
    sortUpgrades(data.unequipped)
    print("\nSelect one to lose.")
    upgrades = []
    print("-In Compartments-")
    count = 0
    for comp, details in data.ship.items():
        upgrade = details[2]
        if upgrade != ["None"]:
            count += 1
            print(f"{count}. ", end="")
            printOneUpgrade(upgrade)
            upgrades.append(upgrade)  # Store name for lookup
    print("-Unused Upgrades-")
    for u in data.unequipped_ship_upgrades:
        count += 1
        print(f"{count}. ", end="")
        printOneUpgrade(u)
        upgrades.append(u[0])  # Store name for lookup
    print("0. Go Back")
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    loseUpgrade(upgrades[choice - 1])  # Pass upgrade name to upgradeLost
        
if __name__ == "__main__":
    load()
    shipMenu()