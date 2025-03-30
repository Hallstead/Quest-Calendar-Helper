import data
import followers
from util import getValidChoice

def hpMenu():
    print("\n--HP Menu--")
    print(f"Current HP: {data.hp}/{data.max_hp}")
    print("1. Restore Health")
    print("2. Take Damage")
    bodyGuard = False
    limit = 2
    for f in data.followers:
        if f[0] == "Body Guard":
            bodyGuard =  True
            break
    if bodyGuard:
        print("3. Body Guard Takes Damage")
        limit = 3
    print("0. Go Back")
    choice = getValidChoice("Selection: ", limit)
    val = 0
    try:
        if choice == 1:
            val = int(input("Health to restore: "))
        elif choice == 2:
            val = -int(input("Damage taken: "))
        elif choice == 3:
            val = int(input("Damage taken by the Body Guard: "))
            followers.bodyGuardTakesDamage(val)
            val = 0
        elif choice == 0:
            return
        if val:
            modifyHP(val)
        hpMenu()
    except:
        print("That is not a number.")

def modifyHP(val):
    data.hp += val
    if data.hp > data.max_hp:
        data.hp = data.max_hp
    if data.hp <= 0:
        data.hp = 0
    print(f"New HP: {data.hp}/{data.max_hp}")
    if data.hp == 0:
        # TODO: check for Revive abilities
        print("You have died!")
        followers.loseAtDeathFollowers()
        