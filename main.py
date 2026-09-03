

from priority import Priority
from status import Status
from category import Category
from ticket_manager import *




def show_menu():

    while True:

        print("1 - Create ticket\n2 - Show all tickets\n3 - Search ticket\n4 - Update ticket\n5 - Delete ticket\n6 - Exit")
        choice = input().strip().lower()
        #################
        if choice == "create ticket" or choice == "1":
            title = input("Title: ").strip()
            description = input("Description: ").strip()  

            while True:
                status = input("Status:\n 1 - Pending \n 2 - In progress\n 3 - Closed ").strip().lower()
                if status == "pending" or status == "1":
                    status = Status.PENDING
                    break
                elif status == "in progress" or status == "2":
                    status = Status.IN_PROGRESS
                    break
                elif status == "closed" or status == "3":
                    status = Status.CLOSED
                    break
                else:
                    print("Please choose 1,2,3 or enter a valid status")

            while True:
                priority = input("Priority:\n 1 - Low\n 2 - Medium\n 3 - High\n 4 - Critical ").strip().lower()
                if priority == "1" or priority == "low":
                    priority = Priority.LOW
                    break
                elif priority == "2" or priority == "medium":
                    priority = Priority.MEDIUM
                    break
                elif priority == "3" or priority == "high":
                    priority = Priority.HIGH#
                    break
                elif priority == "4" or priority == "critical":
                    priority = Priority.CRITICAL
                    break
                else:
                    print("Please choose 1,2,3,4 or enter a valid priority")
                    
            while True:
                category = input("Category:\n 1 - Software\n 2 - Hardware\n 3 - Server ").strip().lower()
                if category == "1" or category == "software":
                    category = Category.SOFTWARE
                    break
                elif category == "2" or category == "hardware":
                    category = Category.HARDWARE
                    break
                elif category == "3" or category == "server":
                    category = Category.SERVER
                    break
                else:
                    print("Please choose 1,2,3 or a valid category")

            create_ticket(title,description,status,priority,category)
        ######################################

        elif choice == "show all tickets" or choice == "2":
            show_all_tickets()
        ######################################
        elif choice =="search ticket" or choice == "3":

            while True:    
                try:
                    searched_id = int(input("Please input ticket_id"))
                except ValueError:
                    print("Please input correct ID. No string allowed")
                    continue

                result = search_ticket(searched_id)
                if result is not None:
                    print(result)
                    break
                else:
                    print("No ticket found")
                    break
        ##################################### 
        elif choice == "update ticket" or choice == "4":
            
            while True:
        
                try:
                    ticket_id = int(input("Select ticket ID"))
                    result = search_ticket(ticket_id)
                    if result is not None:
                        break
                    else:
                        print(f"Ticket with ID {ticket_id} not found")

                except ValueError:
                    print("ticket_id has to be int")

            choose_update = input("1 - Update status\n2 - Update priority\n3 - Update category").strip().lower()
            if choose_update == "1" or choose_update == "update status":

                while True:
                    new_status = input("Status:\n 1 - Pending \n 2 - In progress\n 3 - Closed ").strip().lower()
                    if new_status == "pending" or new_status == "1":
                        new_status = Status.PENDING
                        break
                    elif new_status == "in progress" or new_status == "2":
                        new_status = Status.IN_PROGRESS
                        break
                    elif new_status == "closed" or new_status == "3":
                        new_status = Status.CLOSED
                        break
                    else:
                        print("Please choose 1,2,3 or enter a valid status")
                update_status(ticket_id, new_status)

            elif choose_update == "2" or choose_update == "update priority":
                
                while True:
                    new_priority = input("Priority:\n 1 - Low\n 2 - Medium\n 3 - High\n 4 - Critical ").strip().lower()

                    if new_priority == "1" or new_priority == "low":
                        new_priority = Priority.LOW
                        break
                    elif new_priority == "2" or new_priority == "medium":
                        new_priority = Priority.MEDIUM
                        break
                    elif new_priority == "3" or new_priority == "high":
                        new_priority = Priority.HIGH
                        break
                    elif new_priority == "4" or new_priority == "critical":
                        new_priority = Priority.CRITICAL
                        break
                    else:
                        print("Please choose 1,2,3,4 or enter a valid priority")
                update_priority(ticket_id, new_priority)        

            elif choose_update == "3" or choose_update == "update category":

                while True:
                    new_category = input("Category:\n 1 - Software\n 2 - Hardware\n 3 - Server ").strip().lower()

                    if new_category == "1" or new_category == "software":
                        new_category = Category.SOFTWARE
                        break
                    elif new_category == "2" or new_category == "hardware":
                        new_category = Category.HARDWARE
                        break
                    elif new_category == "3" or new_category == "server":
                        new_category = Category.SERVER
                        break
                    else:
                        print("Please choose 1,2,3 or a valid category")
                update_category(ticket_id,new_category)                        
                    
            else:
                print("Please choose 1, 2, 3 or enter a valid option.")

   

        elif choice == "exit" or choice == "6":
            break

show_menu()
