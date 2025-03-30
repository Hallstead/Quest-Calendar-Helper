import data
from load_save_data import save
from util import checkValidYear, enter, getBool, getValidChoice, getYear, isValidInt, modifyAttr, printMenuFromList

def equipmentMenu():
    print("\n--Equipment Menu--")
    print("1. View Equipment")
    print("2. Get Equipment")
    print("3. Change Equipment")
    print("4. Lose Equipment")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 4)
    if choice == 1:
        printEquipment()
    elif choice == 2:
        getSlot(getYear())
    elif choice == 3:
        changeEquipment()
    elif choice == 4:
        loseEquipment()
    elif choice == 0:
        return
    equipmentMenu()
  
def printEquipment():
    sortEquipment(data.equipment)
    sortEquipment(data.unequipped)
    print("\n--Equipment--")
    for e in data.equipment:
        printOneEquipment(e)
    if data.unequipped == []:
        return
    print("\n--Unequipped--")
    for u in data.unequipped:
        printOneEquipment(u)

def printOneEquipment(e):
    print(e[0], end="")
    print(f" ({e[1]}): ", end="")
    for i in range(2, len(e)):
        print(e[i], end="")
        if i != len(e) - 1:
            print(", ", end="")
    print()

def getSlot(year):
    if not checkValidYear(year):
        return
    if int(year) == 2021:
        getEquipment(data.all_equipment[str(year)]["all"])
        return
    slot_list = []
    for slot in data.all_equipment[year]:
        slot_list.append(slot)
    slot_list.sort()
    _, count = printMenuFromList(slot_list)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    else:
        getEquipment(data.all_equipment[year][slot_list[choice-1]])
      
def getEquipment(gear_list):
    print()
    equipment_names = [e[0] for e in data.equipment]
    equipment_names += [e[0] for e in data.unequipped]
    offers, count = printMenuFromList(gear_list, equipment_names, printOneEquipment)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    e = offers[choice-1]
    if "+X" in str(e):
        for i in range(len(e)):
            if "+X" in e[i]:
                stat = e[i].split(" ")[1]
                val = getBonus(f"How much is the bonus to {stat} for {e[0]}?", 7)
                e[i] = str(e[i]).replace("+X",f"+{val}")
    data.unequipped.append(e)
    if getBool(f"Would you like to equip {e[0]}?"):
        eIndex = checkForEquippedSlot(e[1])
        if eIndex == -1:
            equip(len(data.unequipped) - 1)
        else:
            if confirmSwapEquipment(e[1], eIndex, len(data.unequipped) - 1):
                swapEquipment(eIndex, len(data.unequipped) - 1)
            else:
                print("\nDid not confirm. Leaving equipement as is.")
                enter()
                return
                    
def changeEquipment():
    print()
    print("1. Equip")
    print("2. Unequip")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 2)
    if choice == 0:
        return
    elif choice == 1:
        equipSelect()
    elif choice == 2:
        unequipSelect()
        
def unequipSelect():
    print()
    sortEquipment(data.equipment)
    _, count = printMenuFromList(data.equipment, None, printOneEquipment)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    unequip(choice-1)

def equipSelect():
    print()
    available_equipment = [e for e in data.unequipped]
    if not available_equipment:
        print("No available equipment to equip.")
        return
    sortEquipment(data.unequipped)
    _, limit = printMenuFromList(data.unequipped, None, printOneEquipment)
    choice = getValidChoice("Selection: ", limit)
    if choice == 0:
        return
    slot = data.unequipped[choice-1][1]
    index = checkForEquippedSlot(slot)
    if index != -1:
        swap = confirmSwapEquipment(slot, index, choice-1)
        if not swap:
            print("\nDid not confirm. Leaving equipement as is.")
            enter()
            return
        swapEquipment(index, choice-1)
    else:
        equip(choice-1)

def checkForEquippedSlot(slot):
    if slot == "Key Item":
        return -1
    for i in range(len(data.equipment)):
        if data.equipment[i][1] == slot:
            return i
    return -1

def confirmSwapEquipment(slot, eIndex, uIndex):
    print(f"\nSlot -{slot}- is already filled by: ")
    printOneEquipment(data.equipment[eIndex])
    print("Attempting to replace it with: ")
    printOneEquipment(data.unequipped[uIndex])
    return getBool("Would you like to make the swap?")

def swapEquipment(eIndex, uIndex):
    e = unequip(eIndex)
    u = equip(uIndex)

def equip(index):
    item = data.unequipped.pop(index)
    data.equipment.append(item)
    for i in range(2, len(item)):
        if "+" in item[i]:
            val = int(item[i].strip("+")[0])
            trait = item[i].split(" ")[1].lower()
            if trait == "health":
                modifyAttr("hp", val)
                modifyAttr("max_hp", val)
            elif trait == "armor":
                modifyAttr("defense", val)
            else:
                modifyAttr(trait, val)
    if item[0] == "Wand of Pain":
        data.abilities.append("Wand of Pain: Use once per Rest. Use in combat to add a d10 to a Damage roll. Ignores all armor to hit automatically.")
    if item[0] == "The Dragon Staff":
        data.abilities.append("The Dragon Staff: Use once per Rest to add d4 to all Damage rolls for the page.")
    print(f"Equipped {item[0]}.")
    save()
    return item

def getBonus(prompt: str, limit: int):
    entry = input(f"{prompt} (0-{limit}): ")
    if entry.isnumeric() and int(entry) >= 0 and int(entry) <= limit:
        return int(entry)
    print("Input is invalid.")
    print("Using 0 in place of invalid input.")
    return 0

def unequip(index):
    item = data.equipment.pop(index)
    data.unequipped.append(item)
    for i in range(2, len(item)):
        if "+" in item[i]:
            val = int(item[i].strip("+")[0])
            trait = item[i].split(" ")[1].lower()
            if trait == "health":
                modifyAttr("hp", -val)
                modifyAttr("max_hp", -val)
            elif trait == "armor":
                modifyAttr("defense", -val)
            else:
                modifyAttr(trait, -val)
    if item[0] == "Wand of Pain":
        data.abilities.pop(data.abilities.index("Wand of Pain: Use once per Rest. Use in combat to add a d10 to a Damage roll. Ignores all armor to hit automatically."))
    if item[0] == "The Dragon Staff":
        data.abilities.pop(data.abilities.index("The Dragon Staff: Use once per Rest to add d4 to all Damage rolls for the page."))
    print(f"Unequipped {item[0]}.")
    save()
    return item

def sortEquipment(list):
    list.sort(key=lambda x: x[1])

def loseEquipment():
    sortEquipment(data.equipment)
    sortEquipment(data.unequipped)
    print()
    print("Select one to lose.")
    print("-Equipped-")
    count = 0
    for e in data.equipment:
        count += 1
        print(f"{count}. ", end="")
        printOneEquipment(e)
    print("-Unequipped-")
    for u in data.unequipped:
        count += 1
        print(f"{count}. ", end="")
        printOneEquipment(u)
    print("0. Go Back")
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    elif choice <= len(data.equipment):
        e = unequip(choice-1)
        del data.unequipped[len(data.unequipped)-1]
        print(f"{e[0]} has been lost.")
    else:
        index = choice - len(data.equipment) - 1
        e = data.unequipped.pop(index)
        print(f"{e[0]} has been lost.")
    save()
