from enum import Enum

class Category(Enum):
    SOFTWARE = "Software"
    HARDWARE = "Hardware"
    SERVER = "Server"

    def __str__(self):
        return self.value