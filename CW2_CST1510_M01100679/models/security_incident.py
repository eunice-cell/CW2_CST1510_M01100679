class SecurityIncident:
    # Represents each one row from the "cyber_incidents" table
    def __init__(self, id: int, i_date: str, i_type: str, status: str, description: str, reported_by: str):
        self.__id = id
        self.__date = i_date
        self.__type = i_type
        self.__status = status
        self.__description = description
        self.__reported_by = reported_by

    #use the get method because variables are private You can’t access this from outside the class.
    def get_id(self) -> int:
        return self.__id

    def get_date(self) -> str:
        return self.__date

    def get_type(self) -> str:
        return self.__type

    def get_status(self) -> str:
        return self.__status

    def get_description(self) -> str:
        return self.__description

    def get_reporter(self) -> str:
        return self.__reported_by

    # Change the status of an incident
    def update_status(self, new_status: str) -> None:
        self.__status = new_status

    def get_i_type_level(self) -> int:
        """Return an integer severity level (simple example)."""
        mapping = {
            "low": 1,
            "medium": 2,
            "high": 3,
            "critical": 4,
        }
        return mapping.get(self.__i_type.lower(), 0)

    def __str__(self) -> str:
        return f"Incident(id={self.__id}, type={self.__type}, status={self.__status})"
