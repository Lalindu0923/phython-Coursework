import json

transactions = {}
#global transaction dictionary to store 
# File handling functions

def load_transactions():  #load transactions to a json file 
    try:
        global transactions

        with open ("transaction.json","r") as file:  #if not exssist creat a folder 
            transactions = json.load(file)

    except (FileNotFoundError, json.decoder.JSONDecodeError):#if these  errors showed let them pass   
        pass



# def save_transactions():        #save transactions 
#     with open("transaction.json","w") as file:
#         json.dump(transactions, file)  #dump transaction to the transaction folder 
def save_transaction():
    with open("transaction.json",'w') as file:
        json.dump(transactions,file)

def read_bulk_transactions_from_file(filename): #funtion to read from a external file and add details to the dictionary
    try:
    # Open and read the file, then parse each line to add to the transactions dictionary
        filename = filename + ".txt"
        file = open(filename,"r") #open the user enterd file as a file 
        for line in file:  #read the every line in the file 
            #print the lines
            #print(line) 
            line = line.strip().split() #this will turn line in to list
            print(line)
            key = line[0] 
            #print(key)
            value = {"amount":line[3],"date":line[1],"description":line[2]} #access index numbers in the list
            #print(value) #print lines to see the transactions in the file
            
            if key in transactions:     #if transaction type alredy in the transaction append to exssisten transaction type
                transactions[key].append(value)
                save_transaction()
            else:
                transactions[key] = [value] #if not type exssisten add the new type and add the transactions to it 
                save_transaction() 
    except FileNotFoundError:
        print("---File not fount---")    
    
def add_transaction():
    print("____Adding  Transactiopns____")
    while True:
        transaction_type = str(input("Enter the type of transaction: ")) 
        if len(transaction_type) == 0:
            print("Transaction type cannot be empty!")  #make sure user enterd a transaction type 
            continue
        else:
            break
    while True:
        purpose = input("Enter the description: ")
        if len(purpose) ==0:
            print("     Description cannot be empty!") #purpose cannot be empty 
            continue
        else:
            break
    while True:
        try:
            amount = float(input("Transaction amount: ")) #if user enterd a srting insted of numbers
            if type(amount) == str:
                continue
            else:
                break
        except ValueError:
            print("     Enter only numbers!")
        

            
    while True:
                date = str(input("Enter the date of transaction(YYYY-MM-DD): ")) # user has to enter date as a valid input 
                if len(date) == 10:
                    break
                else:
                    print("please enter date in (YYYY-MM-DD) format:   ")
            
    transactions_done= {"amount":  amount, "date": date,"description":purpose}  
    # add amount,date and description to the dictionary as amount,date and purpose and store in a variable 
    if transaction_type in transactions:
            transactions[transaction_type].append(transactions_done)
    else:
            transactions[transaction_type] = [transactions_done]
    save_transaction()

    print("____Transaction added successfully____")
    
    
            
def view_transactions():
    global transactions
    if not transactions:
        print("---Pleas add transaction to view---")
    else:
        print("\n___Transactions___")
        
        i = 1   # i is for count the number of keys in the dictionary 
        for key, value in transactions.items(): 
            print(f"  \n{i} |______{key}______|")
            count = 1 #count is for count number of transactions in a one type
            for values in value: # these date,amount and descriptions are stored in the value and accsess each values in value
                print(f" {count}   date: {values['date']}, description : {values['description']}, amount: {values['amount']}") 
                count += 1 
            print("___________________________________________________________________________________________________")
            i += 1
        
           
    
    
