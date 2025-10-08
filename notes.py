import data
from util import getBool, getValidChoice, printMenuFromList

def notes_menu():
    print_notes()
    print()
    options = ["View notes", "Add note", "Modify note", "Delete note"]
    _, limit = printMenuFromList(options)
    choice = getValidChoice("Selection: ", limit)
    if choice == 0:
        return
    elif choice == 1:
        # print_notes()
        pass
    elif choice == 2:
        print("What note to add (or 0 to go back):")
        note = input("> ")
        if note != "0":
            data.notes.append(note)
            print(f"Added \"{note}\" to notes.")
    elif choice == 3:
        modify_note()
    elif choice == 4:
        delete_note()
    notes_menu()

def print_notes():
    print("\n--Notes--")
    if len(data.notes) == 0:
        print("(None)")
    else:
        for note in data.notes:
            print(note)

def select_note(text):
    print(f"\nSelect a note to {text}:")
    _, limit = printMenuFromList(data.notes)
    choice = getValidChoice("Selection: ", limit)
    return choice - 1

def modify_note():
    index = select_note("modify")
    if index == -1:
        return

    current_note = data.notes[index]
    print("\nCurrent:", current_note)

    try:
        # Try prompt_toolkit (cross-platform, allows editing prefilled text)
        from prompt_toolkit import prompt
        note = prompt("New: ", default=current_note)

    except ImportError:
        # Fallback to normal input
        note = input("New: ")

    data.notes[index] = note
    print("The note has been updated.")
    return

def delete_note():
    index = select_note("modify")
    if index == -1:
        return
    print("\nNote:", data.notes[index])
    if getBool("Are you sure you want to delete this note?"):
        data.notes.pop(index)
        print("The note has been deleted.")
    return