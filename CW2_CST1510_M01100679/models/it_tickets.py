class ITTicket:
    """ this class represents one dataset record from the "it tickets" table"""

    def __init__(self, id: int, priority: str, description: str, status: str, created_at: str, created_date: str):
        self.__id = id               # database ID
        self.__priority = priority    # low, medium, high
        self.__description = description  # full text of the ticket
        self.__status = status        # open, closed, in-progress
        self.__created_at = created_at    # time
        self.__created_date = created_date  # date

    # Getter method: These methods allow other parts of your program to read the values
    def get_id(self) -> int:
        return self.__id

    def get_priority(self) -> str:
        return self.__priority

    def get_description(self) -> str:
        return self.__description

    def get_status(self) -> str:
        return self.__status

    # Mark ticket as closed
    def close(self) -> None:
        self.__status = "Closed"

    # the __str__ helps python print the object in a readable way
    # if use print you get something like this :<__main__.User object at 0x000001FFED45E7E0>
    def __str__(self) -> str:
        return f"Ticket(id={self.__id}, priority={self.__priority}, status={self.__status})"
