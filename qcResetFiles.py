def characterSheet():
    with open("Felix Factotum 2025.txt", "w") as f:
        f.write("""Felix Factotum
Level: 2
Virtue: 1
Str: 0
Dex: 3
Con: -4
Int: 7
Wis: -2
Cha: 0
HP: 18
Max HP: 21
Def: 2
Atk: 7
Dmg: 5(2d8)+0
Gold: 57
Credits: 12
Amber: 50
Boon: 1

-Abilities-
Investigator: +2 on checks to search for things.
Reroll: Once per page, reroll a die and take the new result.
Lucky: When you roll a 1 on a d20 roll, reroll the die and take the new result.
Inspiration 2: You have two Inspiration Points to power your abilities.
Combat Surge: Use one Inspiration Point. Add 1d4 to a single Attack or Damage roll.
Cunning Knowledge: Use one Inspiration Point. Add 1d4 to a single trait roll.
Cunning Insight: Use two Inspiration Points. Add your Intellect modifier to a d20 roll that does not include Intellect.

-Inventory-
2x Health Potion (1d4)
1x Antidote
3x Combat Tonic (S)
1x Solar Grenade
3x Warding Ointment
1x Nimblecap
1x Foresight Flower

-Equipment-
Plasma Sword, Weapon, +1 Attack, +2 Defense, +1 Damage_Step
Spinal Amplifier, Upgrade, +1 Dexterity, +1 Attack
Blossom Wand, Item, +1 Intellect, +1 Attack
--Unequipped--

-Followers-
""")

def items():
    with open("items.txt", "w") as f:
        f.write("""Health Potion (1d4): Consumed on use. Restores d4 health. Can't be used in Combat./2021, 2024
Health Potion (2d4): Consumed on use. Restores 2d4 health. Can't be used in Combat./2022
Med Kit: Consumed on use. Restores 2d4 health. Can't be used in Combat./2023
Greater Health Potion (d10): Consumed on use. Restores d10 health. Can't be used in Combat./2021
Greater Health Potion (2d8): Consumed on use. Restores 2d8 health. Can't be used in Combat./2022
Meal Rations: Consumed on use. Needed if you can't find food and water./2021, 2022, 2023, 2024
Honey: Consumed on use. Use as 1 Health Potion or d6 Meal Rations./2024
Campfire: Consumed on use. Take a Rest./2024
Ship Parts: Consumed on use. Restores 1 point of Integrity to any ship compartment./2023
Antidote: Consumed on use. Removes the "Poisoned" and "Infected" conditions/2022, 2023, 2024
Cleansing Crystal: Consumed on use. Removes the "Cursed" condition./2024
Holy Water: Consumed on use. Removes the "Cursed" condition./2022
Repair Kit: Consumed on use. Removes the "Malfunction" condition./2023
Bandages: Consumed on use. Removes an Injury inflicted from death./2021, 2022
Ointment: Consumed on use. Removes a single wound inflicted from death./2021, 2022
Phoenix Tears: Consumed on use. Removes a single wound inflicted from death./2024
Potion of Clarity: Consumed on use. Removes a single Trauma inflicted from death./2021, 2022
Wound Sealant: Consumed on use. Removes Injuries inflicted from death./2023
Combat Tonic (S): Consumed on use. Add d4 to a single Attack roll./2021, 2024
Combat Tonic (All): Consumed on use. Add d4 to all Attack rolls on a page./2022, 2023
Dragon's Fire (S): Consumed on use. Add d4 to a single Damage roll./2021, 2024
Dragon's Fire (All): Consumed on use. Add d4 to a all Damage rolls for the page./2022
Solar Grenade: Consumed on use. Add d4 to all Damage rolls on a page./2023
Warding Ointment: Consumed on use. Add d4 to a single Defense roll./2024
Shield Battery: Consumed on use. Add +2 Defense for the page./2023
Brawnberry: Consumed on use. Add d4 to Strength on a single roll./2024
Strengthener Rx: Consumed on use. Add d4 to Strength for the page./2023
Potion of Giant Strength: Consumed on use. Add d6 to Strength for the page./2021, 2022
Nimblecap: Consumed on use. Add d4 to Dexterity on a single roll./2024
Adrenaline Rx: Consumed on use. Add d4 to Dexterity for the page./2023
Potion of the Wind: Consumed on use. Add d6 to Dexterity for the page./2021, 2022
Stoutseed: Consumed on use. Add d4 to Constitution on a single roll./2024
Fortifier Rx: Consumed on use. Add d4 to Constitution for the page./2023
Potion of Fortitude: Consumed on use. Add d6 to Constitution for the page./2021, 2022
Foresight Flower: Consumed on use. Add d4 to Intellect on a single roll./2024
Stimulant Rx: Consumed on use. Add d4 to Intellect for the page./2023
Potion of the Gods: Consumed on use. Add d6 to Intellect for the page./2021, 2022
Sageleaf: Consumed on use. Add d4 to Wisdom on a single roll./2024
IntulSense Rx: Consumed on use. Add d4 to Wisdom for the page./2023
Draught of Enrichment: Consumed on use. Add d6 to Wisdom for the page./2021, 2022
Glamour Stone: Consumed on use. Add d4 to Charisma on a single roll./2024
Relaxant Rx: Consumed on use. Add d4 to Charisma for the page./2023
Aged Wine: Consumed on use. Add d6 to Charisma for the page./2021, 2022
Physical Elixir: Consumed on use. Add a d8 to all Strength, Dexterity, and Constitution for the page./2021
Mental Draught: Consumed on use. Add a d8 to all Intellect, Wisdom, and Charisma for the page./2021
Map & Compass: Add +2 to Wisdom rolls while traveling. Can't have more than one./2021, 2022
Lockpicking Tools: Add +2 to rolls when picking locks. Can't have more than one./2021, 2022
Sharpened Weapon: Add +1 to all Damage rolls. Max of +3./2021, 2022
Fortified Weapon: Add +1 to all Attack rolls. Max of +3./2021, 2022
Spellbook: Gain 1 extra spell point./2021
Mule: Add +2 to Wisdom rolls while traveling on land. Can't have more than one mount./2021, 2022
Horse: Add +4 to Wisdom rolls while traveling on land. Can't have more than one mount./2021, 2022
Seaquine: Add +4 to Wisdom rolls while traveling on land or at sea. Can't have more than one mount./2022
Row Boat: Add +2 to Survival rolls while traveling on the river. Mount required. Can't have more than one boat./2021
Magical Boat: Add +4 to Survival rolls while traveling on the river. No Mount required. Can't have more than one boat./2021
""")

