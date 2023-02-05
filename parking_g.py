
tickets = [num for num in range(1,3)]
spaces = [num for num in range(1,3)]



class ParkingGargage():


    def __init__(self):
        self.current_ticket = []
        
    
    def space_change(self):
        spaces.pop()
        self.ticket_tracking()
    
    def ticket_tracking(self):
        user_ticket = tickets.pop()
        print(f"your Ticket {str(user_ticket)} in space # {user_ticket}")
        users_choice = input("Would you like to pay now? (y/n): ")
        if users_choice == "y":
            prep = Paid(pre_paid="", pay_later="")
            prep.pre_pay()



   
    
            
    def leaving(self):
          user_show_ticket = input("what is your ticket#?: (ticket#): ")
          for ticket, val in self.current_ticket.items():
           print(current_ticket[user_show_ticket])
           print("Have a nice day! ")
           return
    def run(self):
        while True:
            user_choice = input("are you parking: (y/n) ")
            if user_choice == "y":
             
    
class Paid():

    def __init__(self, pre_paid, pay_later):
        self.pre_paid = pre_paid 
        self.pay_later = pay_later

    def pre_pay(self):
       while True:
         user_choice == input("Please pay $5.00: (y/n): ")
         if user_choice == "y":
            print("Ticket has been paid, you have 15min to leave")
            back_to_run = P

          

new_customer = ParkingGargage()
new_customer.current_ticket
    



        
    


