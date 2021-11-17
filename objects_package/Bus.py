class Bus:
    def __init__(self,numofseats):
        self.seats = ['free' for i in range(numofseats)]

    def __str__(self):
        return f"{self.seats}"

    def geton(self,name):
        if 'free' in self.seats:
            self.seats[self.seats.index('free')]=name
        else:
            print(f"the passanger {name} cant get into the bus")
    def getoff(self,name):
        if name in self.seats:
            self.seats[self.seats.index(name)]='free'
        else:
            print(f"the passanger {name} didnt found")

