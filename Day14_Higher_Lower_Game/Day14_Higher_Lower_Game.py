from game_data import data
from higherlowergame_logo import logo, vs
import random

def format_data(random_data):
    """Takes the account data from list of dictionary and returns the printable format."""
    name = random_data["name"]
    desc = random_data["description"]
    country = random_data["country"]
    return f"{name}, a {desc}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user's guess and the follower counts and returns if they got it right."""
    if (a_followers > b_followers and guess == 'A') or ( b_followers > a_followers and guess == 'B'):
        return True
    else:
        return False

print(logo)

score = 0
continue_game = True
random_b = random.choice(data)

while continue_game:
    # Get 2 random accounts from the list and show name, description and country
    random_a = random_b
    random_b = random.choice(data)

    if random_a == random_b:
        random_b = random.choice(data)

    print(f"Compare A: {format_data(random_a)}.")
    print(vs)
    print(f"Against B: {format_data(random_b)}.")

    # User should guess
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    a_follower_count = random_a["follower_count"]
    b_follower_count = random_b["follower_count"]
    is_correct = check_answer(user_answer, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        continue_game = False
