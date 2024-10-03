import json

# Global list to store transactions
transactions = []


def load_transactions(): # load transactions from a json file
    try:
        with open("transactions.json", "r") as file: # open the json file in read mode
            load = json.load(file)

        for load_element in load:
            transactions.append(load_element)

    except FileNotFoundError:
        # if file not found creat a error message
        pass


def save_transactions():
    # this will save the data to the json file
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)


def add_transaction(amount, purpose, about, date): #creat a funtion to add transaction to the json file
    print("___Adding the transaction___ ")
    try:
        # get 4 inputs from the user as amount,purpose of the transaction,date and the is that a income or a expense
        amount = float(input("Transactions amount: "))
        purpose = str(input("Enter the description: "))
        while True:
            # gets a valid input from the user
            about = str(input("Type of the transaction (Income/Expense): ")).capitalize()
            if about in ["Income","Expense"]:
                break
                # if user Entered correctly break the loop
            else:
                # if user did not enter the input correctly loop will iterate until it s gets true
                print("please enter income or expense!")
        while True:
            date = str(input("Enter the date of transaction(YYYY-MM-DD): "))
            if len(date) == 10:
                break
            else:
                print("please enter date in (YYYY-MM-DD) format:   ")

        # add inputetd details to the end of the json file
        transactions.append([amount, purpose, about, date])
        save_transactions()
        # save the json file
        print("Successfully added")
        return()
    except ValueError:
        print("Enter the Valid amount")

def view_transactions():# funtion to viwe the transaction added to the json file
    print("___Total transaction___")
    if not transactions:
        # this massage will pringt if there is no transaction in the json file
        print("You haven't add any transactions yet.")
    else:
        print(f"    amount(LKR)           Description                 Type                   Date                ")
        # count will show the how meny transactions in the file
        count = 1

        for transaction in transactions:
            #print the transaction in the transactions[]
            print("________________________________________________________________________________________________________________")
            print(f"{count}:  Amount:{transaction[0]}     Description:{transaction[1]}              Type:{transaction[2]}           Date:{transaction[3]}")
            count += 1
            # count will be increase by 1 after one iterete has completed
def update_transaction():
    # if ueser needed to update the current information in the file
    # ask the user what change and in what transaction
    transaction_update = int(input("transaction number you needed to be updated: "))

    select_list = transactions[int(transaction_update) - 1]
    if 0 < transaction_update <= len(transactions):
        print("you selected the", select_list) # print the selected line for confirmation
        while True:
            try:
                print("_________________________________________________")
                print("1.Amount     2.Description    3.Type    4.Date")
                print("_________________________________________________")
                # ask the user to select the number from the above

                change_selection = int(input("Select the number: "))
                if change_selection == 1:
                    new_amount = int(input("Enter the new amount: "))
                    transactions[transaction_update - 1][0] = new_amount
                    # change the selected variable in the selected list
                    save_transactions()
                    # save transaction
                elif change_selection == 2:
                    new_purpose = str(input("Enter the new Description: "))
                    transactions[transaction_update - 1][1] = new_purpose
                    save_transactions()
                elif change_selection == 3:
                    new_about = str(input("Type of transaction (Income/Expense):  "))
                    transactions[transaction_update - 1][2] = new_about
                    save_transactions()
                elif change_selection == 4:
                    new_date = str(input("Enter the new date:  "))
                    transactions[transaction_update - 1][3] = new_date
                    save_transactions()
                print("Updated successfully")
                break
            except ValueError:
                print("Enter a valid amount")


def delete_transaction():
    # deleting the transaction
    print("___Deleting transaction___")
    d_transactions = int(input("Enter the transaction number to delete:  ")) -1
    # get s input from ther user and -1 to asing the value
    # list will asing the value from the 0

    if 0 <= d_transactions < len(transactions):
        
        # if the number user enterd is in range of above than that list will bee deleted

        del transactions[d_transactions]
        print("Successfully deleted")
        save_transactions()

    else:
       print("    Enter a valid transaction!")


def display_summary():
    print("___Transaction summary___ ")
    print(f"Total transaction you has done{len(transactions)}")
    income_total = 0
    expense_total = 0
    for transaction in transactions:

        if transaction[2]  == "Income":
            # this will collect all the incomes and add them all to the income_total variable
            income_total += transaction[0]
            print(f"Total of income:{income_total}")
        else:
            # this will add all expense and store in the expense_total
            expense_total += transaction[0]
            print(f"Total of Expense{expense_total}")
    net_total = income_total - expense_total
    print(net_total)


def main_menu():
    load_transactions()
    while True:
        # print the options for the user
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        selection = input("Select the number: ")
        # selecting the
        if selection == "1":
            # add tyransactions to the list
            add_transaction("amount"," purpose"," about", "date")
        elif selection == "2":
            # view added transactions
            view_transactions()
        elif selection == "3":
            # update a transaction in the list
            update_transaction()
        elif selection == "4":
            # delete the transactions in the list
            delete_transaction()
        elif selection == "5":
            # display the total transaction in the list and total incomes and expenses
            display_summary()
        elif selection == "6":
            # to exit from the loop
            print("your transactions been added to the list SUCCESSFULLY")
            break
        else:
            print("Enter a valid number!")


if __name__ == "__main__":
    main_menu()
