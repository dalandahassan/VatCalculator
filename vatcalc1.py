import os
#this program use to help to determine the vat of each purchese
#created by Hassan Al - Basri Dalanda
def vat_calculator():
    print(" -------------------------------")
    print("| Welcome to the VAT Calculator |")
    print(" -------------------------------")
    while True:
        choice = input("\nPress V to calculate from total amount \nPress N to check the vat from first amount \nPress I to know about this App. (v/n): ")
    
    #this is to calculate from total amount of purchase
        if choice.lower() == 'v':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Calculating from Total amount\n")
            gross_amount = float(input("Enter Total amount with VAT: "))
            vat = gross_amount / 1.15 * 0.15 
            net_amount = gross_amount - vat
            print(f"First amount: {net_amount:.3f}")
            print(f"VAT amount: {vat:.3f}")
    
    #to calculate the vat from first amount  
        elif choice.lower() == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Checking Vat from First amount\n")
            gross_amount = float(input("Enter First amount: "))
            vat = gross_amount *.15
            net_amount = gross_amount + vat
            print(f"VAT amount: {vat:.3f}")
            print(f"Total amount with Vat: {net_amount:.3f}")

        elif choice.lower()== 'i':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-----------------------------")
            print("|        Created by         |")
            print("|  Hassan Al-Basri Dalanda  |")
            print("|  FB: Basri Dalanda        |")
            print("-----------------------------")
            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid choice!")
            continue
    
        choice = input("\nDo you want to continue? (y/n): ")
        if choice.lower() == 'n':
            break
        elif choice.lower() == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            vat_calculator()

vat_calculator()