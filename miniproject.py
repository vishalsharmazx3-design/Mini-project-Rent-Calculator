'''
In this python project we will make rent calculator 

Inputs we need from the user:
1. total rent
2. food ordered
3. electricity bill
4. charge per unit

Output : total amount to be paid by the user
'''

persons = int(input("Enter the number of persons = "))
rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter your food bill = "))
electricity = int(input("Enter your electricity bill = "))
charge_per_unit = int(input("Enter the charge per unit = "))

total = rent + food + electricity + charge_per_unit

total_per_person = total / persons


print(f"Total amount to be paid by each person is: {total_per_person}")