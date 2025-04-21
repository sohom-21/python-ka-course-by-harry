"""
#2. The game() function in a program lets a user play a game and returns the score as an
 integer. You need to read a file 'Hi-score.txt' which is either blank or contains the
 previous Hi-score. You need to write a program to update the Hi-score whenever the
 game() function breaks the Hi-score.
"""
# 🕹 Game Idea: Number Guessing Game:
    # Computer randomly ek number choose karega (say 1 se 10 ke beech).
    # User ko woh number guess karna hoga.
    # Har wrong guess pe -1 score ya attempt count ho sakta hai.
    # Jitni kam attempts mein sahi guess karega, utna better score (ya tu ulta bhi kar sakta hai — jitna zyada correct guess utna zyada score).
    # game() function total score return karega (e.g., 10 - number_of_attempts).

"""
#2. The game() function in a program lets a user play a game and returns the score as an
 integer. You need to read a file 'Hi-score.txt' which is either blank or contains the
 previous Hi-score. You need to write a program to update the Hi-score whenever the
 game() function breaks the Hi-score.
"""
# 🕹 Game Idea: Number Guessing Game:
    # Computer randomly ek number choose karega (say 1 se 10 ke beech).
    # User ko woh number guess karna hoga.
    # Har wrong guess pe -1 score ya attempt count ho sakta hai.
    # Jitni kam attempts mein sahi guess karega, utna better score (ya tu ulta bhi kar sakta hai — jitna zyada correct guess utna zyada score).
    # game() function total score return karega (e.g., 10 - number_of_attempts).

import random

total_score = 0

def game():
    global total_score
    computer_gen_number = random.randint(1, 60)
    number_of_attempts = 0
    print("🎮 Guess the number between 1 to 60:")
    print("🎯 Lesser attempts = Higher score!")

    def start_game(comp_num, attempts):
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            return start_game(comp_num, attempts)

        attempts += 1
        if guess == comp_num:
            print(f"✅ Correct! You took {attempts} attempts.")
            return attempts
        elif guess > comp_num:
            print(f"⬆️ Your guess {guess} is too high.")
        else:
            print(f"⬇️ Your guess {guess} is too low.")
        return start_game(comp_num, attempts)

    returned_attempts = start_game(computer_gen_number, number_of_attempts)
    score = max(0, 60 - returned_attempts + 1)
    total_score += score
    print(f"🏆 Your Score for this round: {score}")
    print(f"🎯 Total Score so far: {total_score}")

    choice = input("Want to play another round? (yes/no): ").strip().lower()
    if choice == 'yes':
        return game()  # recursive re-call for new game
    else:
        return total_score


def score_maintainer():
    try:
        with open('Hi-score.txt', 'r') as file:
            data = file.readline().strip()
            if 'Hi-score' in data:
                parts = data.split(':')
                highscore = int(parts[1].strip()) if len(parts) > 1 and parts[1].strip().isdigit() else 0
            else:
                highscore = 0
    except FileNotFoundError:
        highscore = 0
    except Exception as e:
        print(f"⚠️ Error reading file: {e}")
        highscore = 0

    new_score = game()

    if new_score > highscore:
        print(f"🔥 New High Score: {new_score}!")
        try:
            with open('Hi-score.txt', 'w') as file:
                file.write(f"Hi-score : {new_score}")
        except Exception as e:
            print(f"⚠️ Error writing file: {e}")
    else:
        print(f"🏅 No new high score. Current high score is {highscore}")


"""# score_maintainer()""" # commented out just to try Harry's code



"""Harry solution yaha neche likh raha hu aur upar wala mera sol hai"""

def game_by_harry():
    print("you are playing the game ...")
    score = random.randint(0,62)
    #fetch the hi_score
    with open('hiscore.txt') as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f'you score : {score}')
    if score > hiscore:
        #write this hiscore to the file
        with open('hiscore.txt', 'w') as f:
            f.write(str(score))

    return score

if __name__ == "__main__":
    game_by_harry()




# mera first attempt
"""

import random
total_score = 0

def game():
    global total_score
    computer_gen_number = random.randint(1,60)
    number_of_attempts =  0
    print("guess the number between 1 to 60: ")
    print("The lesser number of attempts gets the higher score !!! ")

    def start_game(computer_gen_number ,number_of_attempts):
        guess = int(input("Enter a number"))
        if guess == computer_gen_number:
            return number_of_attempts
        elif guess > computer_gen_number:
            print(f" your guess {guess} is more than the number")
            return start_game(computer_gen_number, number_of_attempts+1)
        elif guess < computer_gen_number:
            print(f" your guess {guess} is less than the number")
            return start_game(computer_gen_number, number_of_attempts+1)

    returned_attempts = start_game(computer_gen_number, number_of_attempts)
    score = max(0, 60 - returned_attempts + 1)
    total_score = total_score + score
    print(f"Your Score is {total_score}")
    choice = input('Want to play more 😎, to increase the score?? (yes/no): ')
    if choice == 'yes':
        computer_gen_number = random.randint(1, 60)
        number_of_attempts = 0
        start_game(computer_gen_number, number_of_attempts)
    return total_score

def score_maintainer():
    with open('Hi-score.txt', mode='r+') as file:
        data = file.readline()
        print(data)
        new_score = game()
        if 'Hi-score' in data:
            determine_previous = data.split()
            for i in determine_previous:
                if i.strip().isdigit():
                    highscore = int(i)
                    print(f"This is the previous HighScore {highscore}")
                else:
                    highscore = 0
            if new_score > highscore:
                file.seek(0)
                print(f'New High Score: {new_score}!')
                file.write(f'Hi-score : {new_score}')
                file.truncate()


score_maintainer()
"""