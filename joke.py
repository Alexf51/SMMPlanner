import random


def get_random_joke():
    raw_jokes = open('jokes.txt', 'r', encoding='Utf-8').read().split('\n\n\n\n\n')

    jokes = []
    for joke in raw_jokes:
        joke = joke.strip().replace('\n\n', '\n')
        if not joke.isdigit() and len(joke) < 250:
            jokes.append(joke)

    return random.choice(jokes)
