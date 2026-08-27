# 1) list of words
# 2) choose a word from the list
# 3) guess the word
# 4) 

import random
names = ["Helen", "Firouzeh", "Faezeh", "Rostam", "Yalda"]

selected_name = random.choice(names).lower()

guess_count = len(selected_name)
guessed_list= ['-']*len(selected_name)
current_guess = " ".join(guessed_list)
print(current_guess)


while guess_count > 0:
    
    guessed_char= input(f"{guess_count} times left --- Please enter a character : ")
    
    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print("You have guessed it in B4")
            else:
                for idx,char in enumerate(selected_name):
                    if char == guessed_char:
                        guessed_list[idx] = guessed_char
                current_guess = " ".join(guessed_list)
                print(f"Perfect => {current_guess}")

                if not "-" in guessed_list:
                    print("You Won!!!")
                    break
        else:
            guess_count -=1
            print(f"Wrong! => remained guesses : {guess_count}")
    
    else:
        print("Plese enter a valid character")

    #     if guessed_list== selected_name:
    #         print("Great !!! Your guess was correct")
    #         break
    #     print("Wrong guess!!! Try another word")
    #     guess_count -= 1
    # except:
    #     print("Please enter a valid data!")
    