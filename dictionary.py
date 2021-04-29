import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y or N :" %
                   get_close_matches(w, data.keys())[0])

        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]

        elif yn == "N":
            return "word doesn't exist"

        else:
            return "We didn't understand your input."

    else:
        return "Word doesn't exist. Please double check."


word = input("enter word : ")
output = print(translate(word))
print(output)
