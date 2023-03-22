import os
from art import *
#function that calculate from total amount with vat
def calculate_vat(gross_amount):
    vat = gross_amount / 1.15 * 0.15
    return vat
#function that calculate vat from first amount
def calculate_net_amount(gross_amount):
    net_amount = gross_amount *.15
    return net_amount

def multiple_input():
    
    def calculate_net_and_vat(total_amount_with_vat):
        vat = total_amount_with_vat * 15 / 115
        net_amount = total_amount_with_vat - vat
        return net_amount, vat

    lst = []
    while True:
        try:
            print("You have Entered Option 3.")
            print("Calculating Multiple Invoice with single Payment.\n")
            n = int(input("How many invoices do you want to enter? : "))
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
                total_amount_with_vat = float(input("Enter Total Amount with VAT: "))
                if total_amount_with_vat <= 0:
                    raise ValueError("Amount must be positive.")
                break
            except ValueError:
                print("Invalid input. Please enter a positive number.")
            except KeyboardInterrupt:
                os.system('cls' if os.name == 'nt' else 'clear')
                multiple_input()
        lst.append(total_amount_with_vat)

    # Print the invoices, net amounts, and VAT amounts in a column format
    os.system('cls' if os.name == 'nt' else 'clear')
    print("{:<10} {:<20} {:<20} {:<20}".format("\nInvoice", "First Amount", "VAT Amount","Total Amount with VAT"))
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
            multiple_input()

    dif = bank_amount - total
    if total > bank_amount :
        print(f"Amount Difference is: {dif:.2f}")
        print("Bank Payment is less.\n")
    elif total == bank_amount:
        print("Bank Amount are Correct.\n")
    else :
        print(f"Amount Difference is: {dif:.2f}")
        print("Bank Amount is more.\n") # this function is to calculate multiple invoice

def vat_calculator():
    
    print(text2art('Vat Calculator',font="small"))

    while True:
        print("Press --> 1: Calculate from Total Amount")
        print("Press --> 2: Calculate from First Amount")
        print("Press --> 3: Calculate Multiple Invoice")
        print("Press --> 4: About")
        choice = input("\nEnter Option: ")
        
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('You have Entered Option 1')
            print("Calculating from Total Amount\n")
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
            print(f"First Amount: {net_amount:.2f}")
            print(f"VAT Amount: {vat:.2f}\n")
    
    #to calculate the vat from first amount  
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('You have Entered Option 2')
            print("Checking Vat from First Amount\n")
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
            print(f"VAT Amount: {vat:.2f}")
            print(f"Total Amount with VAT: {net_amount:.2f}\n")

        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            multiple_input()

        elif choice == '4':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('The Vat is %15 for calculation base on Saudi Arabia.')
                    print('Version 1.3.2\nRelease on March 14 2023\n')
                    print("        Created by:         ")
                    tprint('Basri')
                    print("Contact on Facebook\nBasri Dalanda\n")

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid Input...")
            vat_calculator()
            continue
        
        choice = input("Press Enter to Continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        vat_calculator()
        if choice.lower() == 'n':
            break #this is the main
                 
vat_calculator()