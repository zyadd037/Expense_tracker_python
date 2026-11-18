import json  # عملنا استدعاء لمكتبة عشان نحفظ البيانات الموجوده ف list, dictionaries 

# I would devide project into smaller tasks to make functions more clear

expense = []  # I did an empty list to store income data in list 
try:
    with open("expenses.json" , "r") as file: # here made read function to the file for not missing data i store if I closed the program at all
        expenses = json.load(file) # return data from file to python

except FileNotFoundError: # if we didnt find the file then we would an empty list to collect all expenses
    expenses = []  

# the interface of the program 
while True:
    print("\n ===== Expense Tracker =====") #DataTypes
    print("1- Add Expenses : ")
    print("2- Show Expenses : ")
    print("3-Monthly Summary ")
    print("4-program has finished! : -------------- ")
    user_choice = input(" please Choose an option ") # i ask user to enter his choice :) 

# option 1 : Add Expenses 
if user_choice == "1":  # if user move to choice 1 so will meet some questions about entries like (amount, categories and date) and that what i provided through DataTypes.
    amount = float(input(" Enter the required amount :")) # i asked user to enter amount from float type
    category = input("Enter category of the product")      #asked user to enter category from str type
    date = input("Enter the current date of the operation") #asked user to enter category from str type

# ihere i made a dictionary for including different entries
    expense = {
        "amount" : amount ,
        "category" : category,
        "date" : date 

}

    expenses.append(expense) # i added dictionary into list so if i add new expenses in the future(append) it will be added or stores into list

    with open("expenses.json" , "w") as file:  # this function to store data through json.dump function and arrange data through (indent)
        json.dump(expenses , file , indent=4) # w is write function (module 4)

    print("expenses are added added successfully !")
 
# -----------------------------------------

# option 2 : Show Expenses 
elif user_choice == "2":
    for expense in expenses:
        print(f" Amount : {expense[amount]}")
        print(f" Category : {expense[category]}")
        print(f" Date : {expense[date]}")

#option 3 : Monthly Summary
elif user_choice == "3": # if user decided to choose date of operation
    date = input("Enter Month (YYY-MM) : ") # this line to ask user to enter month of registration 
    total = 0 
    count = 0 # i considered the 2 opertaion (total , count) with zero as a start  , total to calculate sum of categories and count to calculate the numb of them.
    category_totals = {} # is responsible for calculating expenses that related to their categories
    
    for expense in expenses: # for loop to move into every single expenses
        if expense["date"].startswith(month):  # starts.with(() if history started with month that user choose
            total += expense["amount"] #  if we found expenses in the required month so we would add in total
            count+=1 # and add 1 in count
            category = expense["category"]


            if category in category_totals: # in this part we put a condition to find simillar categories and add the amount 
                category_totals[category]+= expense["amount"]
            else:
                category_totals[category] = expense["amount"] # if category has not amy similar categories so we add it as new category

        if count == 0:
            print("No expenses found this month ! ")

        else:
            avg = total / count # average calculation
            print(f" Month : {month} ")
            print(f" total of categories : {category} ")
            print(f" average  : {avg:.2f} ") # showing value of avg with only 2 numb after . if its a float
            print("\n Catogeries Calculations : ")

            for category in category_totals: # for loop checking all catigories in prog
                category_avg =  category_totals[category] 
                print(f" {category} : {category_avg}") # showing results of category as value and category_avg as a key









