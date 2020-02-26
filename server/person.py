class Person:
    """
    Represents a person, holds name, socket client and address
    """
    def __init__(self, addr, client):
        self.addr = addr
        self.client = client
        self.name = None

    def set_name(self, name):
        """
        sets the person name
        :param name: str
        :return: None
        """
        self.name = name

    def __repr__(self):
        return f"Person({self.addr}, {self.name})"

    def __str__(self):
        return f"Person({self.addr}, {self.name})"

