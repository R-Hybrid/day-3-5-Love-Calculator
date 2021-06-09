# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Combining makes easier work of counting in the end
combined_string = name1 + name2
lowercase_string = combined_string.lower()

#Probably the most difficult part to figure out
t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

#Adding the values
true = t + r + u + e

l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")

love = l + o + v + e

#Needs to be an int after so we use int outside.
love_score = int(str(true) + str(love))

#What would come after 50?
if (love_score < 10) or (love_score > 90):
  print(f"Your love score is {love_score}, you go together like mentos and coke.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}") 