import time

a = int(input("enter the time in sec : "))

for x in range(a,0,-1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times UP !!!")

NUm pad:
num_pad = ((1 , 2 ,3),
            (4 , 5 ,6),
            (7 , 8 ,9))
for rows in num_pad:
    for num in rows:
        print(num, end=" ")
    print()
