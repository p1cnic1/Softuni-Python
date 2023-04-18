cards = input().split(" ")
n_shuffles = int(input())

top_card = cards[0]
bottom_card = cards[-1]

half = len(cards) // 2
shuffles = []

for i in range(n_shuffles):

    left_cards = []
    right_cards = []


    for index in range(1, half):
        left_cards.append(cards[index])

    for index in range(half, len(cards) - 1):
        right_cards.append(cards[index])

    for index in range(len(left_cards)):
        shuffles.append(right_cards[index])
        shuffles.append(left_cards[index])

    cards = shuffles.copy()
    cards.append(bottom_card)
    cards.insert(0, top_card)
    shuffles = []

print(cards)