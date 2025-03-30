import data
from equipment import equipmentMenu, printEquipment
import followers
from hp import hpMenu
from items import itemMenu, printItems
from load_save_data import load, save
from ship import printShip, shipMenu
from util import enter, getBool, getValidChoice

def printAbilities():
    print("\n--Abilities--")
    for a in data.abilities:
        print(a)
    print("\n--Abilities from Cohorts--")
    for f in data.followers:
        skill1 = f[2]
        skill2 = f[3]
        print(f"{skill1}: {data.skills_dict[skill1][0] if skill1 in data.skills_dict else ''}")
        if skill2:
            print(f"{skill2}: {data.skills_dict[skill2][0] if skill2 in data.skills_dict else ''}")


def printTraits():
    print("\nStr\tDex\tCon\tInt\tWis\tCha")
    if (data.strength >= 0):
        print(f" ", end="")
    print(data.strength, end="\t")
    if (data.dexterity >= 0):
        print(f" ", end="")
    print(data.dexterity, end="\t")
    if (data.constitution >= 0):
        print(f" ", end="")
    print(data.constitution, end="\t")
    if (data.intellect >= 0):
        print(f" ", end="")
    print(data.intellect, end="\t")
    if (data.wisdom >= 0):
        print(f" ", end="")
    print(data.wisdom, end="\t")
    if (data.charisma >= 0):
        print(f" ", end="")
    print(data.charisma)

def printStats():
    print("\nHP\tAttack\tDefense\tDamage")
    print(f"{data.hp}/{data.max_hp}\t+{data.attack}\t+{data.defense}\t{data.damage_chart[data.damage_step]}{' + ' + str(data.damage) if data.damage else ''}")

def printMoney():
    total = data.gold + data.credits + data.amber
    print("\nTotal Currency:", total)
    print("  Gold:", data.gold)
    print("  Credits:", data.credits)
    print("  Amber:", data.amber)

def printCharacterSheet():
    print()
    print(data.name)
    print("Level:", data.level)
    print("Virtue:", data.virtue)
    printTraits()
    printStats()
    printMoney()
    print("\nBoon:", data.boon)
    printAbilities()
    printItems()
    printEquipment()
    enter()
    followers.printFollowers()
    printShip()
    # printParty()
    # printFollowersReserve()

def boonMenu():
    print("\n--Boon Menu--")
    print(f"Boon: {data.boon}")
    print("Would you like to ", end="")
    if data.boon:
        print("spend your", end="")
    else:
        print("gain a", end="")
    choice = input(" boon? (y/n): ")
    if choice.lower() == "y":
        if data.boon:
            data.boon -= 1
            print("Spending Boon.")
        else: 
            data.boon += 1
            print("You got a Boon.")
        save()

def moneyMenu():
    print("\n--Money Menu--")
    print("1. View Currency")
    print("2. Gold")
    print("3. Credits")
    print("4. Amber")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 4)
    if choice == 1:
        printMoney()
        enter()
    elif choice == 2:
        currency = "Gold"
    elif choice == 3:
        currency = "Credits"
    elif choice == 4:
        currency = "Amber"
    elif choice == 0:
        return
    if choice != 1:
        addMoney(currency)
    moneyMenu()
        
def addMoney(currency):
    print(f"\n1. Add {currency}")
    print(f"2. Lose {currency}")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 2)
    if choice == 0:
        return
    try:
        val = int(input(f"How {'many' if currency == 'Credits' else 'much'} {currency} to {'add' if choice == 1 else 'lose'}: "))
    except:
        print("\nThat is not a number.")
        enter()
        return
    if val != 0:
        print(f"You {'added' if choice == 1 else 'lost'} {val} {currency}.")
        if choice == 2:
            val = -val
        if currency == "Gold":
            data.gold += val
        if currency == "Credits":
            data.credits += val
        if currency == "Amber":
            data.amber += val
        save()
        enter()

def restMenu():
    response = getBool("Would you like to take a Rest?")
    if response:
        rest()
           
def rest():
    data.hp = data.max_hp
    
    # TODO: check abilities for per Rest and uncheck them
    
    # Leave on Rest Followers
    followers.loseAtRestFollowers()
            
def virtueMenu():
    print("\n--Virtue Menu--")
    print(f"Current Virtue: {data.virtue}")
    print("1. +1 Virtue")
    print("2. -1 Virtue")
    print("0. Go Back")
    choice = getValidChoice("Selection: ", 2)
    if choice == 1:
        modifyVirtue(1)
    elif choice == 2:
        modifyVirtue(-1)
    else:
        return
    virtueMenu()

def modifyVirtue(val):
    data.virtue += val
    if data.virtue > 10:
        data.virtue = 10
    if data.virtue < -10:
        data.virtue = -10
    followers.loseAtVirtueFollowers()
        
def menu():
    while(True):
        print("\n--Main Menu--")
        print("1. View Character Sheet")
        print("2. Modify HP")
        print("3. Items")
        print("4. Abilities")
        print("5. Money")
        print("6. Boon")
        print("7. Equipment")
        print("8. Followers")
        print("9. Ship")
        print("10. Rest")
        print("11. Virtue")
        print("12. Save")
        print("0. Close")
        choice = getValidChoice("Selection: ", 12)
        if choice == 1: # View Character Sheet
            printCharacterSheet()
        elif choice == 2: # Modify HP
            hpMenu()
        elif choice == 3: # Items
            itemMenu()
        elif choice == 4: # Abilities
            printAbilities()
        elif choice == 5: # Money
            moneyMenu()
        elif choice == 6: # Boon
            boonMenu()
        elif choice == 7: # Equipment
            equipmentMenu()
        elif choice == 8: # Followers
            followers.followersMenu()
        elif choice == 9: # Ship
            shipMenu()
        elif choice == 10: # Rest
            restMenu()
        elif choice == 11: # Virtue
            virtueMenu()
        elif choice == 12: # Save
            save()
        elif choice == 0: # Close
            break

if __name__ == "__main__":
    load()
    menu()
    
 
