gifts = input().split()
command = input().split()


while command[0] != "No" and command[1] != "Money":
    iterator = 0
    last_element = len(gifts)


    if command[0] == "OutOfStock":
        gift = command[1]

        for i in range(len(gifts)):
            if gift in gifts[i]:
                gifts[i] = "None"

    elif command[0] == "Required":
        gift1 = command[1]
        index1 = command[2]
        index1_as_int = int(index1)

        for i in range (len(gifts)):
            if i == index1_as_int:
                gifts[i] = gift1

    elif command[0] == "JustInCase":
        just_in_case = command[1]

        for i in range(len(gifts)):
            if i == len(gifts) - 1:
                gifts[i] = just_in_case

    command = input().split()

while 'None' in gifts:
    gifts.remove('None')

else:
    print(*gifts)
