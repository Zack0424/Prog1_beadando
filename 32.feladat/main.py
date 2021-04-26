import random
STARTING_SCORE = 301

# Functions

def throws_to_end(score:int):
    throws = 0
    throw_list = sorted([value for value in dart_board.values()])
    for i in reversed(throw_list):
        if score // i >= 1:
            throws += score // i
            score = score % i
        if score ==0:
            return throws


def throw(target:str):
    choices = ["T","S","D"]
    center_throws = ["bullseye","outer_bullseye"]
    chance = random.randint(0,101)
    if chance < 51:
        return target
    elif 50 < chance < 71:
        return random.choice(list(dart_board.keys()))
    elif 70< chance < 101 and target == "bullseye" or target == "outer_bullseye":
        center_throws.remove(target)
        return center_throws[0]
    else:
        choices.remove(target[0])
        return f"{random.choice(choices)}{target[1:]}"






# Creating Dartboard
dart_board = {}
starting_points = 501

for i in range(1,21):
    dart_board[f"S{i}"] = i
    dart_board[f"D{i}"] = i * 2
    dart_board[f"T{i}"] = i * 3
dart_board["outer_bullseye"] = 25
dart_board["bullseye"] = 50
dart_board["miss"] = 0



# Main Game
throw_number = 0
game_is_on = True
score = STARTING_SCORE
while game_is_on:
    print(f"Pontok: {score}")
    print()
    print(f"Ennyi dobásból lehetne befejezni: {throws_to_end(score=score)}")
    target = input("A célpont: ")
    if target not in dart_board.keys():
        print("A beírt célpont nem érvényes, kérem próbálja újra!")

    else:
        current_throw = throw(target=target)
        print(f"Ez volt a célpont: {target}, ide érkezett: {current_throw}")
        score -= dart_board[current_throw]


        throw_number +=1

print(f"Ennyi dobásból sikerült a játék: {throw_number}")