def equipment():
    with open("equipment.txt", "w") as f:
        f.write("""Shield of Valor, 2021, Shield, +1 Armor, Can sell for 25 gold
Ring of Mind, 2021, Ring, +1 Intellect, +1 Wisdom, Can sell for 30 gold
Wand of Pain, 2021, Item, Use once per Rest. Use in combat to add a d10 to a Damage roll. Ignores all armor to hit automatically., Can sell for 35 gold
Iron Belt of Fortitude, 2021, Belt, +1 Strength, Constitution, Can sell for 35 gold
Cloak of Thieves, 2021, Cloak, +1 Dexterity, +1 Charisma, Can sell for 35 gold
Collar of Creation, 2021, Necklace, +5 Health, Can sell for 35 gold
The Dragon Staff, 2021, Key Item, Use once per Rest to add d4 to all Damage rolls for the page. Can't be sold or sacrificed upon death.
Circlet of Potential, 2022, Helmet, +1 Strength, +1 Dexterity, +1 Constitution, +1 Intellect, +1 Wisdom, +1 Charisma, Can sell for 50 gold

Champion Shield, 2022, Shield, +1 Dexterity, +1 Defense
Necklace of Luck, 2022, Necklace, +1 Dexterity, +1 Attack
Belt of the Champ, 2022, Belt, +1 Dexterity, +1 Health
World Watcher's Staff, 2022, Key Item, Can be used in combat to Banish an enemy to its home realm. May contain other secrets. Can't be sold or sacrificed upon death.
Flame Shield, 2022, Shield, +1 Strength, +1 Defense
Ring of Fire, 2022, Ring, +1 Strength, +1 Health
Fire Gloves, 2022, Gloves, +1 Strength, +1 Damage
Helm of Nature, 2022, Helmet, +1 Wisdom, +1 Defense
Thorn Bracers, 2022, Bracers, +1 Wisdom, +1 Attack
Belt of the Forest, 2022, Belt, +1 Wisdom, +1 Health
Water Ring, 2022, Ring, +1 Charisma, +1 Health
Cloak of Currents, 2022, Cloak, +1 Charisma, +1 Defense
Helm of the Deep, 2022, Helmet, +1 Charisma, +1 Defense
Air Necklace, 2022, Necklace, +1 Intellect, +1 Health
Gloves of Mist, 2022, Gloves, +1 Intellect, +1 Damage
Boots of Flight, 2022, Boots, +1 Intellect, +1 Attack
Shadow Weapon, 2022, Weapon, +1 Constitution, +1 Damage
Cloak of Shadows, 2022, Cloak, +1 Constitution, +1 Defense
Bracers of the Night, 2022, Bracers, +1 Constitution, +1 Attack
Divine Helmet, 2022, Helmet, +2 Defense
Necklace of Balance, 2022, Necklace, +1 Defense, +1 Health
Gloves of Light, 2022, Gloves, +1 Defense, +1 Damage
Ring of Ice, 2022, Ring, +1 Damage, +1 Health
Winter Shield, 2022, Shield, +1 Damage, +1 Defense
Ice Boots, 2022, Boots, +1 Damage, +1 Attack
Machine Bracers, 2022, Bracers, +2 Attack
Cog Weapon, 2022, Weapon, +1 Attack, +1 Damage
Belt of Many Gears, 2022, Belt, +1 Attack, +1 Health
Soul Stealer Weapon, 2022, Weapon, +1 Health, +1 Damage
Cloak of Evil, 2022, Cloak, 2022, +1 Health, +1 Defense
Boots of the Dead, 2022, Boots, +1 Health, +1 Attack
Sundial, 2023, Upgrade, +1 Attack, +1 Damage, +1 Defense, +1 Health

Kinetic Shield, 2023, Shield, +1 Dexterity, +1 Defense
Kinetic Harness, 2023, Belt, +1 Dexterity, +2 Health
Spinal Amplifier, 2023, Upgrade, +1 Dexterity, +1 Attack
Photons Comms Link, 2023, Comms, +1 Intellect, +2 Health
Photon Gloves, 2023, Gloves, +1 Intellect, +1 Damage
Photon Shield, 2023, Shield, +1 Intellect, +1 Defense
Solar Visor, 2023, Helmet, +1 Wisdom, +1 Defense
Solar Belt Clips, 2023, Belt, +1 Wisdom, +2 Health
Solar Energy Pack, 2023, Pack, +1 Wisdom, +1 Attack
Sonic Comms Link, 2023, Comms, +1 Charisma, +2 Health
Sonic Helmet, 2023, Helmet, +1 Charisma, +1 Defense
Sonic Armor Plate, 2023, Armor, +1 Charisma, +1 Defense
Pulse Gauntlet, 2023, Gloves, +1 Strength, +1 Damage
Pulse Pads, 2023, Boots, +1 Strength, +1 Attack
Pulse Absorber, 2023, Upgrade, +1 Strength, +2 Health
Plasma Vest, 2023, Armor, +1 Constitution, +1 Defense
Plasma Slicer, 2023, Weapon, +1 Constitution, +1 Damage
Plasma Pack, 2023, Pack, +1 Constitution, +1 Attack
Cryo Visor, 2023, Helmet, +2 Defense
Cryo Mitts, 2023, Gloves, +1 Defense, +1 Damage
Neural Apparatus, 2023, Upgrade, +1 Defense, +2 Health
Laser Guard, 2023, Shield, +1 Damage, +1 Defense
Laser Boots, 2023, Boots, +1 Damage, +1 Attack
Laser Relay, 2023, Comms, +1 Damage, +2 Health
Jet Force Axe, 2023, Weapon, +1 Damage, +2 Health
Jet Blast Belt, 2023, Belt, +4 Health
Jet Pack, 2023, Pack, +1 Attack, +2 Health
Arc Deflector, 2023, Armor, +1 Attack, +1 Defense
Arc Blade, 2023, Weapon, +1 Attack, +1 Damage
Arc Boots, 2023, Boots, +2 Attack
Mysterious Canister, 2024, Item, +1 Strength, +1 Dexterity, +1 Constitution, +1 Intellect, +1 Wisdom, +1 Charisma, +X Health

Royal Bloom Shield, 2024, Shield, +1 Intellect, +1 Defense
Alchemist Belt, 2024, Belt, +1 Intellect, +2 HP
Blossom Wand, 2024, Item, +1 Intellect, +1 Attack
Amethyst Choker, 2024, Necklace, +1 Dexterity, +1 Attack
Feather Bow, 2024, Weapon, +1 Dexterity, +1 Damage
Imperial Helm, 2024, Helmet, +1 Dexterity, +1 Defense
Bark Cap Armor, 2024, Armor, +1 Wisdom, +1 Defense
Cloak of Feathers, 2024, Cloak, +1 Wisdom, +1 Attack
Winged Ring, 2024, Ring, +1 Wisdom, +2 Health
Black Cap Helm, 2024, Helmet, +1 Charisma, +1 Defense
Twig Strapp Gloves, 2024, Gloves, +1 Charisma, +1 Damage
Shiitake Staff, 2024, Item, +1 Charisma, +2 Health
Claw Mace, 2024, Weapon, +1 Strength, +1 Damage
Pearl Stream Belt, 2024, Belt, +1 Strength, +2 Health
Opal Charm, 2024, Necklace, +1 Strength, +1 Attack
Amethyst Ring, 2024, Ring, +1 Constitution, +2 Health
Cedar Plate, 2024, Armor, +1 Constitution, +1 Defense
The Oak Cloak, 2024, Cloak, +1 Constitution, +1 Attack
Phoenix Belt, 2024, Belt, +1 Defense, +2 Health
Ruby Burst Shield, 2024, Shield, +2 Defense
Sun Ray Mittens, 2024, Gloves, +1 Defense, +1 Damage
Cloak of Webs, 2024, Cloak, +1 Damage, +1 Attack
Mask of Feathers, 2024, Helmet, +1 Damage, +1 Defense
The Fang, 2024, Weapon, +2 Damage
Creeping Vine Staff, 2024, Item, +2 Health, +1 Damage
Ring of Thorns, 2024, Ring, +4 Health
Green Grove Armor, 2024, Armor, +2 Health, +1 Defense
Combat Mits, 2024, Gloves, +1 Attack, +1 Damage
Bashing Shield, 2024, Shield, +1 Attack, +1 Defense
Potent Necklace, 2024, Necklace, +2 Attack
Seed of Life, 2025, Item, +1 Attack, +1 Damage, +1 Defense, +X Health
""")

