#Step 1 
import random
import hangmanArt
import hangman_words


print(hangmanArt.logo)

#Randomly choosing a word from the word_list and assign it to a variable called chosen_word.
rand_word=random.choice(hangman_words.word_list)

#Print dashes representing the word to guess

progress_word2_list=list("_"*len(rand_word))
print(''.join(progress_word2_list))

#Initializing counters
letter_guessed=0
lives=6
end_of_game=False

while(end_of_game==False):

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

  guess=input("Guess a letter: ").lower()

#Restart Flag in each loop
  hit_flag=False
 
  for order in range(0,len(rand_word)):
    if guess == progress_word2_list[order]:
      print("Already selected, pick another")
      hit_flag=True
      break
    elif guess == rand_word[order]:
      progress_word2_list[order]=guess
      hit_flag=True

  
  
  progress_word2=''.join(progress_word2_list)
  print(progress_word2)


  if hit_flag==False:
    lives-=1
    print(hangmanArt.hangman_stages[6-lives])
    if lives == 0:
      print("You've lost :(")
      end_of_game=True
  else:
    print(hangmanArt.hangman_stages[6-lives])
    if not "_" in progress_word2:
      print("You've won! Congrats")
      end_of_game=True
  


  
