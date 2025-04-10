import data

def getBool(prompt):
    """
    prompts the user for yes or no. Returns true if user enters "y" or "yes" in any capitalizaion, else returns false.
    """
    response = input(prompt + " (y/n): ").lower()
    return response in ["y", "yes"]

def enter():
    input("\nPress enter to continue...")

def isValidInt(val, limit = None):
    try:
        val = int(val)
    except:
        print("\nThat is not a number.")
        enter()
        return False
    if val < 0 or (limit and val > limit):
        if limit:
            print(f"\nThat number is not in range [0-{limit}]")
        else:
            print("\nThe number must be greater than 0")
        enter()
        return False
    return True

def getYear() -> str:
    # TODO: check for preset year and only show things from the set year.
    year = input("What year (2021-2024): ")
    if isValidInt(year) and int(year) in data.years:
        return year
    return 0

def checkValidYear(year):
    if not str(year).isnumeric() or int(year) not in data.years:
        print("Invalid year entered.")
        enter()
        return False
    return True

def printMenuFromList(mainList: list, checkList: list = None, printOne = None):
    offers = []
    count = 0
    for item in mainList:
        if checkList and item[0] in checkList:
            continue
        count += 1
        print(f"{count}. ", end="")
        if printOne:
            printOne(item)
        else:
            print(item)
        offers.append(item)
    print("0. Go Back")
    return offers, count

def modifyAttr(a, val):
    setattr(data, a, getattr(data, a) + val)

def getValidChoice(prompt: str, limit: int = None):
    choice = input(prompt)
    if isValidInt(choice, limit):
        return int(choice)
    return 0