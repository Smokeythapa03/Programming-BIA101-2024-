string = "Greeks"  # call by value
def test(string):
    string = "GreeksforGreeks"
    print("Inside Function:", string)
   # Driver's code
test(string)
print("Outside Function:", string)

