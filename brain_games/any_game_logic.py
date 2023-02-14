import prompt
from brain_games import cli
from brain_games.scripts import brain_games


def main(current_func, introduction):
    brain_games.greetings()
    name = cli.welcome_user()
    print(introduction)
    ROUNDS = 3
    for i in range(0, ROUNDS):
        [question, correct_answer] = current_func()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer /;(./ Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
