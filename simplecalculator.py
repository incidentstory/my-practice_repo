print("simple calculator python program")
c=int(input("emter 1 for addition\nenter 2 for subraction\nenter 3 for multlipication\nenter 4 for divison\nenter your choice: "))
a=int(input("enter first number : "))
b=int(input("enter second number : "))

def simplecalc(x,y,z):
    if z==1:
       print("the sum is :",x+y)
    elif z==2:
        print("the answer is :",x-y)
    elif z==3:
        print("the product is :",x*y) 
    elif z==4:
        print("the product is :",x/y)
    else:
        print("enter valid input")
simplecalc(a,b,c)
