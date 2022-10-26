"""CYOA - Demon Attack! A game for demon-slaying enthusiasts."""

__author__: str = "730536657"

from random import choice, randint, sample

# Global HP and player name variable
points: int
player: str

# EMOJIs used
EXCLAMATION: str = "\U00002757"
HEART: str = "\U00002665"
SAD_FACE: str = "\U00002639"
YOU_POINTER: str = "\U0001FAF5"
DEMON_FACE: str = "\U0001F47F"
FIRE: str = "\U0001F525"


def greet() -> None:
    """Welcomes player to the game and introduces the rules."""
    global player
    # Prompts user for name
    player = input(f"Hello{EXCLAMATION} What's your {YOU_POINTER}  name? ")
    # Welcome Message
    print(f"{player}, this is Demon Attack {DEMON_FACE}{FIRE} a game where you defeat demons before letting them defeat you{EXCLAMATION}\nEvery round, you will be given three random attack choices to reduce the demon's {HEART}HP. Each attack isn't equal{EXCLAMATION}\nSome attacks do more damage than others and some attacks can flop, so choose wisely. Your opponent, the demon {DEMON_FACE}, will also have a chance to attack you with a random attack choice.\nIn Standard Mode, you start off with 100 {HEART}HP and the demon starts with 50 {HEART}HP. But in Custom Mode, you get to choose how much {HEART}HP the demon has, and it's up to you to\npick the right attacks to defeat the demon. You earn 5 points everytime you play a Standard game against a demon and 10 points for every Custom game.\nYou'll also earn points based on how many {HEART}HP you beat the demon by, but the demon can earn points by beating you too.\nGood luck and score as many points as possible, {player}{EXCLAMATION}")


def user_dmg_calc(attack: str, attack_list: list[str]) -> int:
    """Calculates damage done by user based on their chosen attack."""
    dmg: int = 0
    # First three attack choices are low-damage
    if attack in attack_list[0:3]:
        dmg = randint(1, 10)
    elif attack in attack_list[3:6]:  # Second three attacks are high-damage
        dmg = randint(15, 25)
    elif attack in attack_list[6:9]:  # Last three attacks are variable
        dmg = randint(1, 50)
    return dmg


def demon_dmg_calc(attack: str, attack_list: list[str]) -> int:
    """Calculates damage done by demon based on random attack chosen."""
    dmg: int = 0
    # First three attacks are very low-damagge
    if attack in attack_list[0:3]:
        dmg = randint(3, 8)
    elif attack in attack_list[3:6]:  # Second three attacks have an opportunity for a bit more damage
        dmg = randint(5, 20)
    elif attack in attack_list[6:9]:  # Last three attacks are variable but can be high-damage
        dmg = randint(5, 40)
    return dmg


def points_calc(points: int, loser_hp: int, winner_hp: int, rounds: int) -> int:
    """Calculates player's points for each battle win, and gives player a chance to double their points."""
    hp_difference: int = winner_hp - loser_hp
    points += hp_difference
    print(f"\nCongrats, {player}{EXCLAMATION} You successfully beat the demon {DEMON_FACE} in {rounds} rounds and earned {hp_difference} points{EXCLAMATION} Let's flip a coin for a chance to double the amount of points you earned from this battle{EXCLAMATION}\n")
    flip_opts: list[str] = ["heads", "tails"]
    user_choice: str = ""
    # Prompts user for heads or tails choice
    while user_choice not in flip_opts:
        user_choice = input(f"\n\t{player}, pick Heads or Tails: ").lower()
    flip_ans: str = choice(flip_opts)
    if user_choice == flip_ans:  # Doubles points earned that round
        points += hp_difference
        print(f"\n\tYay{EXCLAMATION} It was {flip_ans}. You just earned an additional {hp_difference} points{EXCLAMATION} ")
    else:
        print(f"\n\tSorry{EXCLAMATION} It was {flip_ans}{SAD_FACE}")
    return points


def mode() -> str:
    """Prompts user to pick a game mode and enters the selected mode."""
    global player
    global points
    standard_pts: int = 5
    custom_pts: int = 10
    mode_choice: str = ""
    # Three options/branches for user to pick from
    mode_opts: list[str] = ["standard", "custom", "exit"]
    # Keeps prompting user to pick mode option until they type a valid input
    while mode_choice not in mode_opts:
        mode_choice = input(f"\n{player}, pick a Game Mode (Standard, Custom, or Exit): ").lower()
    if mode_choice == "standard":
        points += standard_pts
        print(f"\n{player}, you just earned {standard_pts} points for choosing Standard Mode{EXCLAMATION}")
    if mode_choice == "custom":
        points += custom_pts
        print(f"\n{player}, you just earned {custom_pts} points for choosing Custom Mode{EXCLAMATION}")
    # Returns mode choice of user
    return mode_choice