def update_transactions():
    view_transactions()
    print("----------------------------------------------")
    try:
        update_type = str(input("Enter the transaction type to update: ")) #let the user select the transaction type to update
    except TypeError:
        print("Enter the transaction type") 
    if update_type in transactions:  #if user input a  type 
            while True:
                transaction_number = int(input(" **Enter the transaction number: ")) #check transaction type in the dictionary and if it is valid,
                if  transaction_number >= 1  and len(transactions[update_type]) <= transaction_number:
                    print("____select the number you wish to update.___")
                    print("  1.Amount \n  2.Date \n  3.Description") #let the user select the option to select user need to update 
                    to_update = input("select the number to update: ")
                
                    if to_update == "1":    #select number 1 to update the amount of the transaction select
                        new_amount = int(input("   Enter the new amount: "))
                        transactions[update_type][transaction_number-1]["amount"] = new_amount
                                    #key           transaction number      selection to update
                        print("____New amount updated successfully!____")
                        save_transactions()
                        break    
                    elif to_update == "2":  #select number 2 to update the date of the transaction select
                        new_date = str(input("   Enter the date of transaction(YYYY-MM-DD): "))
                        transactions[update_type][transaction_number - 1]["date"] = new_date
                        print("___ New date updated successfully!___")
                        save_transactions()
                        break
                        
                    elif to_update == "3":  #select number 3 to update the description of the transaction select
                        new_Description = input("   Enter the new discription of the transaction: ")
                        transactions[update_type][transaction_number - 1]["description"] = new_Description
                        print("___New description updated successfully!___")
                        save_transactions()
                        break
                    else:
                        print("---Enter number 1 to 3---")
                    #each break will exit the if else loop after its updated
                break  #to exit while loop      
                
def delete_transaction():
    view_transactions()
    global transactions
    # count = 1
    
    del_tran_type = input("Enter the transaction type wish to delete: ") #let the user to select the type of the transaction needed to delete transaction include
    if del_tran_type in transactions:
        print(transactions[del_tran_type]) #print the transactions in the selected transaction type
        while True:
            del_transaction = int(input("   Enter the transaction you wish to delete: ")) - 1   #transaction in the transaction type are in a list
            # - 1 to acsses corrct index in the list
            if  0 <= del_transaction <= len(transactions):
                del transactions[del_tran_type][del_transaction] #delete the selected transaction in the transaction type
                if len(transactions[del_tran_type]) == 0:
                    del transactions[del_tran_type]
                    print("   transaction type also deleted")
                print("___successfully deleted!___")
                save_transactions()
                break
            else:
                print("---Enter a valid number!---  ")
    else:
        print("---Enter a valid transaction!---")    
        


def display_summary():
    print("___Transaction summary___")
    print(f"* You have added {len(transactions)} transaction type") #total transaction types in the transactions dictionary
    print(transactions.keys()) #print all the types in the transactions
    for key in transactions:
        
        for value in transactions[key]: # print vales in the key 
                print(value)
                
            
        
    
    
def main_menu():
        load_transactions()
        while True:
        # print the options for the user
            print("\n| Personal Finance Tracker |")
            print("+---------------------------+")
            print("  1. Add Transaction")
            print("  2. Add bulk transactions")
            print("  3. View Transactions")
            print("  4. Update Transaction")
            print("  5. Delete Transaction")
            print("  6. Display Summary")
            print("  7. Exit")
            print("-----------------------------")
            selection = input("Select the number: ")
            # selecting the option
            if selection == "1":
                # add tyransactions to the dictionary
                add_transaction()
            elif selection == "2":
                # add bulk transaction to the dictionary
                filename = input("Enter the file name: ")
                read_bulk_transactions_from_file(filename)
            elif selection == "3":
                # view added transactions
                view_transactions()
            elif selection == "4":
                # update a transaction in the dictionary
                update_transactions()
            elif selection == "5":
                # delete the transactions in the dictionary
                delete_transaction()
            elif selection == "6":
                # display the total transaction in the list and total incomes and expenses
                display_summary()
            elif selection == "7":
                # to exit from the loop
                print("your transactions been added to the list SUCCESSFULLY")
                break
            else:
                print("---Enter a valid number!---")

if __name__ == "__main__":
    main_menu()
