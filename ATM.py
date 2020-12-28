from time import sleep

def password():

    pin = int(input("please, enter your Account pin: "))
    if pin == 123456789:
        print("correct Account, please wait we are fetching your data")
        sleep(2)
        return True
    else:
        print("Incorrect password, Authentication Failed!!")
        return False

def atm_start():

    balance = 0

    print("Hello, welcome to the ATM  ")
    if password():
        while True:
            print("press '1' for checking balance")
            print("press '2' for withdrawl")
            print("press '3' for Deposit")
            print("press '4' fot exiting out of the ATM ")

            choose = int(input("\nchoose which money transaction fits for your day: "))

            if choose == 1:
               print("please wait we are fetching your data...")
               sleep(2)
               print("your account is: ", balance)

            elif choose == 2:
                 withdrawl =int(input("how much money do you want to take from your account: "))
                 balance =  balance - withdrawl
                 print(f"you have successfully taken{withdrawl} money from your account ")

            elif choose == 3:
                 deposit = int(input("how much do you want to add in your account: "))
                 balance = balance + deposit
                 print(f"you have successfully added {deposit} money to your account ")

            elif choose == 4:
                 print("Thanks for using the ATM,hope you have a good day!!")
                 break

atm_start()
