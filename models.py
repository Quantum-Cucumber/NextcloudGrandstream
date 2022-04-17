class Phone:
    def __init__(self, types: list[str], number: str):
        # type can be work, home, mobile
        types = [x.upper() for x in types]
        if "HOME" in types:
            self.type = "Home"
        elif "WORK" in types:
            self.type = "Work"
        elif "CELL" in types:
            self.type = "Mobile"
        else:
            self.type = "Mobile"

        self.number = number


class Contact:
    def __init__(self, name: str, phones: list[Phone]):
        if name.count(" ") == 1:  # 1 space - first and last
            self.firstName = name.split(" ")[0]
            self.lastName = name.split(" ")[1]
        elif name.count(" ") != 1:
            self.firstName = name
            self.lastName = None

        self.phones = phones
