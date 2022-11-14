#Day 14

from art import logo
from art import vs
from game_data import data
import random

chosen_number_1 = random.randint(0, len(data)) 

score = 0
answer = True
while answer:
  print(logo)
  #chosen_number_1 = random.randint(0, len(data))
  print("Compare A:", data[chosen_number_1]['name'], data[chosen_number_1]['description'],"from" + " " + data[chosen_number_1]['country'])
  
  print(vs)
  
  chosen_number_2 = random.randint(0, len(data)) 
  #print(chosen_number_2)
  print("Against B:", data[chosen_number_2]['name'], data[chosen_number_2]['description'],"from" + " " + data[chosen_number_2]['country'])
  
  def compare():
    if data[chosen_number_1]['follower_count'] > data[chosen_number_2]['follower_count']:
      return("A")
    else:
      return("B")
  compare()
    
  user_answer = input("Who has more followers? Type 'A' or 'B':" )
  if user_answer == compare():
       score +=1
       print(f"You're right! Current score: ", score)
       clear()
       print(f"You're right! Current score: ", score)
       chosen_number_1 = chosen_number_2
  else:
       print(f"Sorry, that's wrong. Final score:", score)
       answer = False
