import getpass
import time 
import otpatm
users = ['7722 0044 2255', '6654 2251 7876', '6763 2345 6784']
usname=['sabarish','raghavan','samuel']
pins = ['0719', '2222', '3333']
amounts = [10000, 20000, 30000]
count = 0
while True:
                user=input("ENTER ACCOUNT NUMBER OF THE USER:  ")
                if user in users:
                    for i in range(0,len(users)):
                            if user==users[i]:
                                    n=i
                            else:
                                continue
                    break
                else:
                        print("INVALID USERNAME")
while count<=3:
        pin=getpass.getpass('PLEASE ENTER PIN:  ')
        if pin.isdigit():
                if user == users[n]:
                        if pin == pins[n]:
                                break
                        else:
                                count += 1
                                print('INVALID PIN')
                                print()
        else:
                print("pin consists of 4 digits")
                count+=1
if count==3:
        print('3 unsuccessful pin attempts, exiting')
        print('your card has been blocked')
        exit()
print('LOGIN SUCCESSFUL, CONTINUE')
print(str.capitalize(usname[n]), 'welcome to ATM')
while True:
        
        response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nGreen PIN(G)  \nQuit_______(Q) \n: ').lower()
        
        valid_responses = ['s', 'w', 'l', 'p','g', 'q']
        response = response.lower()
        if response == 's':
                
                print(str.capitalize(usname[n]), 'YOU HAVE ', amounts[n],'RUPEES ON YOUR ACCOUNT.')
                
                
        elif response == 'w':
                
                cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
                
                if cash_out%10 != 0:
                        
                        print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 RUPEES NOTES')
                        
                elif cash_out >= amounts[n]:
                        
                        print('YOU HAVE INSUFFICIENT BALANCE')
                        
                else:
                        amounts[n] = amounts[n] - cash_out
                        
                        print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
                        
                        
        elif response == 'l':
                print()
                
                cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
                
                print()
                if cash_in%10 != 0:
                        
                        print('AMOUNT YOU WANT TO LODGE MUST MATCH MULTIPLES OF 10')
                        
                else:
                        amounts[n] = amounts[n] + cash_in
                        
                        print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
                        
        elif response == 'p':
                
                new_pin = str(input('ENTER A NEW PIN: '))
                
                if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
                        
                        new_ppin = str(input('CONFIRM NEW PIN: '))
                        
                        if new_ppin != new_pin:
                                
                                print('PIN MISMATCH')
                                
                        else:
                                pins[n] = new_pin
                                print('NEW PIN SAVED')
                                
                else:
                        
                        print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
        elif response == 'g':
                phoneno=int(input("ENTER YOUR MOBILE NUMBER:"))
                rphoneno=int(input("CONFIRM YOUR MOBILE NUMBER:"))
                if phoneno==rphoneno:
                    print("PLEASE WAIT")
                    time.sleep(2)
                    print("OTP IS BEING GENERATED")
                    if __name__ == "__main__":
                        passcode7=otpatm.generateOTP()
                        print("THE ONE TIME PASSWORD IS:",passcode7)
                    otp=input("ENTER THE ONE TIME PASSWORD:")
                    if otp==passcode7:
                    
                        
                        
                                npin=int(input("ENTER YOUR NEW PIN"))
                                rpin=int(input("REENTER YOUR NEW PIN"))
                                if npin==rpin:
                                        print("PIN SUCCESSFULLY CREATED")
                                else:
                                        print("PIN MISMATCH")
                                        print("RETRY")
                                        exit()
                    else:
                                print("INVALID OTP")
                                exit()
                else:
                        print("PHONE NUMBER DOES NOT MATCH")
                        print("TRY AGAIN")
                        exit()
    
    
    
                
        elif response == 'q':
            print("THANK YOU FOR USING THE ATM")
            time.sleep(3)
            exit()
        else:
                
                print('RESPONSE NOT VALID')
	

				



