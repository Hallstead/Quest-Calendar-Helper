# TODO: make abilities track uses per page and per rest

import data
from util import enter, getBool, getValidChoice
from load_save_data import save
from items import special_items


def printAbilities():
    print("\n--Abilities--")
    for a in data.abilities:
        print(a)
    if set(special_items) & set(data.inventory.keys()):
        print("\n--Abilities from Special Items--")
        for item in special_items:
            if item in data.inventory:
                if item == "Fortified Weapon":
                    print(f"Fortified Weapon{"s" if data.inventory[item] > 1 else ""}: Attack +{data.inventory[item]}")
                elif item == "Sharpened Weapon":
                    print(f"Sharpened Weapon{"s" if data.inventory[item] > 1 else ""}: Damage +{data.inventory[item]}")
                else:
                    print(f"{item}: {data.item_dict[item][0]}")
    if len(data.followers) > 0:
        print("\n--Abilities from Followers--")
        for f in data.followers:
            skill1 = f[2]
            skill2 = f[3]
            print(f"{skill1}{': ' + data.skills_dict[skill1][0] if skill1 in data.skills_dict else ''}")
            if skill2:
                print(f"{skill2}{': ' + data.skills_dict[skill2][0] if skill2 in data.skills_dict else ''}")
    
    if any(data.ship[comp][3] != ["None"] for comp in data.ship):
        print("\n--Abilities from Crewmates--")
        for comp in data.ship:
            crewmate = data.ship[comp][3]
            if crewmate != ["None"]:
                skill = crewmate[3]
                print(f"{skill}{': ' + data.skills_dict[skill][0] if skill in data.skills_dict else ''}")

    if len(data.party) > 0 or len(data.bugs) > 0:
        print("\n--Abilities from Party Members and Bugs--")
        for pm in data.party:
            skill1 = pm[2]
            skill2 = pm[3]
            skill, suits, val = skill1.split("/")
            print(f"{skill} ({suits} >= {val}){': ' + data.skills_dict[skill][0] if skill in data.skills_dict else ''}")
            if skill2: # party members should all have a second skill, but checking just to be sure.
                skill, suits, val = skill2.split("/")
                print(f"{skill} ({suits} >= {val}){': ' + data.skills_dict[skill][0] if skill in data.skills_dict else ''}")
        for pm in data.bugs:
            skill1 = pm[2]
            skill2 = pm[3]
            skill, suits, val = skill1.split("/")
            print(f"{skill} ({suits} >= {val}){': ' + data.skills_dict[skill][0] if skill in data.skills_dict else ''}")
            if skill2: # bugs should all not have a second skill, but checking just in case.
                skill, suits, val = skill2.split("/")
                print(f"{skill} ({suits} >= {val}){': ' + data.skills_dict[skill][0] if skill in data.skills_dict else ''}")
            
