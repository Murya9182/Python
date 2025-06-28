


class Mensa():
    def __init__(self):
        self.kunden = []

    def add_kunde(self, kunde):
        self.kunden.append(kunde)

    def remove_kunde(self, kunde):
        self.kunden.remove(kunde)

    def notify(self):
        for kunde in self.kunden:
            kunde.update()

class Kunde():
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"{self.name} has been notified.")


class Mitarbeiter(Kunde):
    def __init__(self, name):
        super().__init__(name)

    def update(self):
        print(f"{self.name} (Mitarbeiter) has been sent a letter.")

class Student(Kunde):
    def __init__(self, name):
        super().__init__(name)

    def update(self):
        print(f"{self.name} (Student) has been sent an email.")


# Example usage
mensa = Mensa()
kunde1 = Kunde("Max")
kunde2 = Mitarbeiter("Anna")
kunde3 = Student("Tom")

mensa.add_kunde(kunde1)
mensa.add_kunde(kunde2)
mensa.add_kunde(kunde3)

mensa.notify()
