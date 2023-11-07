#in case i wanna use "" in a word
print ('hi, "friend"')

#ask user for their name
name = input("what's your name? ") #name is a function

#say hello to user
print ("hello, " + name) # el signo "+" es para añadir marsvariables al texto

#remove whitespace from str
name = name.strip()

#to capitalize user's name
name = name.title()

#str
print("hello, ", end="")
print(name)

#split user's name in first and last name
first, last = name.split()