fibs = [0,1]
num = input("How many fibs number do you want?")
for i in range(num-2):
    fibs.append(fibs[-1]+fibs[-2])
print fibs
