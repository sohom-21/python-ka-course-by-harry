# 5. Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,abording,destination):
        print(f'The ticket is booked in train no: {self.trainNo} from {abording}, to {destination}')
        pass

    def getStatus(self):
        print(f'Train no: {self.trainNo} is running on time')
        pass

    def getFare(self,abording,destination):
        print(f'The ticket fare in train no: {self.trainNo} from {abording}, to{destination} is {randint(222, 5555)}')
        pass

t = Train(16324)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")