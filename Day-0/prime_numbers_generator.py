prime_numbers=[]

def prime_n_g(n):
    for i in range(2,n):
        if i==2 or i==3 or i==5 or i==7 or((i**2)+1)%2==0 and i%3!=0 and i%5!=0 and i%7!=0:
            prime_numbers.append(i)
    print(prime_numbers)
        

prime_n_g(int(input("Please insert a number range: ")))
