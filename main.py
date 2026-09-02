from ticket import Ticket
from priority import Priority
from status import Status
from category import Category

ticket_list = []

def search_ticket(searched_id):

    for ticket in ticket_list:
        if ticket.ticket_id == searched_id:
            return ticket
    return None

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

ticket1 = Ticket(1,"Drucker kaputt", "Drucker schluckt das papier. Komplett verstopft", Status.PENDING, Priority.CRITICAL, Category.SOFTWARE)
ticket2 = Ticket(2,"Computer stürzt ab", "Computer stürzt direkt nach dem Starten ab",Status.PENDING, Priority.CRITICAL, Category.HARDWARE)

ticket_list.append(ticket1)
ticket_list.append(ticket2)



print(ticket2)
update_category(2,Category.SOFTWARE)
print(ticket2)