import crewmates
import data
from load_save_data import load, save
import party
from util import checkValidYear, getBool, getValidChoice, getYear, printMenuFromList

def followersMenu():
    # TODO: Allow for predetermined year
    year = data.year
    if not year:
        year = getYear()
    year = int(year)
    if not checkValidYear(year):
        return
    if year == 2021 or year == 2022:
        followersMenu2021(year)
    elif year == 2023:
        # crewmates
        crewmates.crewmateMenu()
    elif year in [2024, 2026]:
        # party members
        party.partyMenu()
        
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
    offers, count = printMenuFromList(data.all_followers[str(year)], follower_names, printOneFollower)
    choice = getValidChoice("Selection: ", count)
    if choice == 0:
        return
    f = offers[choice-1]
    if f[0] == "Young Demon":
        if data.virtue > 5:
            print("The Young Demon refuses to join you because your Virtue is too high.")
            return
    data.followers.append(f)

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
        skill, suits, val = skill1.split("/")
        print(f"      {skill}: {suits} >= {val}")
        if skill2:
            skill, suits, val = skill2.split("/")
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

if __name__ == "__main__":
    load()
    followersMenu2021(2021)
    save()