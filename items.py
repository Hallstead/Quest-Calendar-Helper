import random
import data
from load_save_data import save
from util import checkValidYear, enter, getValidChoice, getYear, isValidInt, printMenuFromList

special_items = ["Map & Compass", "Lockpicking Tools", "Sharpened Weapon", "Fortified Weapon", "Horse", "Mule", "Seaquine", "Row Boat", "Magical Boat", "Spellbook"]

def itemMenu():
    printItems()
    print("\n--Item Menu--")
    options = ["List Inventory", "Gain Item", "Use Item", "Find Backpack Item"]
    _, limit = printMenuFromList(options)
    choice = getValidChoice("Selection: ", limit)
    if choice != 0:
        print()
    if choice == 1:
        # printItems()
        pass
    elif choice == 2:
        year = data.year
        if not year:
            year = getYear()
        gainItem(year)
    elif choice == 3:
        useItem()
    elif choice == 4:
        find_backpack_item()
    elif choice == 0:
        return
    itemMenu()
        
def gainItem(year):
    if not checkValidYear(year):
        return
    item_list = []
    count = 0
    for item in data.item_dict:
        if str(year) in data.item_dict[item][1]:
            count += 1
            item_list.append(item)
            print(f"{count}. {item}")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    item = item_list[choice-1]
    val = input(f"How many {item}{'s' if item[-1] != 's' else ''} to gain: ")
    if not isValidInt(val):
        print("That is not a number")
        return
    if val == "0":
        return
    add_item(item, int(val))
    save()
    enter()

def add_item(item: str, val: int):
    if val == 0:
        return
    if item in data.inventory:
        data.inventory[item] += val
    else:
        data.inventory[item] = val
    print(f"{val} {item}{'s' if item[-1] != 's' and val > 1 else ''} added to inventory.")
    if item == "Fortified Weapon":
        data.attack += val
        print(f"Attack increased by {val}.")
    if item == "Sharpened Weapon":
        data.damage += val
        print(f"Damage increased by {val}.")

def useItem():
    avoid_item_list = special_items
    sortItems()
    item_list, count = printMenuFromList(data.inventory, avoid_item_list)
    choice = getValidChoice("Which item to consume: ", count)
    if choice == 0:
        return
    item = item_list[choice-1]
    val = input(f"How many {item}{'s' if item[-1] != 's' else ''} to consume (up to {data.inventory[item]}): ")
    if not isValidInt(val, data.inventory[item]):
        return
    val = int(val)
    if val == 0:
        return
    data.inventory[item] -= val
    print(f"Used ", end="")
    if data.inventory[item] <= 0:
        del data.inventory[item]
        print(f"last {item}.", end="")
    else:
        print(f"{val} {item}{'s' if item[-1] != 's' and val > 1 else ''}.", end="")
    if item == "Fortified Weapon":
        data.attack -= val
        print(f"Attack decreased by {val}.")
    if item == "Sharpened Weapon":
        data.damage -= val
        print(f"Damage decreased by {val}.")
    print()
    save()

def sortItems():
    inv_dict = dict()
    for item in data.item_dict:
        if item in data.inventory:
            inv_dict[item] = data.inventory[item]
    data.inventory = inv_dict

def printItems():
    sortItems()
    print("\n--Inventory--")
    for i in data.inventory:
        print(f"{data.inventory[i]}x {i}:\t", end="")
        if len(i) <= 10:
            print("\t", end="")
        print(f"{data.item_dict[i][0]}")

def find_backpack_item():
    item_list = []
    year = data.year
    if not year:
        year = getYear()
    if not checkValidYear(year):
        return
    if year == 2024:
        item_list = ["Meal Ration", "Dragon's Fire (S)", "Combat Tonic (S)", "Warding Ointment", "Brawnberry", 
                     "Nimblecap", "Stoutseed", "Foresight Flower", "Sageleaf", "Galmour Stone"]
    elif year == 2026:
        item_list = ["NightShade", "Cryptweed", "Blightroot", "Wolfsbane", "Bonedust", "Moonmoss"]
    else:
        print("No backpack items available for that year.")
        enter()
        return
    item = random.choice(item_list)
    add_item(item, 1)