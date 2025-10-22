#Input
time_in_seconds = int(input("What is the time in seconds?: "))

#Calculation
hours = int(time_in_seconds // 3600)
minutes = int(time_in_seconds % 3600) // 60
seconds = int(time_in_seconds % 60)

#Output
print(f"Elapsed time is: {hours:02d}:{minutes:02d}:{seconds:02d}")