def custom_mode() -> None:
    """Custom function allows user to decide difficulty of battle."""
    global points
    global player
    user_hp: int = 100
    demon_hp: int = 0

    # Custom Mode Attack Options
    custom_user_attacks: list[str] = ["chop", "scratch", "poke", "glare", "whip", "kachow", "sneak", "smash", "spray"]
    custom_demon_attacks: list[str] = ["tickle", "nudge", "hit", "pipe", "knuckle", "power", "stomp", "thrust", "push"]

    user_attack_options: list[str] = list()
    user_attack: str = ""
    demon_attack: str = ""
    
    user_attack_dmg: int = 0
    demon_attack_dmg: int = 0
    print(f"\nWelcome to Custom Mode, {player}{EXCLAMATION} You will have 100 {HEART}HP, but you {YOU_POINTER}  get to decide how much {HEART}HP the demon {DEMON_FACE} you'll slay will have. But you have the pick a {HEART}HP above 50. Choose wisely{EXCLAMATION}")
    # Keeps prompting user for demon's HP until they pick a number above 50
    while demon_hp <= 50:
        demon_hp = int(input(f"\n\tPick your demon opponent's {HEART}HP: "))
        print(f"\nLet's Get Started! You have {user_hp}{HEART}HP and the demon {DEMON_FACE} has {demon_hp}{HEART}HP")
        rounds = 0
    # Custom Game loop
    while user_hp > 0 and demon_hp > 0:
        print(f"\n\t============== Round {rounds + 1} ==============")
        user_attack_options = sample(custom_user_attacks, 3)
        user_attack = ""
        while user_attack not in user_attack_options:
            user_attack = input(f"\n{player}, choose your attack: {user_attack_options[0]}, {user_attack_options[1]}, or {user_attack_options[2]}: ").lower()

        user_attack_dmg = user_dmg_calc(user_attack, custom_user_attacks)
        
        demon_attack = choice(custom_demon_attacks)
        demon_attack_dmg = demon_dmg_calc(demon_attack, custom_demon_attacks)
        
        print(f"\nYour {user_attack} attack dealt {user_attack_dmg} {HEART} damage{EXCLAMATION} to the demon")
        demon_hp -= user_attack_dmg

        print(f"\n\tThe demon's {demon_attack} attack dealt {demon_attack_dmg} {HEART} damage to you")
        user_hp -= demon_attack_dmg

        if user_hp < 0:
            user_hp = 0
        if demon_hp < 0:
            demon_hp = 0

        print(f"\nYou have {user_hp} {HEART}HP left")
        print(f"\n\tThe demon {DEMON_FACE} has {demon_hp} {HEART}HP left")
        rounds += 1
    # Three different print options based on outcome of game
    if user_hp > demon_hp:
        points = points_calc(points, demon_hp, user_hp, rounds)
    elif demon_hp > user_hp:
        print(f"\nDarn{EXCLAMATION} The demon {DEMON_FACE} defeated you {SAD_FACE}. Better luck next time{EXCLAMATION}")
    else:
        print(f"\nWow! You {YOU_POINTER}  and the demon {DEMON_FACE} tied{EXCLAMATION} Why dont you settle it with another match{EXCLAMATION}")


def main() -> None:
    """Start point of the program, takes user through greet and mode functions."""
    global points
    global player
    points = 0
    greet()
    user_mode: str = mode()

    user_hp: int = 0
    demon_hp: int = 0
    # Standard Mode Attack Options
    standard_user_attacks: list[str] = ["slice", "cut", "slap", "punch", "kick", "flick", "headbutt", "stab", "noogie"]
    standard_demon_attacks: list[str] = ["grab", "pinch", "twist", "choke", "elbow", "thrash", "bash", "slash", "erase"]

    rounds: int = 0

    user_attack_options: list[str] = list()
    user_attack: str = ""
    demon_attack: str = ""
    
    user_attack_dmg: int = 0
    demon_attack_dmg: int = 0

    while user_mode != "exit":
        if user_mode == "standard":
            user_hp = 100
            demon_hp = 50
            rounds = 0
            # Standard Game Loop
            while user_hp > 0 and demon_hp > 0:
                print(f"\n\t============== Round {rounds + 1} ==============")
                # Samples three random attack options for user to pick from
                user_attack_options = sample(standard_user_attacks, 3)
                user_attack = ""
                # Keeps prompting user to pick an attack from the options presented
                while user_attack not in user_attack_options:
                    user_attack = input(f"\n{player}, choose your attack: {user_attack_options[0]}, {user_attack_options[1]}, or {user_attack_options[2]}: ").lower()
                # Calculates damage of chosen attack
                user_attack_dmg = user_dmg_calc(user_attack, standard_user_attacks)
                # Chooses random demon attack and calcs damage of that attack
                demon_attack = choice(standard_demon_attacks)
                demon_attack_dmg = demon_dmg_calc(demon_attack, standard_demon_attacks)

                print(f"\nYour {user_attack} attack dealt {user_attack_dmg} {HEART} damage{EXCLAMATION} to the demon")
                demon_hp -= user_attack_dmg

                print(f"\n\tThe demon's {demon_attack} attack dealt {demon_attack_dmg} {HEART} damage to you")
                user_hp -= demon_attack_dmg
                # Doesn't allow HP to fall under 0
                if user_hp < 0:
                    user_hp = 0
                if demon_hp < 0:
                    demon_hp = 0

                print(f"\nYou have {user_hp} {HEART}HP left")
                print(f"\n\tThe demon {DEMON_FACE} has {demon_hp} {HEART}HP left")
                rounds += 1
            # Three different print options based on outcome of game
            if user_hp > demon_hp:
                points = points_calc(points, demon_hp, user_hp, rounds)
            elif demon_hp > user_hp:
                print(f"\nDarn{EXCLAMATION} The demon {DEMON_FACE} defeated you {SAD_FACE}. Better luck next time{EXCLAMATION}")
            else:
                print(f"\nWow! You {YOU_POINTER}  and the demon {DEMON_FACE} tied{EXCLAMATION} Why dont you settle it with another match{EXCLAMATION}")
        elif user_mode == "custom":
            custom_mode()
        # Returns user back to main menu to play again/exit/pick a different mode
        print("\nReturning to the Main Menu...\n")
        user_mode = mode()
    # Goodbye Message
    print(f"\nThanks for playing Demon Attack {DEMON_FACE}{FIRE}, {player}. You {YOU_POINTER}  earned {points} points. Enjoy the rest of your day{EXCLAMATION}\n")
    return None


if __name__ == "__main__":
    main()