phonebook = {}

def create_records(name, number):
    if name == "" or number == "":
        print("Name or Number cannot be empty")
        return
    if name in phonebook:
        print("name already exist")
        return
    if not number.isdigit() or len(number) != 10:
        print("number must be in 10 digit or in numerical")
        return

    phonebook[name] = number
    print("Your record is added successfully")
    
def view_records():
    if not phonebook:
        print("Record are empty")
        return
    
    print("phonebook records:")
    for name, number in phonebook.items():
        print(f"name: {name}, number: {number}")
        
        
def update_records(name, new_number):
    if name not in phonebook:
        print("Name not excist in phonebook")
        return
    if not new_number.isdigit() or len(new_number) !=10:
        print("number must be in 10 digit or in numerical")
        return
    
    phonebook[name] = new_number
    print("Your record is updated successfully")
    
def delete_records(name):
    if name not in phonebook:
        print("Name not excist in phonebook")
        return
    
    del phonebook[name]
    print("record deleted successfully")
    
def search_records(name):
    if name not in phonebook:
        print("name not exist in phonebook")
        return
    
    print(f"name: {name}, number: {phonebook[name]}")
def main_menu():
    while True:
        print("my phonebook menu")
        print("1. create records")
        print("2. view records")
        print("3. update records")
        print("4. delete records")
        print("5. search records")
        print("6. Exit from my phone book")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            number = input("Enter your number")
            create_records(name, number)   
        elif choice == "2":
            view_records()
        elif choice == "3":
            name = input("Enter your name to update: ")
            number = input("Enter your number to update")
            update_records(name, number)
        elif choice == "4":
            name = input("Enter wgich name to delete: ")
            delete_records(name)
        elif choice == "5":
            name = input("Enter which name to search: ")
            search_records(name)
        elif choice == "6":
            print("exited the phonebook successfully")
            break
        else:
            print("invalid choice: ")
            
main_menu()
                
               
                             
                