
tickets = [num for num in range(1,46)]
spaces = [num for num in range(1,46)]
current_ticket = {}


class ParkingGargage:

    def __init__(self, spaces, tickets):
        self.spaces = spaces
        self.tickets = tickets
    
    def space_change():# for updating parking spaces list
        pass

    def ticket_tracking():# for updating tickets list
        pass

    def ticket_pay(): # for updating current_ticket dictionary
        pass
    
    def run():
        user_choice = input("Are you parking: (y/n): ") # If "n" go to leaving function
        if user_choice == "y":
            pass # go to take_ticket function in Ticket class
    
    def leaving():
        pass# leaving function: lives in parent class(ParkingGargage)
        # When user is leaving (input: "what is your ticket number? ")
            # If ticket comes back True(they pre-paid): prompt "Have a nice day" then end code
                # Increase both ticket list and parking spaces available
            # If ticket comes back False(pay later): direct the code to the paid function

class Ticket(ParkingGargage):

    def __init__(self, spaces, tickets, show_if_paid):
        super().__init__(self, spaces, tickets)
        self.show_if_paid = show_if_paid

    def take_ticket(): # take ticket
        pass # printed message "Welcome, please take your ticket."
    # input("To pay now enter 1, for later enter 2:  ")
                    # If user enters 1, (go to paid function) also, decrease both tickets list and spaces list by 1
                    # If user enters 2, update current_ticket dictionary to False(pay later), decrease both tickets list, and spaces list by 1, also quit program
    
    #def print_ticket_tf()           
        #pass
    
    class Paid():

        def __init__(self, spaces, tickets, paid):
            super().__init__(self, spaces, tickets)
            self.paid = paid 
            
    
        def paying():
            pass
        # paid function for parking before and after parking
            
            # Pre-pay function: if user inputs "now": input("Please pay $5.00: (y/n): ")
                # If "y" then update current_ticket dictionary to True(they pre-paid) end program
                # If "n"  input("To pay now enter 1, for later enter 2:  ")
                    # If user enters 2, update current_ticket dictionary to False(pay later), end program

            # Pay when leaving function:
                # input("Please pay $5.00: (y/n) ")
                    # If user enters "y" print "Have a nice day."
                    # If user enters "n" repeat prompt: input("Please pay $5.00: (y/n) ")

# For All Inputs: if they do not enter the correct inputs prompt message: "Input Invalid"
    