def followers():
    with open("followers.csv", "w") as f:
        f.write("""name;year;skill1;skill2;condition
Travel Guide;2021;Danger Sense;Hunter;If you ever roll a 1 on a Survival roll (before bonuses), the Travel Guide leaves.
Burglers;2021;Locksmith;Stealthy;If your Health ever reaches zero, the Burglars take all your gold and leave.
Alchemist;2021;Alchemy;;If you ever buy a Health Potion elsewhere, the Alchemist leaves.
Minstrel;2021;Persuasive;Animal Tamer;If your Health ever reaches zero, the Minstrel leaves.
Arificer;2021;Student;Gadget;If you ever take a Rest without using the Artificer's Gadget Ability, the Artificer leaves.
Fairies;2021;Lucky;Command Fate;If you ever roll a 1 when using either of the Fairies' abilities, the Fairies leave.
Priestess;2021;Revive;;If your health drops to zero a second time before you Rest, the Priestess will leave.
Body Guard;2021;Guard;;Once the Guard takes a total of 30 damage, he leaves. The Body Guard can't heal.
Baby Dragon;2021;Baby Dragon;;The Baby Dragon requires 4 Meal Rations every time you take a Rest. If you cannot or do not feed it, it leaves.
;;;;
Thief;2022;Locksmith;Pickpocket;Upkeep: 5 gold
Warrior;2022;Athlete;Animal Tamer;Upkeep: 5 gold
Young Demon;2022;Intimidating;;If your Virtue ever goes above 5, the demon leaves.
Tracker;2022;Survivalist;Lucky;Upkeep: 10 gold
Raiders;2022;Stealthy;Danger Sense;Upkeep: 10 gold
Sentry;2022;Investigator;Intimidating;Upkeep: 10 gold
Sorceress;2022;Student;Revive;Upkeep: 10 gold
Bodyguard;2022;Shield;Athlete;Upkeep: 10 gold
Mage;2022;Danger Sense;Arcane Adept;Upkeep: 10 gold
;;;;
Zoologist;2023;+1 Integrity;Animal Tamer;
Convoy;2023;+1 Integrity;Survivalist;
SD-247;2023;+1 Integrity;Computers;
Detective;2023;+1 Integrity;Investigator;
Telepath;2023;+1 Integrity;Arcane Adept;
Analist;2023;+1 Integrity;Student;
Mechanic;2023;+1 Integrity;Engineering;
Scout Drone;2023;+1 Integrity;Stealthy;
Demolitionist;2023;+1 Integrity;Locksmith;
Merchant;2023;+1 Integrity;Persuasive;
Navigator;2023;+1 Integrity;Piloting;
Soldier;2023;+1 Integrity;Athlete;
Explorer;2023;+1 Integrity;Danger Sense;
;;;;
Party;;;;
March 1;;;;
March 20;;;;
April 16;;;;
June 15/16;;;;
July 18;;;;
September 24;;;;
October 26/27;;;;
November 16/17;;;;
Bugs;;;;
February 15;;;;
March 2/3;;;;
March 21;;;;
May 7;;;;
July 19;;;;
August 26;;;;
September 26;;;;
November 18;;;;
""")

