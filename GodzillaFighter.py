import random
import time
#Importing these to be used for things like delyas of computer thinking and also to have random amounts of damage



# creates the players class which I use to represent game characters
class Player():
    def __init__(self, name):
        self.health = 100  # Initialize your own health
        self.name = name   # This establishes your name 
        self.wins = 0      # This will be used to start a wins counter

    #Function will calculate damage taken by the player use abs so we cant get things like negatives
    def calculate_damage(self, damage_amount, attacker):
        if (damage_amount > self.health):
            overkill = abs(self.health - damage_amount)
            self.health = 0
            if (overkill > 0):
                print("{0} takes damage from {1}, with {2} overkill!"
                      .format(self.name.capitalize(), attacker, overkill))
            else:
                print("{0} takes damage from {1}!"
                      .format(self.name.capitalize(), attacker))
        else:
            self.health -= damage_amount
            print("{0} takes {1} damage from {2}!"
                  .format(self.name.capitalize(), damage_amount, attacker))

    # Calculates if you use some form of healing
    def calculate_heal(self, heal_amount):
        if (heal_amount + self.health > 100):
            self.health = 100
            print("{0} heals back to full health!"
                  .format(self.name.capitalize()))
        else:
            self.health += heal_amount
            print("{0} heals for {1}!"
                  .format(self.name.capitalize(), heal_amount))

# Function to check if a given input can be converted to an integer, just so you can have a non attack, attacks etc are determined by what int you select
def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

# Function to get the user attack
def get_selection():
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("Select an attack: ")
        if (parse_int(choice) is True):
            return int(choice)
        else:
            print("The input was invalid. Please try again.")

# Function to get computer's attack selection based on health
def get_computer_selection(health):
    sleep_time = random.randrange(2, 5)  # Simulate the computer thinking time this just makes it more like a real game where the opponent has to think 
    print("....thinking....")
    time.sleep(sleep_time)

    # Decision-making for the computer's attack based on its health to give the best possible decision 
    if (health <= 35):
        result = random.randint(1, 6)
        if (result % 2 == 0):
            return 3
        else:
            return random.randint(1, 2)
    elif (health == 100):
        return random.randint(1, 2)
    else:
        return random.randint(1, 3)

# Function to play a single round of the game
def play_round(computer, human):
    game_in_progress = True
    current_player = computer

    while game_in_progress:
        if (current_player == computer):
            current_player = human
        else:
            current_player = computer

        # Display players' health
        print()
        print("You have {0} health remaining and the "
              "computer has {1} health remaining."
              .format(human.health, computer.health))
        print()

        if (current_player == human):
            # Display available attacks for the human player
            print("Available attacks:")
            print("1) Electric shock - Causes moderate damage.")
            print("2) Wild Swing of your sword - high or low damage, "
                  "depending on your luck!")
            print("3) Medical pack - Restores some amount of health.")
            move = get_selection()
        else:
            # Get the computer's attack selection
            move = get_computer_selection(computer.health)

        # Performs the selected attack or healing action
        if (move == 1):
            damage = random.randrange(18, 25)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 2):
            damage = random.randrange(10, 35)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 3):
            heal = random.randrange(18, 25)
            current_player.calculate_heal(heal)
        else:
            print ("The input was not valid. Please select a choice again.")

        # Check if the game has ended due to a player's health reaching 0
        if (human.health == 0):
            print("Sorry, you lose!")
            computer.wins += 1
            game_in_progress = False

        if (computer.health == 0):
            print("Congratulations, you beat your opponent, I knew you could do it {0}!".format(human.name.capitalize()))
            human.wins += 1
            game_in_progress = False

# Function to start the game
def start_game():
    print("Welcome to Artie's Godzilla fighter game!")

    # Create player instances for the human and computer
    computer = Player("Godzilla")
    name = input("Please enter your name: ")
    human = Player(name)

    keep_playing = True

    while (keep_playing is True):
        # Display the current score
        print("Current Score:")
        print("You - {0}".format(human.wins))
        print("Godzilla - {0}".format(computer.wins))

        # Reset players' health and play a round
        computer.health = 100
        human.health = 100
        play_round(computer, human)
        print()

        # Ask the player if they want to play another round
        response = input("Play another round? (Y/N)")
        if (response.lower() == "n"):
            break

# Start the game by calling the start_game function
start_game()
