import data

path = "data/"
character = "character.txt"

# TODO: Cbaracter file selection.

def load():
    with open(path + character, "r") as f:
        """Load all player data from the character save file into the data module."""
        data.name = f.readline().strip()
        data.year = int(f.readline().split(":")[1].strip())
        data.level = int(f.readline().split(":")[1].strip())
        if not data.year or data.year in [2021, 2022, 2023, 2024]:
            data.virtue = int(f.readline().split(":")[1].strip())
        if not data.year or data.year == 2026:
            data.notoriety = int(f.readline().split(":")[1].strip())
            data.minions = int(f.readline().split(":")[1].strip())
        data.strength = int(f.readline().split(":")[1].strip())
        data.dexterity = int(f.readline().split(":")[1].strip())
        data.constitution = int(f.readline().split(":")[1].strip())
        data.intellect = int(f.readline().split(":")[1].strip())
        data.wisdom = int(f.readline().split(":")[1].strip())
        data.charisma = int(f.readline().split(":")[1].strip())
        data.hp = int(f.readline().split(":")[1].strip())
        data.max_hp = int(f.readline().split(":")[1].strip())
        data.defense = int(f.readline().split(":")[1].strip())
        data.attack = int(f.readline().split(":")[1].strip())
        dmg_line = f.readline().strip()
        data.damage_step = int(dmg_line.split(":")[1].strip().split("(")[0])
        data.damage = int(dmg_line.split(":")[1].strip().split("+")[-1])
        if not data.year or data.year in [2021, 2022, 2026]:
            data.gold = int(f.readline().split(":")[1].strip())
        if not data.year or data.year in [2023]:
            data.credits = int(f.readline().split(":")[1].strip())
        if not data.year or data.year in [2024]:
            data.amber = int(f.readline().split(":")[1].strip())
        data.boon = int(f.readline().split(":")[1].strip())

        line = readline(f) # clear blank lines and
        if line.startswith("-"): #step past "-Abilities-"
            line = readline(f)
        while goodline(line):
            data.abilities.append(line)
            line = readline(f)

        line = readline(f) #step past "-Inventory-"
        while goodline(line):
            count, item_name = line.split("x ")
            if int(count) > 0:
                if item_name in data.inventory:
                    data.inventory[item_name] += int(count)
                else:
                    data.inventory[item_name] = int(count)
            line = readline(f)
        
        line = readline(f) #step past "-Equipment-"
        while goodline(line):
            l = parseListLine(line)
            data.equipment.append(l)
            line = readline(f)

        line = readline(f) #step past "--Unequipped--"
        while goodline(line):
            l = parseListLine(line)
            data.unequipped.append(l)
            line = readline(f)
        
        if not data.year or data.year in [2021, 2022]:
            line = readline(f) #step past "-Followers-"
            while goodline(line):
                l = parseListLine(line)
                data.followers.append(l)
                line = readline(f)
        
        if not data.year or data.year == 2023:
            line = readline(f) #step past -Ship Stats-
            while goodline(line):
                attr, val = line.split(":")
                setattr(data, attr.strip().lower(), int(val.strip()))
                line = readline(f)

            line = readline(f) #step past -Ship Compartments-
            while goodline(line):
                compartment, l = line.split(":")
                chp, max_chp, upgrade, crewmate = l.strip().split("/")
                upgrade = parseListLine(upgrade)
                crewmate = parseListLine(crewmate)
                data.ship[compartment] = [int(chp.strip()), int(max_chp.strip()), upgrade, crewmate]
                line = readline(f)

            line = readline(f) #step past --Upgrades Reserve--
            while goodline(line):
                l = parseListLine(line)
                data.unequipped_ship_upgrades.append(l)
                line = readline(f)
           
            line = readline(f) #step past --Crewmates Reserve--
            while goodline(line):
                l = parseListLine(line)
                data.crew_reserve.append(l)
                line = readline(f)

        if not data.year or data.year in [2024, 2026]:
            pm_count = 0
            b_count = 0
            line = readline(f) #step past -Party-
            while goodline(line):
                slot, member = line.split(":")
                if slot.lower().startswith("slot"):
                    pm_count += 1
                elif slot.lower().startswith("bug"):
                    b_count += 1
                member = member.strip()
                if member != "None":
                    member = parseListLine(member)
                    if member[3]:
                        data.party.append(member)
                    else:
                        data.bugs.append(member)
                line = readline(f)

            data.party_limit = max(5, pm_count)
            data.bugs_limit = max(5, b_count)

            line = readline(f) #step past -Party Reserve-
            while goodline(line):
                l = parseListLine(line)
                data.party_reserve.append(l)
                line = readline(f)
        
        
        line = readline(f) #step past -Notes-
        while goodline(line):
            data.notes.append(line)
            line = readline(f)

    loadItemsFile()
    loadEquipmentFile()
    loadFollowersFile()
    loadSkillsFile()
    loadShipUpgradesFile()

