import re
import json
import random

def display_title():
    print("🎮 Welcome to:")
    print("✊ Rock   ✋ Paper   ✌️ Scissors")
    print("Try to beat the computer. First to 3 wins!")
    print("Type 'rock' (or 'r'), 'paper' (or 'p'), or 'scissors' (or 's') to play.\n")

def get_player_name():
    name = input("Enter your name or code name: ")
    while not re.match("^[a-zA-Z0-9_]{3,15}$", name):
        print("Invalid name. Use only letters, numbers, and underscores.")
        name = input("Enter your name or code name: ")
    return name

def normalize_choice(choice):
    abbreviations = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }
    return abbreviations.get(choice, choice)

def emoji_for(choice):
    return {
        "rock": "✊",
        "paper": "✋",
        "scissors": "✌️"
    }.get(choice, "")

def get_player_choice():
    choice = input("Your move (rock/r, paper/p, scissors/s): ").strip().lower()
    choice = normalize_choice(choice)
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice.")
        choice = input("Choose rock/r, paper/p, or scissors/s: ").strip().lower()
        choice = normalize_choice(choice)
    return choice

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def play_game():
    choices_history = []
    player_wins = 0
    computer_wins = 0
    round_num = 1

    while player_wins < 3 and computer_wins < 3:
        print(f"\n🕹️ Round {round_num}")
        player = get_player_choice()
        computer = random.choice(["rock", "paper", "scissors"])
        winner = get_winner(player, computer)

        print(f"You chose: {emoji_for(player)} {player}")
        print(f"Computer chose: {emoji_for(computer)} {computer}")

        if winner == "player":
            print("✅ You win this round!")
            player_wins += 1
        elif winner == "computer":
            print("❌ You lost this round.")
            computer_wins += 1
        else:
            print("⚖️ It's a tie.")

        choices_history.append({
            "round": round_num,
            "player": player,
            "computer": computer,
            "winner": winner
        })

        round_num += 1

    return {
        "rounds": choices_history,
        "result": "Player wins!" if player_wins == 3 else "Computer wins!"
    }

def save_game(name, game_data):
    output = {
        "player": name,
        "game_result": game_data["result"],
        "rounds": game_data["rounds"]
    }
    with open("rock_paper_scissors.json", "w") as f:
        json.dump(output, f, indent=4)
    print("\n📁 Game saved to rock_paper_scissors.json")

def main():
    display_title()
    name = get_player_name()
    game_data = play_game()
    print(f"\n🏁 Final Result: {game_data['result']}")
    save_game(name, game_data)

if __name__ == "__main__":
    main()

# AI Acknowledgment:
# Portions of this code were developed with support from ChatGPT (OpenAI) as allowed under Study.com's AI usage policy.
