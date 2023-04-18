cards = input().split(" ")

is_true = True

A = [1,2,3,4,5,6,7,8,9,10,11]
B = [1,2,3,4,5,6,7,8,9,10,11]

a_counter = 11
b_counter = 11

for i in cards:
    word,value = i.split("-")
    value_int = int(value)

    if word == "A":
        if value_int in A:
            A.remove(value_int)
            a_counter -= 1

    elif word == "B":
        if value_int in B:
            B.remove(value_int)
            b_counter -= 1

    if a_counter < 7 or b_counter < 7:
        print(f"Team A - {a_counter}; Team B - {b_counter}")
        print("Game was terminated")
        is_true = False
        break

if is_true == True:
    print(f"Team A - {a_counter}; Team B - {b_counter}")