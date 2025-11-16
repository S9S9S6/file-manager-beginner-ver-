import os
def create_file(file_name):
    try:
        with open(file_name, 'x') as f:
            print(f" File '{file_name}' created successfully.")
    except FileExistsError:
        print(f"⚠️ File '{file_name}' already exists.")
    except Exception as e:
        print(f"❌ Error creating file: {e}")

def view_all_files():
    files = os.listdir()
    if not files:
        print("📂 No files found in this directory.")
    else:
        print("\n📁 Files in current directory:")
        for file in files:
            print(f" - {file}")
        print()

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f" File '{file_name}' has been deleted.")
    except FileNotFoundError:
        print(f"⚠️ File '{file_name}' not found.")
    except Exception as e:
        print(f" Error deleting file: {e}")

def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            print(f"\n Content of '{file_name}':\n{'-'*40}\n{content}\n{'-'*40}\n")
    except FileNotFoundError:
        print(f"⚠️ File '{file_name}' not found.")
    except Exception as e:
        print(f" Error reading file: {e}")

def edit_file(file_name):
    try:
        with open(file_name, 'a') as f:
            content = input("✏️ Enter data to add: ")
            f.write(content + "\n")
            print(f" Data added to '{file_name}'.")
    except FileNotFoundError:
        print(f"⚠️ File '{file_name}' not found.")
    except Exception as e:
        print(f"❌ Error editing file: {e}")

def main():
    while True:
        print("\n========== FILE MANAGEMENT APP ==========")
        print("1️⃣  Create a file")
        print("2️⃣  View all files")
        print("3️⃣  Delete a file")
        print("4️⃣  Read a file")
        print("5️⃣  Edit a file")
        print("6️⃣  Exit")
        print("=========================================")

        choice = input("👉 Enter your choice (1–6): ").strip()

        if choice == '1':
            file_name = input("Enter file name: ").strip()
            create_file(file_name)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            file_name = input("Enter file name to delete: ").strip()
            delete_file(file_name)
        elif choice == '4':
            file_name = input("Enter file name to read: ").strip()
            read_file(file_name)
        elif choice == '5':
            file_name = input("Enter file name to edit: ").strip()
            edit_file(file_name)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()


                



