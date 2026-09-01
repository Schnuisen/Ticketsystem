from enum import Enum

class Status(Enum):

    PENDING = "Pending"
    IN_PROGRESS ="In progress"
    CLOSED = "Closed"


    def __str__(self):
        return self.value