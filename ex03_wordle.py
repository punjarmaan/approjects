"""A closer take towards achieving Wordle!"""

__author__ = "730536657"


def contains_char(word: str, char: str) -> bool:
    """Tests whether a single character is inside a given word."""
    assert len(char) == 1

    word_length = len(word)
    i: int = 0
    
    # Cycles each index of the word to check match
    while i < word_length:
        if char == word[i]:
            return True
        i += 1
    
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Uses contains_char to create a string of emojis signifies correctness of user's guess."""
    assert len(guess_word) == len(secret_word)
    
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    guess_result = ""
    
    secret_length = len(secret_word)
    i: int = 0

    # Adds green, yellow, or white box to emoji string according to the user's guess
    while i < secret_length:
        if contains_char(secret_word, guess_word[i]) and guess_word[i] == secret_word[i]:
            guess_result += green_box
        elif contains_char(secret_word, guess_word[i]) and guess_word[i] != secret_word[i]:
            guess_result += yellow_box
        else:
            guess_result += white_box
        i += 1

    return guess_result


def input_guess(expected_len: int) -> str:
    """Continues prompting the user until receiving a guess of valid length."""
    user_guess: str = input(f"Enter a {expected_len} character word: ")

    # Keeps prompting user until their guess is of the expected length
    while len(user_guess) != expected_len:
        user_guess = input(f"That wasn't {expected_len} chars! Try again: ")
    
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Secret word and turn + guess variable initialization
    secret: str = "codes"
    secret_len = len(secret)
    turn: int = 1
    current_guess: str = ""

    # Cycles through a max of 6 turns until user guesses word correctly or runs out
    while turn <= 6 and current_guess != secret:
        print(f"=== Turn {turn}/6 ===")
        current_guess = input_guess(secret_len)
        print(emojified(current_guess, secret))
        turn += 1
    
    # Final results print (success/failure)
    if current_guess == secret:
        print(f"You won in {turn - 1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()