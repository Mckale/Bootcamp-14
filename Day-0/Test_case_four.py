

def fibonnacci(0,n):
    a,b=0,1
    for i in range(0,n):
        a,b=b,a+b
        return a

print(fibonnacci(0,100))

