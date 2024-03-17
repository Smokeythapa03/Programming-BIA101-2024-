my_city = "New York"
print(type(my_city))

#single quotes have exactly
#the same use as double quotes
my_city = 'New York'
print(type(my_city))

#setting the veriable type explicity 
my_city = str("New York")
print(type(my_city))

#just adding string 

word1 = 'New '
word2 = 'York'

print(word1 + word2)
#how to select the characters
word = "Rio de Janeiro" #use index
char = word[4]
print(char)
# how to replce part of string
word.replace('Rio', "Mar")
print(word)

word = "Rio de Janeiro" # count the numbers of occurances (character)
print(word.count(' '))
 # how to repeat a strings
print(word*3)

#spilt the string
word = "Rio de Janeiro"
spilt_word = word.split(' ')#to split string whenever there is white space
spilt_word = word.split(',')
