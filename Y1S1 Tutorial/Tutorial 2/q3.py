#Input
yearly_income = float(input("What is your yearly income?: "))

#Calculation
if (yearly_income <= 2500):
    tax_rate = float(0.00)
elif (yearly_income <= 10000):
    tax_rate = float(0.05)
elif (yearly_income <= 50000):
    tax_rate = float(0.15)
else:
    tax_rate = float(0.25)

tax_payable = yearly_income * tax_rate

#Output
print(f"Total tax payable: RM{tax_payable:.2f} ({int(tax_rate * 100):d}%)")
