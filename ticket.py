from status import Status

class Ticket:

    def __init__(self,ticket_id,title,description,status,priority,category):
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.category = category

    def change_status(self,new_status):
        self.status = new_status
        print("Status changed to", self.status)
        return self.status

    def change_prio(self,new_priority):
        self.priority = new_priority
        print("Priority changed to", self.priority)
        return self.priority

    def change_category(self,new_category):
        self.category = new_category
        print("Category changed to", self.category)
        return self.category

    
    def __str__(self):
        return f"Ticket_ID: {self.ticket_id}\nTitle: {self.title}\nDescription {self.description} \nStatus: {self.status}\nPrio: {self.priority}\nCategory: {self.category}"