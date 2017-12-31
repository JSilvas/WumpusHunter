
####Commence Wumpus Hunting 1.0.0 (Now with industrial strength wumpucides! :D)

#### Key Functions ########################################
def print_cave_map():
	"""Prints map of caves"""
	for number in cave_numbers:													#progress report
		print(number, ":", caves[number])
	print('----------')
	print("cave mapping successful")

def inventory_prep():
	"""Wumpus shopping inventory preparations"""
	shopping_list = ['Bread', 'Cheese', 'Bow and Arrow',
	'Lantern', 'Rope', 'Milk']
	print("Wumpus hunting checklist:")
	for each_item in shopping_list:
		time.sleep(1)
		print(each_item)
		if each_item == "Lantern":
			time.sleep(1)
			print("Dont't forget to light your lantern")
			print("once you're down there.")
			time.sleep(2)
	if 'Milk' in shopping_list:
		time.sleep(2)
		print("Oh good, you remembered the milk!")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print()

#### Player Interaction Functions ####
def print_location(player_location):
	"""Tell the player about where they are """
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print()
	print(cave_names[player_location])
	print("From here, you see a:")
	neighbors = caves[player_location]
	for tunnel in range(0,3):
		next_cave = neighbors[tunnel]
		print(" ", tunnel+1, "-", cave_names[next_cave])
	if wumpus_location in neighbors:
		print("I smell a wumpus!")

#### Functions For Player Actions ####
def ask_for_cave():
	""" Ask the player to choose a cave
	from their current_location. """
	player_input = input("Which cave? ")
	if player_input in ['1', '2', '3']:
		index = int(player_input) - 1
		neighbors = caves[player_location]
		cave_number = neighbors[index]
		return cave_number
	else:
		print(player_input + "?")
		print("That's not a direction that I can see!")
		return False

def ask_for_action():
	""" Find out what the player wants to do next. """
	print("What do you do next?")
	print(" m) move")
	print(" a) fire and arrow")
	action = input(">")
	if action == "m" or action == "a":
		return action
	else:
		print(action + "?")
		print("I'm not sure I know how to do that.")
		return None

def action_move():
	""" Player action to move """
	new_location = ask_for_cave()
	if new_location is None:
		return player_location
	else:
		return new_location

def action_shooting():
	""" Player action to fire arrow """
	print("Firing...")
	shoot_at = ask_for_cave()

	if shoot_at == wumpus_location:
		print("Twangggg...Aargh! You shot the mighty wumpus!")
		print("Well done, fearsome wumpus hunter!")
		return True
	elif shoot_at == False:
		return False
	else:
		print("Twanggg...clatter, clatter...")
		print("You wasted your arrow!")
		print("Empty handed, you begin the ")
		print("long trek back to your village...")
		return True

#### Misc Functions ####
def title_image():
	""" Hunt the Wumpus title ascii image """
	print("*Needs Title ASCII Image Here*")

	time.sleep(4)


#### Begin Game ############################################
import random
import time

title_image()
inventory_prep()
time.sleep(4)

#### Genereates randomized set of caves each interconnected to 3 other caves
#### from the range of 0-19
cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
	caves.append([])

unvisited_caves = list(range(0,20))												# Set up
visited_caves = [0]
unvisited_caves.remove(0)

while unvisited_caves != []:													# Main loop
	i = random.choice(visited_caves)											# Pick random cave number
	if len(caves[i]) >= 3:
		continue
	#print_cave_map()															#for dev purposes only
	next_cave = random.choice(unvisited_caves)									# Link it to an unvisited one
	caves[i].append(next_cave)
	caves[next_cave].append(i)

	visited_caves.append(next_cave)												# Mark cave as visited
	unvisited_caves.remove(next_cave)

for i in cave_numbers:															# Dig out rest of tunnels
	while len(caves[i]) < 3:
		passage_to = random.choice(cave_numbers)
		caves[i].append(passage_to)
	#print_cave_map()															#for dev purposes only

cave_names = [
	#PLACEHOLDER NAMES
	"~Arched cavern~", "~Twisty passages~", "~Dripping passages~", "~Dusty crawlspace~",
	"~Underground lake~", "~Black pit~", "~Collapsed cave~", "~Shallow pool~",
	"~Icy underground river~", "~Sandy hollow~", "~Old firepit~", "~Tree root cave~",
	"~Narrow ledge~", "~Winding steps~", "~Echoing chamber~", "~Musty cave~",
	"~Gloomy cave~", "~Low ceilinged cave~", "~Wumpus lair~", "~Ethereal chasm~"]

#print_cave_map()																#for dev purposes only


#### Randomizes Wumpus location for each play through ####
wumpus_location = random.choice(cave_numbers)
wumpus_friend_location = random.choice(cave_numbers)
player_location = random.choice(cave_numbers)
while player_location == wumpus_location:
	player_location = random.choice(cave.numbers)

#### User Interface ####
print("Welcome to Hunt the Wumpus!")
print("You can see", len(cave_numbers), "caves")
print("To play, just type the number")
print("of the cave you wish to enter next.")

while 1:
	print_location(player_location)

	action = ask_for_action()
	if action is None:
		continue

	if action == "m":
		player_location = action_move()
		if player_location == wumpus_location:
			print("Aargh! You got eaten by a wumpus!")
			#raw_input("hit enter to continue")									# Needs fix to pause text at session completion
			break

	if action == "a":
		game_over = action_shooting()
		if game_over == True:
			#raw_input("hit enter to continue")									# Needs fix to pause text at session completion
			break
