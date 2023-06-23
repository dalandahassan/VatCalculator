import os
from art import *
from colorama import init, Fore, Back, Style
import time

init()

def type_text(text, delay=0.1):
    for char in text:
        print(Fore.YELLOW + char, end='', flush=True)  # Print the character without a newline
        time.sleep(delay)  # Introduce a delay between characters
    print()

def display_info():
    about = "This Application is not for sale. \nAny miscalculation done by the user of this app \nthe developer is not responsible for it. \nThe Vat is %15 for calculation base on Saudi Arabia.\nVersion 1.3.5\nRelease on March 14 2023\n"
    type_text(about)
    print(Fore.MAGENTA + "        Created by:         ")
    print(Fore.CYAN + text2art('Basri'))
    print(Fore.RED + 'Contact on Facebook\nBasri Dalanda\n')

def header():
    print(Fore.CYAN + text2art( 'Vat Calculator',font="small") + Style.RESET_ALL)

#This is for option 3 calculation
def calculate_net_and_vat(total_amount_with_vat):
        vat = total_amount_with_vat * .15 / 1.15
        net_amount = total_amount_with_vat - vat
        return net_amount, vat
        
        
#this is for option 1 calculation
def calculate_vat(gross_amount):
    vat = gross_amount / 1.15 * 0.15
    return vat
#ths is for opt 2
def calculate_net_amount(gross_amount):
    net_amount = gross_amount *.15
    return net_amount    

def option_one():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Back.GREEN + 'You have Entered Option 1')
    print("Calculating from Total Amount\n" + Style.RESET_ALL)
    while True:
        try:
            gross_amount = float(input("Enter Total Amount with VAT: "))
            break
        except ValueError:
            print('Invalid Input! Please Enter number only.\n')
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            vat_calculator()
    vat = calculate_vat(gross_amount)
    net_amount = gross_amount - vat
    
    print(Back.CYAN + "\n{:<20} {:<20}".format("Net Amount", "%15 Vat" + Style.RESET_ALL))
    print("{:<20.2f} {:<20.2f}\n".format(net_amount, vat))
        
         
def option_two():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Back.YELLOW + 'You have Entered Option 2')
        print("Checking Vat from First Amount\n" + Style.RESET_ALL)
        while True:
            try:
                gross_amount = float(input("Enter First Amount: "))
                break
            except ValueError:
                print('Invalid Input! Please Enter number only.\n')
            except KeyboardInterrupt:
                os.system('cls' if os.name == 'nt' else 'clear')
                vat_calculator()
        vat = calculate_net_amount(gross_amount)
        net_amount = gross_amount + vat
        
        print(Back.CYAN + "\n{:<20} {:<20}".format("%15 Vat", "Total Amount with VAT" + Style.RESET_ALL))
        print("{:<20.2f} {:<20.2f}\n".format(vat, net_amount))           
         
def option_three():

    lst = []
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Back.MAGENTA + "You have Entered Option 3.")
            print("Calculating Multiple Invoice with single Payment.\n" + Style.RESET_ALL)
            n = int(input("How many invoices do you want to enter? : "))
            print("\nENTER TOTAL AMOUNT WITH VAT.")
            if n <= 0:
                raise ValueError("Number of invoices must be positive.")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            vat_calculator()
    
    # Enter all invoices first
    for i in range(n):
        while True:
            try:
                invoice_number = i + 1
                total_amount_with_vat = float(input(f"Invoice number {invoice_number}: "))
                if total_amount_with_vat <= 0:
                    raise ValueError("Amount must be positive.")
                break
            except ValueError:
                print("Invalid input. Please enter a positive number.")
            except KeyboardInterrupt:
                os.system('cls' if os.name == 'nt' else 'clear')
                option_three()
        lst.append(total_amount_with_vat)

    # Print the invoices, net amounts, and VAT amounts in a column format
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Back.CYAN + "{:<10} {:<20} {:<20} {:<20}".format("\nInvoice", "Net Amount", "%15 Vat","Total Amount with VAT" +Style.RESET_ALL))
    for i in range(n):
        gross_amount = lst[i]
        net_amount, vat = calculate_net_and_vat(lst[i])
        print("{:<10} {:<20.2f} {:<20.2f} {:<20.2f}".format(i+1, net_amount, vat,gross_amount))

    # Calculate the sum of the numbers in the list
    total = sum(lst)
    print(f"\nTotal of All invoices with VAT: {total:.2f}")
    while True:
        try:
            bank_amount = float(input("Enter Payment Amount: "))
            break
        except ValueError:
            print('Invalid Input! Please Enter number only.\n')
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            option_three()

    dif = bank_amount - total
    if total > bank_amount :
        print(f'Amount Difference is: {Fore.RED}{dif:.2f}{Style.RESET_ALL}')
        print("Bank Payment is less.\n")
    elif total == bank_amount:
        print(Fore.YELLOW + "Bank Amount are Correct.\n" + Style.RESET_ALL)
    else :
        print(f"Amount Difference is: {Fore.GREEN}{dif:.2f}" +Style.RESET_ALL)
        print("Bank Amount is more.\n")
        
    while True:
        try:
            #print("Press " + Fore.GREEN + "Enter" + Style.RESET_ALL + " to Calculate Again or enter " + Fore.YELLOW + "'n'" + Style.RESET_ALL + " to exit:")
            #choice = input()
            choice = input("Press Enter to Calculate Again or enter 'n' to exit: ")
            if choice == '':
                option_three()
            elif choice.lower() == 'n':
                #return
                os.system('cls' if os.name == 'nt' else 'clear')
                vat_calculator()
            else:
                raise ValueError(Fore.RED + "Invalid input. Please press Enter or 'n'." + Style.RESET_ALL)
        except ValueError as e:
            print(str(e))
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            vat_calculator()
 

def vat_calculator():
    header()
    while True:
        print(Fore.CYAN + "[1]: Calculate from Total Amount")
        print("[2]: Calculate from First Amount")
        print("[3]: Calculate Multiple Invoice" + Style.RESET_ALL)
        #print("[4]: About")
        choice = input("\nEnter Option: ")
        
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            option_one()
            while True:
                try:
                    choice = input("Enter to calculate again or type 'n' to exit: ")
                    #os.system('cls' if os.name == 'nt' else 'clear')
                    if choice.lower() == 'n':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        vat_calculator()
                        break
                    elif choice != '':
                        print("Invalid choice! Press Enter to calculate again or type 'n' to exit...")
                        continue
                    else:
                        option_one()
                except KeyboardInterrupt:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    vat_calculator()
    
    #to calculate the vat from first amount  
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            option_two()
            while True:
                try:
                    choice = input("Enter to calculate again or type 'n' to exit: ")
                    #os.system('cls' if os.name == 'nt' else 'clear')
                    if choice.lower() == 'n':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        vat_calculator()
                        break
                    elif choice != '':
                        print("Invalid choice! Press Enter to calculate again or type 'n' to exit...")
                        continue
                    else:
                        option_two()
                except KeyboardInterrupt:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    vat_calculator()

        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            option_three()  

        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            display_info()
            break
            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + "Invalid Input..." + Style.RESET_ALL)
            vat_calculator()
            continue
        
    vat_calculator()
      
    
if __name__ == "__main__":
         vat_calculator()