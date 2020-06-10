"""
q1 - > A local farmer wants to keep a list of the different types of animal on his farm. Create a list to
hold the values of cows, sheep, pigs, horses, chickens, goats and ducks

q2 -> Add a print statement to your code so that the program will print “chickens”, using the access by
index technique (hint – remember how list element numbering works)

q3 -> Set up a variable to store the length of the list. Find the length using an appropriate command.
(Don’t just count!)\

q4 -> The farmer has decided to stop keeping horses on the farm and keep donkeys instead. Write a
del statement to remove horses from the list (again using access by index), and append donkeys
to the list. Use a counter-controlled loop to print out all the elements of the list, using the
variable you set up in Question 3 as the stop value.
"""


#question 1
animals = ["cows","sheep","pigs","horses","chickens","goats","ducks"]

#question 2
print(animals[4])

#question 3
length_of_animals = len(animals)

#question 4
del animals[3]
animals.append("donkeys")
counter = 0
while counter < length_of_animals:
  print(animals[counter])
  counter+=1