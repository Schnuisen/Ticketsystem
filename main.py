from ticket import Ticket
from priority import Priority
from status import Status
from category import Category

ticket_list = []

def search_ticket(searched_id):

    for ticket in ticket_list:
        if ticket.ticket_id == searched_id:
            print(ticket)
            return ticket
    return None

ticket1 = Ticket(1,"Drucker kaputt", "Drucker schluckt das papier. Komplett verstopft", Status.PENDING, Priority.CRITICAL, Category.SOFTWARE)
ticket2 = Ticket(2,"Computer stürzt ab", "Computer stürzt direkt nach dem Starten ab",Status.PENDING, Priority.CRITICAL, Category.HARDWARE)

ticket_list.append(ticket1)
ticket_list.append(ticket2)


result = search_ticket(2)
print(result.title)
print(result.category)