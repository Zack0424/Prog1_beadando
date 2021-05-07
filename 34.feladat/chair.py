
class Chair:
    def __init__(self,number,toggle=True):
        self.number = number
        self.sitable = toggle
        self.taken = False
        self.show = number
        self.test_sitable = True
    def seatClosed(self):
        self.sitable = False

    def seatTaken(self):
        self.taken = True