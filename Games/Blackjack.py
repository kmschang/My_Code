from random import randint


def title_message():
    print(r"|▔| |   |▔|  |▔▔   | /        T    |▔|  |▔▔  | /  ")
    print(r"|▔| |   |▔|  |     |/_        |    |▔|  |    |/_  ")
    print(r"|_| |__ | |  |__   |  \       |_T  | |  |__  |  \ ")
    print("\n" * 2)


suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
cards = [
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
]
ranks = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


def deal(num):
    n = 0
    cards = {}

    while n < num:
        random_number = randint(0, 52)

        card_suit_num = random_number // 13
        card_suit_num += 1

        if card_suit_num == 1:
            pass
        if card_suit_num == 2:
            pass
        if card_suit_num == 3:
            pass
        if card_suit_num == 4:
            pass

        card_rank_ran_num = random_number // 4
        card_rank_ran_num += 1

        if card_rank_ran_num == 1:
            pass
        if card_rank_ran_num == 2:
            pass
        if card_rank_ran_num == 3:
            pass
        if card_rank_ran_num == 4:
            pass
        if card_rank_ran_num == 5:
            pass
        if card_rank_ran_num == 6:
            pass
        if card_rank_ran_num == 7:
            pass
        if card_rank_ran_num == 8:
            pass
        if card_rank_ran_num == 9:
            pass
        if card_rank_ran_num == 10:
            pass
        if card_rank_ran_num == 11:
            pass
        if card_rank_ran_num == 12:
            pass
        if card_rank_ran_num == 13:
            pass

        cards[n] = card_rank_ran_num

        print(cards[n])

        n += 1


deal(2)
