# find the number in 1 and 100 which cannot be divided by 7 or does not include number 7
for n in range(1, 101):
    if (n%10)==7 or (n//10)==7 or (n%7)==0:
        continue
    else:
        print(n)
    
