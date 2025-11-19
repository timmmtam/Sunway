#Stimulate bomb countdown
import time

timer = int(input("How many seconds will the bomb explode in?: "))
i = 0

while (i < timer):
    time.sleep(1)
    i += 1
    print(i)
else:
    print ("BOOM")