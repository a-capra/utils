n = int(input('Enter an integer : '))

for i in range(1,n+1):
    prime = True
    for j in range(2,i):
        rem = i%j
        if rem == 0:
            prime = False
            break
    if prime:
        print('{} is prime'.format(i))