def skills():
    with open("skills.csv", "w") as f:
        f.write("""name;cost;use;description;years
Animal Tamer;1;O;Add +2 to all rolls to train and handle animals.;2021, 2022, 2023
Arcane Adept;1;O;Add +2 to all rolls to handle and deal with magic.;2021, 2022, 2023, 2024
Athlete;1;O;Add +2 to all rolls to overcome physical and athletic hurdles.;2021, 2022, 2023, 2024
Bug Tamer;1;O;Add +2 to all rolls to train and handle bugs.;2024
Computers;1;O;Add +2 to all rolls to operate computer systems.;2023
Danger Sense;1;O;Add +2 to all rolls to avoid traps and surprise hazards.;2021, 2022, 2023, 2024
Engineering;1;O;Add +2 to all rolls to build and repair devices.;2023
Intimidating;1;O;Add +2 to all rolls to threaten and intimidate;2021, 2022, 2023, 2024
Investigator;1;O;Add +2 to all rolls to search and investigate;2021, 2022, 2023, 2024
Locksmith;1;O;Add +2 to all rolls to pick a lock.;2021, 2022, 2023, 2024
Persuasive;1;O;Add +2 to all rolls to persuade and convince.;2021, 2022, 2023, 2024
Piloting;1;O;Add +2 to all rolls to navigate and fly a ship.;2023
Stealthy;1;O;Add +2 to all rolls to sneak and remain hidden.;2021, 2022, 2023, 2024
Student;1;O;Add +2 to all rolls to recall history and knowledge.;2021, 2022, 2023, 2024
Survivalist;1;O;Add +2 to all rolls to endure long journeys.;2021, 2022, 2023, 2024
Lucky;1;B;Whenever you roll a 1 on any d20, reroll and take the new result. If the new result is also a 1, it must be kept.;2021, 2022, 2023, 2024
Hunter;;O;The Travel Guide always has 1 ration you can use (max of 1 per day).;2021
Alchemy;;O;Once per day, you can pay the Alchemist 5 gold for him to make you a Health Potion (restore d4 Health).;2021
Gadget;;B;Once per day, pay 2 gold to gain a +2 to any single die roll.;2021
Command Fate;;B;Once per Rest, reroll any single die roll once.;2021
Revive;1;B;Once per Rest, when your Health drops to zero, restore it to 25% of your max Health, rounded up.;2021, 2022
Guard;;B;The Body Guard can take damage in place of your hero.;2021
Shield;;B;Once per Page: Reduce total incoming damage by 3.;
;;;;
""")
        
def shipParts():
    with open("ship upgrades.txt", "w") as f:
        f.write("""Thusters, Engine Room, +10 Evasion
Sensors, Bridge, +5 Aim
Defectors, Weapons, +1 Shield
Greenhouse, Labs, +5 Evasion
Regen Pod, Crew Quarters, +5 Aim
Escape Pod, Cargo, +1 Integrity
Generator, Engine Room, +1 Integrity
Cannons, Weapons, +10 Aim
Teleporter, Cargo, +1 Shield
Machine Shop, Labs, +5 Aim
Bio Locks, Crew Quarters, +1 Integrity
Nav System, Bridge, +5 Evasion
Tractor Beam, Bridge, +1 Integrity
Homing Beacon, Weapons, +1 Integrity
Smuggler Bin, Cargo, +10 Evasion
Life Scanner, Labs, +1 Integrity
Reactor, Engine Room, +1 Shield
Leisure Center, Crew Quarters, +5 Evasion
""")

if __name__ == "__main__":
    items()
    characterSheet()
    equipment()
    followers()
    shipParts()