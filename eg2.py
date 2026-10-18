x= int(input("Enter your first number :"))
y= int(input("Enter your second number :"))
z=input("Enter your operator (+,-,*,/) :")

def add (x,y):
    print(x+y)
    
def multiply(x,y):
    print(x*y)
    
if x > y:
    def sub(x,y):
        print(x-y)
    def division(x,y):
        print(x/y)
        
elif x < y:
    def sub(x,y):
        print(x-y)
    def division(x,y):
        print(x/y)
    
    if z=="+" :
        add(x,y)
        
    if z=="-" :
        sub(x,y)
        
    if z=="*" :
        multiply(x,y)
        
    if z=="/" :
        division(x,y)
    
    
    
