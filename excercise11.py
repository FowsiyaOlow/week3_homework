#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# I have used this code to find the length of the string which gives me the output of 81
# I used the print function to see the length of the output in the terminal
# I added a string so I can easily see what the value is for
# the len function has the variable in the brackets and this is what returns the length of the Belgium variable
print("This is the length of the Belgium string:" , len(Belgium))

# this is a unicode example
# I have then used the len function to get the length of belgium
# I have then used the '*' operator as this will multipy the integer form len by the "-" string
# This will output 81 "-" all next to each other
print("-" * len(Belgium))

# I created a new variable called "Belgium_colon"
# I then used the .replace string method
# in this method I had then put the comma in the old and colon in the new
# this will print out Belgium with colons inbetween words instead of commas
Belgium_colon = Belgium.replace(",", ":")
print(Belgium_colon)

# I defined a new variable of population_belgium
# I sliced the string to get the number of the population of Belgium
# I printed the value to make sure I sliced the correct data from the string
population_belgium = Belgium[8:16]
print(population_belgium)

# Same process as previous, I sliced the string to get the population of brussels alone and printed it off
population_brussels = Belgium[26:32]
print(population_brussels)

# created a new variable called total_population
# used the + operator to add the variables together
# had to use the int function to change the variables from strings into integers
# the output will give you  11183818
total_population = int(population_belgium) + int(population_brussels)
print(total_population)



