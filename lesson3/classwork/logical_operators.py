age = int(input ("How old are you?"))
has_ticket = input("Do you have a movie ticket? (yes/no)")
if age >= 13 and has_ticket == "yes":
    print ("You can enter the PG-13 movie")
else: 
    print ("Sorry, you cannot enter")
print ("movie check complete.")
has_pass = input("Do you have a bus pass? (yes/no)") 
has_coins = input("Do you have coins? (yes/no)")
if has_pass == "yes" or has_coins == "yes":
    print ("You can ride the bus!")
else:
    print ("Sorry, sucker! You gotta walk.")
print ("Bus check complete.")