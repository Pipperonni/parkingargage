tickets = [num for num in range(1,46)]
spaces = [num for num in range(1,46)]
current_ticket = {}


class ParkingGargage:

    def __init__(self, spaces, tickets):
        self.spaces = spaces
        self.tickets = tickets
    
    def space_change(self):# for updating parking spaces list
        self.spaces = spaces.pop()
        return 

    def ticket_tracking(self):# for updating tickets list
        tickets.pop()
        users_ticket = "".join("Ticket#" + str(self.spaces))
        print(users_ticket)
        return 
       
