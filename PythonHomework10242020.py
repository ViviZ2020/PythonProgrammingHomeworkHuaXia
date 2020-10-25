#When I ran the program below, nothing showed up after running the program
'''
def CalculateBills(Bills, tip):

    Bills = input("Payment Amount:")    
    Tip = input("Tip Percentage:")
    Bills = int(Bills)
    Tip = float(Tip)
    tip = Bills * Tip

    print("Your payment amount is:")
    print(Bills)
    print("Your tip is:")
    print(tip)

print(CalculateBills(Bills, tip))
'''

#Program that worked for me:
Bills = input("Payment Amount(Please input without dollar sign):")    
Tip = input("Tip Percentage(Please input without percentage mark and as a decimal):")
Bills = int(Bills)
Tip = float(Tip)
tip = Bills * Tip

print("Your payment amount is:")
print(Bills)
print("Your tip is:")
print(tip)



    


