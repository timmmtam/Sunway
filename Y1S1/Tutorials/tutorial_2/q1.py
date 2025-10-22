#Input
new_videos = int(input("How many new videos do you want to rent tonight?: "))
old_videos = int(input("How many old videos do you want to rent tonight?: "))

#Calculation
new_cost = float(new_videos * 3)
old_cost = float(old_videos * 2)
total_cost = new_cost + old_cost

#Output
print(f"Your total cost for tonight is: RM{total_cost:.2f}")
