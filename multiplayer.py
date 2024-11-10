with open(hangman_functions.py):


def multiplayer_game(file_name, num_players):
    word_list =[]
    word_to_guess = random.choice(word_list)
    letters_guessed = []
    players_scores = {f"Player {i+1}": 0 for i in range(num_players)}
    current_player_index = 0
    max_turns = 6 
    turns_left = max_turns * num_players
    
    print("Game Started!")
    print(f"Word to guess has {len(word_to_guess)} letters.")

    #Sets up the game to have two players play
  
    while turns_left > 0:
        current_player = f"Player {current_player_index + 1}"
        print(f"\n{current_player}'s turn!")
        print("Current word progress: " + display_word_progress(word_to_guess, letters_guessed))
        
        guess = input(f"{current_player}, enter a letter or guess the word: ").strip()
        
        if len(guess) == 1: 
            if user_guess_letter(guess, word_to_guess):
                print(f"Correct! {guess} is in the word.")
                add_letters_to_guess_list(guess, letters_guessed)
                players_scores[current_player] += 1
            else:
                print(f"Incorrect! {guess} is not in the word.")
        
        elif len(guess) > 1:  
            if user_guess_word(guess, word_to_guess):
                print(f"Correct! {current_player} guessed the word!")
                players_scores[current_player] += 5  
                break
            else:
                print(f"Incorrect! {guess} is not the word.")
        
        # Check if the word is fully guessed
        if set(word_to_guess.upper()) <= set(letters_guessed):
            print(f"\n{current_player} has guessed the word correctly!")
            players_scores[current_player] += 5  
            break

        # Switch player turn
        turns_left -= 1
        current_player_index = (current_player_index + 1) % num_players
        
#The above is the code that is for the main game play
    
    # Game Over: Declare winner based on scores
    print("\nGame Over!")
    winner = max(players_scores, key=players_scores.get)
    print(f"The winner is {winner} with {players_scores[winner]} points!")

# Run the multiplayer game with a word file and 2 players
multiplayer_game('words.txt', 2)
