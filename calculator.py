def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multi(num1,num2):
    return num1*num2
def divi(num1,num2):
    return num1/num2
def module(num1,num2):
    return num1%num2
print("select opertion")
print("a.add")
print("b.sub")
print("c.multi")
print("d.divi")
print("e.module")
while True:
    choice= input("enter choice(a/b/c/d/e):")
    if choice in ('a','b','c','d','e'):
        try:
            a=int(input("enter the first number:"))
            b=int(input("enter the second number:"))

        except:
            print("invalid input")
            continue
        if choice=='a':
            print(a,"+",b,"=",add(a,b))
        elif choice=='b':
            print(a,"-",b,"=",add(a,b))
        elif choice=='c':
            print(a,"*",b,"=",add(a,b))
        elif choice=='d':
            print(a,"/",b,"=",add(a,b))
        elif choice=='e':
            print(a,"%",b,"=",add(a,b))
    else:
        print("invalid")
