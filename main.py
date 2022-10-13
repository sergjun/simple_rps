import random

def get_choices():
  options = ["rock", "paper", "scissors"]
  player_choice = input("Enter a choice rock, paper, scissors: ")
  computer_choice = random.choice(options)
  choices = {"player": player_choice,              "computer":     computer_choice}

  return choices

def check_win(player, computer):
  print(f"You chose {player}, the computer chose {computer}")
  winning_message = "Player win! :D"
  loosing_message = "Player Loose :("
  if player == computer:
    return "Tie! :|"
  elif player == "rock":
    if computer == "scissors":
      return winning_message
    else:
      return loosing_message
  elif player == "paper":
    if computer == "rock":
      return winning_message
    else:
      return loosing_message
  elif player == "scissors":
    if computer == "paper":
      return winning_message
    else:
      return loosing_message


choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)