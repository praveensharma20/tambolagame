import random

def players(n):
    play = []
    for i in range(n):
        nums = list(map(int, input(f"Player-{i+1} think/enter your 5  random numbers with in range 1-20").split()))
        play.append(nums)
    return play


def CreateTicket():
    return random.sample(range(1, 21), 5)


def count_matches(players, revealed):
    scores = []
    for p in players:
        match = 0
        for num in p:
            if num in revealed:
                match += 1
        scores.append(match)
    return scores


def declare_winner(scores):
    max_score = max(scores)
    winners = []

    for i in range(len(scores)):
        if scores[i] == max_score:
            winners.append(i + 1)

    if max_score == 5:
        print("\n PERFECT MATCH WINNER:", winners)
    else:
        print("\n MAX MATCH WINNER:", winners, "with", max_score, "matches")


while True:

    n = int(input("\nEnter number of players: "))
    play = players(n)

    ticket = CreateTicket()
    print("\nTicket generated (hidden)")

    input("\nPress Enter to START REVEALING numbers...")

    revealed = []

    for num in ticket:
        input("Press Enter to reveal next number...")
        revealed.append(num)
        print(" Revealed:", num)

    print("\nAll numbers revealed:", revealed)

    ask = input("\nReveal winner now? (yes/no): ").lower()

    if ask == "yes":
        scores = count_matches(play, revealed)
        print("Matches per player:", scores)
        declare_winner(scores)

    again = input("\nPlay again? (yes/no): ")
    if again != "yes":
        print("Thanks for playing ")
        break