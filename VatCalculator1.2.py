import os
from art import *
def vat_calculator():
    
    print(text2art('Vat Calculator',font="small"))

    while True:
        print("Press --> 1: Calculate from Total Amount")
        print("Press --> 2: Calculate from First Amount")
        print("Press --> 3: About")
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
            vat = gross_amount / 1.15 * 0.15 
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
            vat = gross_amount *.15
            net_amount = gross_amount + vat
            print(f"VAT Amount: {vat:.2f}")
            print(f"Total Amount with VAT: {net_amount:.2f}\n")

        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('The Vat is %15 for calculation base on Saudi Arabia.')
            print('Version 1.2\nRelease on March 14 2023\n')
            print("        Created by:         ")
            tprint('Basri')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid Input...")
            vat_calculator()
            continue
        
        choice = input("Press Enter to Continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        vat_calculator()
        if choice.lower() == 'n':
            break
                 
vat_calculator()