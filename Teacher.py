from User import User

class Teacher(User):
    def teach(self):
        return f"{self.getNombre()} inició sus clases"

    def __str__(self):
        return "Eres un profesor:\n" + super().__str__()