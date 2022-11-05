def details(name,**data):
    print(name,data)
    print(name)
    for i,j in data.items():
        print(i,j)














import sys
sys.setrecursionlimit(2**20)
def hello():
    print("hello world ")
    hello()
hello()
print(sys.getrecursionlimit())







def sum_recursion(num):
    if num==0:
        return num
    return num+sum_recursion(num-1)












