class User:
    """Represents a platform Multi-Domain Intelligence."""
# we create __init__ which is the constructor
    def __init__(self, id: int,username: str, password_hash: str, role: str):
        #we save the variables username, password, role and the __ makes them private
        self.__id = id
        self.__username = username
        self.__password_hash = password_hash
        self.__role = role

    # Return the user's ID
    def get_id(self) -> int:
        return self.__id

    # returns the username so that other part of the code.
    def get_username(self)-> str:
        return self.__username

    # returns the user’s role stored inside the object.
    def get_role(self)-> str:
        return self.__role

    #This method checks if a plain password matches the stored hashed password.
    def verify_password(self, plain_password: str, hasher)-> bool:
        return hasher.check_password(plain_password, self.__password_hash)

    # use __str__ to not print something like this <__main__.User object at 0x000001FFED45E7E0> if you use print()
    def __str__(self)-> str:
        return f"User(id={self.__id}, username={self.__username}, role={self.__role})"
