from ticket import Ticket
from status import Status
from priority import Priority
from category import Category
import json

ticket_list = []


###CREATE / GENERATE###
def generate_ticket_id():

    if ticket_list != []:
        ticket = ticket_list[-1]
        generated_id = ticket.ticket_id +1

        return generated_id
    else:
        generated_id = 1

        return generated_id

def create_ticket(title,description,status,priority,category):

    generated_id = generate_ticket_id()
    new_ticket = Ticket(generated_id,title,description,status,priority,category)

    ticket_list.append(new_ticket)
    return new_ticket
###################################

###DELETE###
def delete_ticket(ticket_id):
    ticket = search_ticket(ticket_id)

    if ticket is not None:
        ticket_list.remove(ticket)
        save_ticket()
        return ticket

    return None


###SEARCH / SHOW FUNCTION###
def search_ticket(searched_id):

    for ticket in ticket_list:
        if ticket.ticket_id == searched_id:
            return ticket
    return None

def show_all_tickets():
    if ticket_list == []:
        print("No tickets available")
        return
    for ticket in ticket_list:
        print(ticket)

###################################

###UPDATE FUNCTIONS###
def update_status(ticket_id,new_status):
    ticket = search_ticket(ticket_id)
    if ticket is not None:
        ticket.status = new_status
        save_ticket()
        return ticket
    
    return None

def update_priority(ticket_id, new_priority):
    ticket = search_ticket(ticket_id)
    if ticket is not None:
        ticket.priority = new_priority
        save_ticket()
        return ticket
    
    return None

def update_category(ticket_id, new_category):
    ticket = search_ticket(ticket_id)
    if ticket is not None:
        ticket.category = new_category
        save_ticket()
        return ticket

    return None

def update_title(ticket_id, new_title):
    ticket = search_ticket(ticket_id)
    if ticket is not None:
        ticket.title = new_title
        save_ticket()
        return ticket

def update_description(ticket_id, new_description):
    ticket = search_ticket(ticket_id)
    if ticket is not None:
        ticket.description = new_description
        save_ticket()
        return ticket
###################################

def save_ticket():
    ticket_data = []

    for ticket in ticket_list:

        ticket_dictionary = {
            "ticket_id": ticket.ticket_id,
            "title": ticket.title,
            "description": ticket.description,
            "status": ticket.status.value,
            "priority": ticket.priority.value,
            "category": ticket.category.value
        }
        ticket_data.append(ticket_dictionary)

    with open("tickets.json", "w") as file:
        json.dump(ticket_data, file, indent=4)

def load_tickets():
    try:    
        with open("tickets.json", "r") as file:
            ticket_data = json.load(file)
    except FileNotFoundError:
        return

    for data in ticket_data:
        ticket = Ticket(
            data["ticket_id"],
            data["title"],
            data["description"],
            Status(data["status"]),
            Priority(data["priority"]),
            Category(data["category"])
        )            

        ticket_list.append(ticket)