def readline(f):
    """Read and return the next non-empty, stripped line from the file or None if EOF."""
    while True:  # Keep reading until a non-blank line or EOF
        line = f.readline()
        if line == "":  # Detect EOF immediately
            print("***EOF***")
            return None
        line = line.strip()  # Remove whitespace
        if line:  # If it's not empty after stripping, return it
            return line

def parseListLine(line):
    """Convert a semicolon-separated line into a list of stripped values."""
    l = line.split(";")
    for i in range(len(l)):
        l[i] = l[i].strip()
    return l

def goodline(line):
    """Return True if line is not None and doesn't start with a dash."""
    return line and not line.startswith("-")

def loadItemsFile():
    with open(path + "items.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            item, l = line.split(": ")
            desc, years = l.split("/")
            data.item_dict[item] = [desc, years]

def loadEquipmentFile():
    with open(path + "equipment.txt", "r") as f:
        for line in f:
            l = line.strip()
            if l == "":
                continue
            l = l.split(",")
            for i in range(len(l)):
                l[i] = l[i].strip()
            year = l[1]
            slot = l[2]
            if year == "2021":
                slot = "all"
            l.remove(year)
            if not year in data.all_equipment:
                data.all_equipment[year] = {}
            if not slot in data.all_equipment[year]:
                data.all_equipment[year][slot] = []
            data.all_equipment[year][slot].append(l)

def loadFollowersFile():
    with open(path + "followers.csv", "r") as f:
        for line in f:
            l = line.strip().split(";")
            if l[0].strip() == "name":
                continue
            print(l)
            year = l[1].strip()
            if year not in data.all_followers:
                data.all_followers[year] = []
            data.all_followers[year].append(l)

def loadSkillsFile():
    with open(path + "skills.csv", "r") as f:
        for line in f:
            sname, cost, use, desc, yearsUsed = line.split(";")
            yearsUsed = yearsUsed.split(", ")
            if sname.strip() == "" or sname.strip() == "name":
                continue
            data.skills_dict[sname] = [desc, cost, use, yearsUsed]

def loadShipUpgradesFile():
    with open(path + "ship upgrades.csv", "r") as f:
        for line in f:
            upgrade, comp, bonus = line.split(";")
            if upgrade.strip() == "" or upgrade.strip() == "Upgrade Name":
                continue
            if comp not in data.all_ship_upgrades:
                data.all_ship_upgrades[comp] = []
            data.all_ship_upgrades[comp].append([upgrade.strip(), comp.strip(), bonus.strip()])

def save():
    with open(path + character, "w") as f:
        f.write(f"{data.name}\n")
        f.write(f"Year: {data.year}\n")
        f.write(f"Level: {data.level}\n")
        if not data.year or data.year in [2021, 2022, 2023, 2024]:
            f.write(f"Virtue: {data.virtue}\n")
        if not data.year or data.year in [2026]:
            f.write(f"Notoriety: {data.notoriety}\n")
            f.write(f"Minions: {data.minions}\n")
        f.write(f"Str: {data.strength}\n")
        f.write(f"Dex: {data.dexterity}\n")
        f.write(f"Con: {data.constitution}\n")
        f.write(f"Int: {data.intellect}\n")
        f.write(f"Wis: {data.wisdom}\n")
        f.write(f"Cha: {data.charisma}\n")
        f.write(f"HP: {data.hp}\n")
        f.write(f"Max HP: {data.max_hp}\n")
        f.write(f"Def: {data.defense}\n")
        f.write(f"Atk: {data.attack}\n")
        f.write(f"Dmg: {data.damage_step}({data.damage_chart[data.damage_step]})+{data.damage}\n")
        if not data.year or data.year in [2021, 2022, 2026]:
            f.write(f"Gold: {data.gold}\n")
        if not data.year or data.year in [2023]:
            f.write(f"Credits: {data.credits}\n")
        if not data.year or data.year in [2024]:
            f.write(f"Amber: {data.amber}\n")
        f.write(f"Boon: {data.boon}\n")
        f.write("\n")
        f.write("-Abilities-\n")
        for a in data.abilities:
            f.write(f"{a}\n")
        f.write("\n")
        f.write("-Inventory-\n")
        for i in data.inventory:
            f.write(f"{data.inventory[i]}x {i}\n")
        f.write("\n-Equipment-\n")
        for e in data.equipment:
            line = prepListLine(e)
            f.write(f"{line}\n")
        f.write("--Unequipped--\n")
        for u in data.unequipped:
            line = prepListLine(u)
            f.write(f"{line}\n")
        f.write("\n")
        if not data.year or data.year in [2021, 2022]:
            f.write("-Followers-\n")
            for follower in data.followers:
                line = prepListLine(follower)
                f.write(f"{line}\n")
            f.write("\n")
        if not data.year or data.year in [2023]:
            f.write("-Ship Stats-\n")
            f.write(f"Aim: {data.aim}\n")
            f.write(f"Evasion: {data.evasion}\n")
            f.write(f"Shield: {data.shield}\n")
            f.write("\n-Ship Compartments-\n")
            for compartment in data.ship:
                chp = data.ship[compartment][0]
                max_chp = data.ship[compartment][1]
                upgrade = data.ship[compartment][2]
                upgrade = prepListLine(upgrade)
                crewmate = data.ship[compartment][3]
                crewmate = prepListLine(crewmate)
                f.write(f"{compartment}: {chp}/{max_chp}/{upgrade}/{crewmate}\n")
            f.write("\n--Upgrades Reserve--\n")
            for u in data.unequipped_ship_upgrades:
                line = prepListLine(u)
                f.write(f"{line}\n")
            f.write("\n--Crewmate Reserve--\n")
            for u in data.crew_reserve:
                line = prepListLine(u)
                f.write(f"{line}\n")
                f.write("\n")
        if not data.year or data.year in [2024, 2026]:
            f.write("-Party-\n")
            i = 1
            for member in data.party:
                m = prepListLine(member)
                f.write(f"Slot {i}: {m}\n")
                i += 1
            for x in range(i, data.party_limit + 1):
                f.write(f"Slot {x}: None\n")
            i = 1
            for bug in data.bugs:
                b = prepListLine(bug)
                f.write(f"Bug {i}: {b}\n")
                i += 1
            for x in range(i, data.bugs_limit + 1):
                f.write(f"Bug {x}: None\n")
            f.write("\n-Party Reserve-\n")
            for follower in data.party_reserve:
                line = prepListLine(follower)
                f.write(f"{line}\n")
        f.write("\n-Notes-\n")
        for note in data.notes:
            f.write(f"{note}\n")
        f.write("\n-End-")

def prepListLine(list):
    if list == "None":
        return "None"
    line = str(list[0])
    for i in range(1, len(list)):
        line += "; " + str(list[i])
    return line

if __name__ == "__main__":
    load()
    save()

