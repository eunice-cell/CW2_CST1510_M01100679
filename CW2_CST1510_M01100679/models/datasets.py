class Dataset:
    """ this class represents one dataset record from the "datasets" table"""

    def __init__(self, id: int, name: str, rows: int, columns: int, uploaded_by: str, date: str):

       # The __init__ function runs automatically when you create a new dataset object.
       # each object will have it's own method and variable

        self.__id = id
        self.__name = name
        self.__rows = rows
        self.__columns = columns
        self.__uploaded_by = uploaded_by
        self.__date = date

    #the getter methods :These methods allow other parts of your program to READ the values
    #without directly touching the private variables (good for safety)

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_rows(self) -> int:
        return self.__rows

    def get_columns(self) -> int:
        return self.__columns

    def get_uploaded_by(self) -> str:
        return self.__uploaded_by

    def get_date(self) -> str:
        return self.__date

    #the __str__ helps python print the object in a readable way
    #if use print you get something like this :<__main__.User object at 0x000001FFED45E7E0>

    def __str__(self) -> str:
        return f"Dataset(id={self.__id}, name={self.__name}, rows={self.__rows}, columns={self.__columns})"
