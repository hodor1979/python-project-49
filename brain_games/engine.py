import prompt
from brain_games import cli
from brain_games.scripts import brain_games
ROUNDS = 3


def main(game, description):
    brain_games.greetings()
    name = cli.welcome_user()
    print(description)
    for i in range(0, ROUNDS):
        [question, correct_answer] = game()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer /;(./ Correct answer "
                  f"was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
