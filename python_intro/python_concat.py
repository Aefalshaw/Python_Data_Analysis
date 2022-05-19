# 1. TASK: print "Hello World"

print("Hello World")

# 2. TASK: print "Hello Noelle!" with the name in a variable

name = "Noelle"
print("Hello " + name) # str + str can concat but not str to int
print("Hello",name)

# 3. TASK: print "Hello 42!" with the number in a variable

num = 42
print("Hello",num,"!")	# with a comma

# 4. TASK: print "I love to eat sushi and pizza." with the foods in variables

fave_food1 = "sushi"
fave_food2 = "pizza"
print("I like to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print("I like to eat {0} and {1}.".format(fave_food1, fave_food2))
print("I like to eat {food1} and {food2}.".format(food1=fave_food1, food2=fave_food2))

print(f"I like to eat {fave_food1} and {fave_food2}.") # with an f string

# Appending the same string to a string can be done using the * operator, as follows:
# str=str * x
# Where x is the number of times string str is appended to itself.

str1="Hi. "
str2="Oh, hi! "
str3=str1+str2
str3=str3*3
print(str3)