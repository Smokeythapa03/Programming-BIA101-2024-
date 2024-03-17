x = float(input('enter first number:'))
y = float(input('enter second numbr:'))
output = 0
operation = input ('enter opration:add, substract, multiply, divide, power, celling')

if operation == 'add':
    output = x + y
    print('product:',output) 
elif operation == 'subtract':
    output = x - y
    print('product:', output)
elif operation == 'multiply':
    output = x * y
    print('product:', output)
elif operation == 'divide':
    output = x / y
    print('product:', output)
elif operation == 'power':
    output = x ** y
    print('product:', output)   
elif operation == 'ceiling':
    output = x // y
    print('product:', output)
else: 
    print('Invalid operation')





furit = ["apple", "banana", "cherry"]
for x in furit:
   print(x)
for x in "banana":
    print(x)
  
