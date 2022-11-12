x=int(input("enter any number"))
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

factorial=fact(x)
print(factorial)
