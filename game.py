# Welcome and introduction
print("Welcome to the Adventure Game!")  
print("Your journey begins here...")

#Ask for name
player_name = input("What is your name, adventurer?")

#Personalized message
print("Welcome, " + player_name + "! Your journey begins now.")

# Use an f-string to display the same message in a more reliable way
print (f"Welcome, {player_name}! Your journey begins now.")

starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deep into the unknown...
"""
print(starting_area)

#Ask the player for the first decision
decision =input("Do you wish to take the path?(yes or no): ").lower()

#Respond based on the player's decision
if decision =="yes":
    print(f"Brave choice, {player_name}! You step onto the path and venture foward")
elif decision =="no":
    print(player_name +", you decide to wait. Perhaps courage will find you later.")
else:
    print("Confused, you stand still, unsure of what to do.")