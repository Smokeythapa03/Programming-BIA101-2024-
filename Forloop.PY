#for loops 
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print (x)

for x in 'banana':
    print(x)

for x in fruits:
    print(x)
    if x == 'banana':
        break

 #continue statement 
fruits =  ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)
    #range() is a sequence of number 
    for x in range (2 , 6):
        print(x)
    #increment the sequence with 3(default is 1)
        for x in range (2, 30, 3):
          print(x)
#can also add a else statement for forloops
          for x in range(6):
              print(x)
          else:
              print("Finally Finished!")


