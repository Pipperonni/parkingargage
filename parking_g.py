
tickets = [num for num in range(1,3)]
spaces = [num for num in range(1,3)]



class ParkingGargage():

    def __init__(self):
        self.current_ticket = {}
        
    
    def space_change(self):
        spaces.pop()
        self.ticket_tracking()
    
    def ticket_tracking(self):
        user_ticket = tickets.pop()
        for i in range(len(tickets)):
            if i == user_ticket:
                print(f"Ticket #{user_ticket}")
        users_choice = input("Would you like to pay now? (y/n): ")
        if users_choice == "y":
            prep = Paid(pre_paid="", pay_later="")
            prep.pre_pay()
            


    def ticket_pay(self): 
        pass
    
    def run(self):
        user_choice = input("Are you parking: (y/n): ") 
        if user_choice == "y":
            self.space_change()
        elif user_choice == "n":
            return
            
    
    def leaving():
         pass

# class Ticket(ParkingGargage):

#     def __init__(self, spaces, tickets, show_if_paid):
#         super().__init__(self, spaces, tickets)
#         self.show_if_paid = show_if_paid

#     def take_ticket(self): # take ticket
#         pass # printed message "Welcome, please take your ticket."
    # input("To pay now enter 1, for later enter 2:  ")
                    # If user enters 1, (go to paid function) also, decrease both tickets list and spaces list by 1
                    # If user enters 2, update current_ticket dictionary to False(pay later), decrease both tickets list, and spaces list by 1, also quit program
    
    #def print_ticket_tf()           
        #pass
    
class Paid():

    def __init__(self, pre_paid, pay_later):
        self.pre_paid = pre_paid 
        self.pay_later = pay_later

    def pre_pay(self):
        print("Please pay $5.00: (y/n): ")
        # paid function for parking before and after parking
            
            # Pre-pay function: if user inputs "now": input("Please pay $5.00: (y/n): ")
                # If "y" then update current_ticket dictionary to True(they pre-paid) end program
                # If "n"  input("To pay now enter 1, for later enter 2:  ")
                    # If user enters 2, update current_ticket dictionary to False(pay later), end program

            # Pay when leaving function:
                # input("Please pay $5.00: (y/n) ")
                    # If user enters "y" print "Have a nice day."
                    # If user enters "n" repeat prompt: input("Please pay $5.00: (y/n) ")

# For All Inputs: if they do not enter the correct inputs prompt message: "Input Invalid

new_customer = ParkingGargage()
new_customer.run() 
    
