# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
score_1 = int(input("What is your first test score?"))
score_2 = int(input ("What is your second test score?"))
if score_1 >= 50 and score_2 >= 50:
    print ("You have passed both!")
else: print ("You failed at least one.")
print ("Test scores complete.")

# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
has_lunch = input ("Did you bring lunch? (yes/no)")
has_water = input ("Did you bring water?")
if has_lunch == "yes" and has_water == "yes":
    print ("You're fully ready!")
elif has_lunch == "yes"or has_water == "yes":
    print ("You're somewhat ready.")
else:
    print ("You're not ready.")
print ("End of check for readiness.")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
num = int(input("Enter a number: "))
if num <1 or num >10:
    print ("Out of range.")
else: 
    print ("In range.")








# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
score = int(input("What is your test score?"))
if score >= 90:
    print("A")
elif score >= 80:
    print ("B")
elif score >= 70:
    print ("C")
elif score >= 60:
    print ("D")
else: 
    print ("F")



# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."



# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
num1 = int(input ("Enter a number."))
num2 = int(input ("Enter a second number."))
