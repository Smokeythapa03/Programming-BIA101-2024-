def myfunc():#local veriables
    x = 300
    print(x)

myfunc()

#function inside a function
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
        myinnerfunc() #if it is remove it will no work as it is calling the inner fnctions
    
myfunc()

#Gobal scope
x = 300

def myfunc():
    print("Inside function",x)
myfunc()
print("Outside function",x)
print(24,x)



 

