budget = float(input("Enter travel budget in INR: "))
rate = float(input("Enter currency exchange rate: "))
fee = float(input("Enter conversion fee percentage: "))

n = int(input("Enter number of expenses: "))

total = 0

for i in range(n):
    expense = float(input("Enter expense amount: "))
    total = total + expense

conversion = total * rate
charge = conversion * fee / 100
final_amount = conversion + charge

print("Total Foreign Expenses:", total)
print("Converted Amount:", conversion)
print("Conversion Fee:", charge)
print("Final Amount in INR:", final_amount)

if final_amount <= budget:
    print("Within Budget")
else:
    print("Budget Exceeded")