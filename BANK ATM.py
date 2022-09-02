# SIMULATE A BANK ATM
# ENTER 4 DIGIT PIN
# TO DO: BALANCE CHECK , MAKE WITHDRAWL , DEPOSIT Money, Reset ATM Pin, Pay Income tax

print("WELCOME TO OUR BANK ATM\n")
correct_pin=1234
restart=('yes')
chances=5
balance=20000
exit="no"

while(chances>=0):
    if (exit=="yes"):
        break
    else:
       pin=int(input("enter your pin: "))
       if (pin==(correct_pin)):
          print("You enter correct pin\n")
          restart='yes'

          while restart not in ('n','no','N','NO'):
            print("WELCOME TO THE ATM MAIN MENU \n")
            print("Press any of below options\n")
            print("Press 1 for balance check\n")
            print("Press 2 for withdrawl \n")
            print("Press 3 for money deposit\n")
            print("Press 4 to reset your ATM pin\n")
            print("Press 5 to pay your income tax\n")
            print("Press 6 to get back the , ATM card\n")
            print("Press 7 to exit the BANK ATM ASAP\n")

            option=int(input("Enter you choice: "))

            if(option==1):
                print("your balance is ",balance,'\n')
                restart=input("Would you like to go back to the main MENU?")
                if restart in('N','NO','n','no'):
                    print("THANK YOU\n")
                    break

            elif(option==2):
                if(balance>0):
                    print("Now Your balance is",balance,'\n')
                    withdraw=float(int(input("Enter amount to withdraw\n")))
                    if(withdraw<=balance):
                            balance=balance-withdraw
                            print("Your balance is",balance,'\n')
                            restart=input("Would you like to go back to the main MENU?")
                            if restart in('N','NO','n','no'):
                                print("THANK YOU\n")
                                break
                    else:
                        print("Enter amount that can be withdrawn according to the balance\n")
                else:
                    print("No balance left\n")
                    print("BALANCE is zero\n")
                    print("Please deposit money asap\n")
                    
            elif(option==3):
                pay=float(int(input("Enter amount to deposit\n")))
                balance+=pay
                print("Your balance is",balance,'\n')
                restart=input("Would you like to go back to the main MENU?")
                if restart in('N','NO','n','no'):
                        print("THANK YOU\n")
                        break

            elif(option==4):
                print("Please enter the pin you remember: ")
                old_pin=int(input())
                if(old_pin==correct_pin):
                  print("RESETTING ATM PIN")
                  new_pin=int(input("Plaese enter your new 4 digit pin: "))
                  correct_pin=new_pin
                  print("PIN RESET\n")
                  restart=input("Would you like to go back to the main MENU?")
                  if restart in('N','NO','n','no'):
                        print("THANK YOU\n")
                        break
                else:
                    print("You have to give a fine of 5000 Rs. to reset pin")
                    balance-=5000.0
                    print("Your balance is",balance,'\n')
                    print("RESETTING ATM PIN")
                    new_pin=int(input("Plaese enter your new 4 digit pin: "))
                    correct_pin=new_pin
                    print("PIN RESET\n")
                    restart=input("Would you like to go back to the main MENU?")
                    if restart in('N','NO','n','no'):
                        print("THANK YOU\n")
                        break

            elif(option==5):
                print("PAYING INCMOE TAX")
                tax=(balance*30)/100
                balance-=tax
                print("Successfully paid",tax,"Rupees of income tax")
                print("Now Your balance is",balance,'\n')
                restart=input("Would you like to go back to the main MENU?")
                if restart in('N','NO','n','no'):
                        print("THANK YOU\n")
                        break

            elif(option==6):
                print("Please wait while your card is returned back\n")
                print("Thank YOU \n")
                break

            elif(option==7):
                exit="yes"
                break
        

            else:
                print("Please enter correct option\n")
                restart='yes'

       elif(pin!=(correct_pin)):
          print("Incorrect pin")
          chances-=1
          if(chances==0):
            print("Chances OVER\n")
            break


print("\n")
print("Thank you for using our ATM \n")
print("Please provide your feedback \n")
rating=float(input("Give rating out of 10\n"))
print("********",rating,"*******")