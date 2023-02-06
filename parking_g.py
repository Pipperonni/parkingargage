
tickets = [1,2,3,4,5,6,7,8,9,10,11]
spaces = [1,2,3,4,5,6,7,8,9,10,11]
current_ticket = {}


class ParkingGargage():

    def __init__(self):
        self.ticket_test = {}
        
    
    def space_parking(self):
        if len(spaces) == 1:
            print("Sorry, there are no available parking spots. Please come back later.")
        else:
            spaces.pop()
            self.ticket_tracking()
    
    def ticket_tracking(self):
        user_ticket = tickets.pop()
        print(f"Your ticket #{str(user_ticket)} in space #{user_ticket}")
        while True:    
            users_choice = input("Would you like to pay now? (y/n): ").lower()
            if users_choice == "y":
                current_ticket[f"{user_ticket}"] = True
                prep = Paid(pre_paid="", pay_later="")
                prep.pre_pay()
            elif users_choice == "n":
                current_ticket[f"{user_ticket}"] = False
                return
            else:
                print("Invald Input")
                continue        
    
    def leaving(self):
        while True:    
            user_show_ticket = input("What is your ticket number?: ").lower()
            if current_ticket[user_show_ticket] == True:    
                print("Have a nice day.")
                tickets.append(user_show_ticket)
                spaces.append(user_show_ticket)
                del current_ticket[user_show_ticket]
                return False
            elif current_ticket[user_show_ticket] == False:
                del current_ticket[user_show_ticket]
                tickets.append(user_show_ticket)
                spaces.append(user_show_ticket)
                prep2 = Paid(pre_paid="", pay_later="")
                return prep2.later_pay()
            else:
                for ticket in current_ticket.keys():
                    if ticket != int(user_show_ticket):
                        print("Invald Input")
                        continue
                    else:
                        break


    def run(self):
        while True:
            user_choice = input("Are you parking: (y/n) or quit: ").lower()                
            if user_choice == "y":
                self.space_parking()
            elif user_choice == "n":
                if len(current_ticket) == 0:
                    continue
                else:
                    self.leaving()
            elif user_choice == "quit":
                return False
            else:
                print("Invald Input")
                continue
            
    
class Paid():

    def __init__(self, pre_paid, pay_later):
        self.pre_paid = pre_paid 
        self.pay_later = pay_later

    def pre_pay(self):
        while True:
            user_choice = input("Please pay $5.00: (y/n): ").lower()
            if user_choice == "y":
                print("Ticket has been paid, you have 15min to leave.")
                back_to_run = ParkingGargage()
                back_to_run.run()
            elif user_choice == "n":
                continue
            else:
                print("Invald Input")
                continue

    def later_pay(self):
        while True:
            user_choice = input("Please pay $5.00: (y/n): ").lower()
            if user_choice == "y":
                print("Have a nice day.")
                back_to_run = ParkingGargage()
                back_to_run.run()
            elif user_choice == "n":
                continue
            else:
                print("Invald Input")
                continue

new_customer = ParkingGargage()
new_customer.run() 
    
