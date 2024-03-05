import random

def flames_game():
    name1 = input("Enter the 1st Name : ").lower()
    name2 = input("Enter the 2nd Name : ").lower()

    chars = []
    for char in name1:
        if char not in name2:
            chars.append(char)

    for char in name2:
        if char not in name1:
            chars.append(char)

    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    index = 0

    if len(chars) > 0:
        index = random.randint(0, len(chars) - 1)

    if len(chars) == 0 or index >= len(flames):
        index = 0

    return flames[index], name1, name2

res, name1, name2 = flames_game()
print(f" FLAMES for {name1} and {name2} is: {res}")