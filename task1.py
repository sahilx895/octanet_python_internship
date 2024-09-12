#for stopping program execution for some time
import time

print("--->Please insert Your CARD<---")
time.sleep(2)

print("please wait !!")

#for card processing
time.sleep(5)

print("---->  WELCOME SAHIL  <----")

password = 1234

#taking atm pin from user
pin = int(input("enter your atm pin--> "))

#user account balance
balance = 5000

#checking pin is valid or not 
if pin == password:
    #loop will run user get free 
    while True:

        #Showing  info to user

        print(""" 
			1 == check balance:
			2 == withdraw balance:
			3 == deposit balance:
			4 == exit!
			"""
              )

        try:    
             #taking an option from user
            option = int(input("Please enter your choise--> "))
        except:
            print("Please enter valid option !!")
        
        #for option 1        
        if option == 1:
            print(f"Your current balance is ->{balance}")
                                     
        if option == 2:

            withdraw_amount = int(input("please enter withdraw amount--> "))

            

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            

            print(f"Your updated balance is {balance}")

            

        if option == 3:

            deposit_amount = int(input("Please enter deposit amount-->"))

            balance = balance + deposit_amount

            

            print(f"{deposit_amount} is credited to your account")



            print(f"Your updated balance is {balance}")



        if option == 4:
            print("Thanks for Visiting.Have a great day !")

            break


else:
    print("Wrong pin!! Please try again")
