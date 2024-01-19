#to-do list
#Ngoc Nguyen & Kayla McClendon
#1-12-24

#starter to make the intial list for the user
print("make a to-do list with 5 items!!")
todoList = [input("Add an item: ")]
for i in range (4):
    todoList.append(input("add another: "))
print(todoList)

#function to run the code again
def again():
    next = input ("would you like to continue? ")
    next = next.capitalize()
    if next == "Yes":
        toDo()
    elif next == "No":
        end()

#ends the code
def end():
    print("Bye-Bye :)!")

#gives the users options regarding the previously made list
def toDo():
    global todoList
    print("1. Add an item \n2. Print list \n3. Mark item as completed \n4. Remove item from list \n5. Remove all tasks from the to-do list \n6. Sort the list alphabetically \n7. Count the number of items on the to-do list \n8. End program")
    ans = input("Which option would you like, 1-5: ")
    #ask the user to add a single task to their list
    if ans == "1":
        todoList.append(input ("add a task: "))
        again()
    #displays the current list
    elif ans == "2":
        print (todoList)
        again()
    
    #marks an item the list that the user stated is completed
    elif ans == "3":
        com = input(print(todoList,"Which one have you completed? "))
        i = todoList.index(com)
        todoList[i] = com + "X"
        print(todoList)
        again()
    
    #allows the user to remove an item off of the list
    elif ans == "4":
        r = input(print(todoList,"Which one do you want to remove? "))
        todoList.remove(r)
        print(todoList)
        again()

    #allows the user to clear entire list
    elif ans == "5":
        todoList.clear()
        print(todoList)
        again()

    #sorts the list alphabetically
    elif ans == "6":
        todoList.sort()
        print(todoList)
        again()
    
    #tells the user the number of items in their list
    elif ans == "7":
        g = len(todoList)
        print(todoList)
        print("There are " + str(g) + " items in your list")
        again()

    #ends the program
    elif ans == "8":
        end()
    #Informs user of their mistake and re runs the program
    else:
        print ("not an option, try again")
        toDo()
#main
toDo()