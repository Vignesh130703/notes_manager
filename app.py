import os

FILE_NAME = "notes.txt"


def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as f:
        f.write(note + "\n")
    print("✅ Note added!\n")


def view_notes():
    if not os.path.exists(FILE_NAME):
        print("No notes yet.\n")
        return

    with open(FILE_NAME, "r") as f:
        notes = f.readlines()

    if not notes:
        print("No notes saved.\n")
        return

    print("\n📒 Your Notes:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note.strip()}")
    print()


def delete_all_notes():
    open(FILE_NAME, "w").close()
    print("🗑️ All notes deleted!\n")


def delete_single_note():
    with open(FILE_NAME, "r") as f:
        notes = f.readlines()

    view_notes()
    num = int(input("Enter note number to delete: "))

    if 1 <= num <= len(notes):
        notes.pop(num - 1)

        with open(FILE_NAME, "w") as f:
            f.writelines(notes)

        print("✅ Note deleted!\n")
    else:
        print("Invalid number!\n")


def search_note():
    keyword = input("Enter keyword: ").lower()

    with open(FILE_NAME, "r") as f:
        notes = f.readlines()

    found = False
    for note in notes:
        if keyword in note.lower():
            print("🔍 Found:", note.strip())
            found = True

    if not found:
        print("No matching notes.\n")


def menu():
    while True:
        print("====== 📝 Notes Manager ======")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete One Note")
        print("4. Delete All Notes")
        print("5. Search Note")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_single_note()
        elif choice == "4":
            delete_all_notes()
        elif choice == "5":
            search_note()
        elif choice == "6":
            print("Bye 👋")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    menu()
