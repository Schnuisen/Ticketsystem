from ticket import Ticket
from priority import Priority
from status import Status
from category import Category

ticket_list = []

###CREATE / GENERATE###
def generate_ticket_id():

    if ticket_list != []:
        ticket = ticket_list[-1]
        generated_id = ticket.ticket_id +1
        print(generated_id)
        return generated_id
    else:
        generated_id = 1
        print(generated_id)
        return generated_id

def create_ticket(title,description,status,priority,category):

    generated_id = generate_ticket_id()
    new_ticket = Ticket(generated_id,title,description,status,priority,category)

    ticket_list.append(new_ticket)
    return new_ticket
###################################

###DELTE###
def delete_ticket(ticket_id):
    ticket = search_ticket(ticket_id)

    if ticket is not None:
        ticket_list.remove(ticket)
        return ticket

    return None


###SEARCH FUNCTION
def search_ticket(searched_id):

    for ticket in ticket_list:
        if ticket.ticket_id == searched_id:
            return ticket
    return None
###################################

###UPDATE FUNCTIONS###
def update_status(ticket_id,new_status):
    ticket = search_ticket(ticket_id)
    if ticket is not None:
        ticket.status = new_status
        return ticket
    
    return None

def update_priority(ticket_id, new_priority):
    ticket = search_ticket(ticket_id)
    if ticket is not None:
        ticket.priority = new_priority
        return ticket
    
    return None

def update_category(ticket_id, new_category):
    ticket = search_ticket(ticket_id)
    if ticket is not None:
        ticket.category = new_category
        return ticket
    
    return None
###################################





ticket1 = create_ticket("Computer stürzt ab", "Nach hochfahren stürzt der Computer sofort ab", Status.PENDING, Priority.HIGH, Category.HARDWARE)
print(ticket1)
ticket2 = create_ticket("Casddasd", "Nasasfasdasdb", Status.IN_PROGRESS, Priority.LOW, Category.SERVER)
print(ticket2)

delete_ticket(2)
