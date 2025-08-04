#exercicio 1
# question 1
def question1():
    try:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        result = numerator / denominator
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid integers.")

    except FileNotFoundError:
        print("Error: The file 'dados.txt' was not found.")
    finally:
        print("Execution completed.")

# question 2
def question2():
    try:
        with open("dados.txt", "r") as file:
                r = file.read()
                print(r)
    except FileNotFoundError:   
        print("Error: The file 'dados.txt' was not found.")

# question 3
def question3():
    from random import randint
    read_num = randint(1, 100)
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < read_num:
            print("Too low! Try again.")
        elif guess > read_num:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number.")
            break

#exercicio2
def question4():
    print("""
    1. Add a new contact
    2. List all contacts
    3. Search for a contact
    4. Delete a contact
    0. Exit
    """)
    contacts = []
    while True:
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            contacts.append({"name": name, "phone": phone})
            print(f"Contact {name} added.")
        elif choice == '2':
            if contacts:
                print("Contacts:")
                print("----------")
                # Display all contacts
                print("Name: Phone")
                for contact in contacts:
                    print(f"{contact['name']}: {contact['phone']}")
            else:
                print("No contacts found.")
        elif choice == '3':
            name = input("Enter contact name to search: ")
            found = False
            for contact in contacts:
                if contact['name'] == name:
                    print(f"{contact['name']}: {contact['phone']}")
                    found = True
                    break
            if not found:
                print(f"Contact {name} not found.")
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            for contact in contacts:
                if contact['name'] == name:
                    contacts.remove(contact)
                    print(f"Contact {name} deleted.")
                    break
            else:
                print(f"Contact {name} not found.")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    clear()
    # question1()
    # input("Press Enter to continue...")
    # question2()
    # input("Press Enter to continue...")
    # question3()
    # input("Press Enter to continue...")
    question4()
    input("Press Enter to exit...")
    clear()

if __name__ == "__main__":
    main()
