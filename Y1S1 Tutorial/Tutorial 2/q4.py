#Input
total_data = int(input("Total data usage for this month(GB): "))

#Calculation
counter = 1
cost = 0
while (counter <= total_data):
    if (counter <= 10):
        cost += 15
    else:
        cost += 30
    counter += 1

#Output
print(f"Your data charges for this month is: RM{float(cost):.2f}")
