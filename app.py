import json
from difflib import get_close_matches
data = json.load(open('data.json'))


def translate(word):

    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        confirm = input(
            f'Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y for yes, or N for no > ')
        confirm = confirm.lower()
        if confirm == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif confirm == 'n':
            return 'The word doesnt exist, please double check it!'
        else:
            return 'We didnt understand your entry. Please try again'
    else:
        return 'The word doesnt exist, please double check it!'


word = input('Enter Word > ')

print(translate(word))
