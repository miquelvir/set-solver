import itertools


def main(manual=True):
    cards = []

    if manual:
        stop = ""
        while stop != "stop":
            # ask cards

            color = input("color [r, p, g]")
            while color not in ("r", "p", "g"):
                color = input("color [r, p, g]")

            fill = input("fill [b, s, d]")
            while fill not in ("b", "s", "d"):
                fill = input("fill [b, s, d]")

            number = input("number [1, 2, 3]")
            while number not in ("1", "2", "3"):
                number = input("number [1, 2, 3]")

            shape = input("shape [o, r, w]")
            while shape not in ("o", "r", "w"):
                shape = input("shape [o, r, w]")

            cards.append((color, fill, number, shape))

            stop = input("stop? [stop, other]")
    else:
        with open('data.txt', 'r') as f:
            raw_cards = f.readlines()
            for raw_card in raw_cards:
                cards.append(raw_card.strip('\n').split(','))

    # all cards are loaded in cards as tuples
    card_combinations = list(itertools.combinations(cards, 3))
    for combination in card_combinations:
        card_0 = combination[0]
        card_1 = combination[1]
        card_2 = combination[2]

        found = True
        for property_card_0, property_card_1, property_card_2 in zip(card_0, card_1, card_2):
            if property_card_0 == property_card_1 == property_card_2:
                pass  # all same, all good
            elif property_card_0 != property_card_1 and property_card_1 != property_card_2 \
                    and property_card_2 != property_card_0:
                pass   # all different, all good
            else:  # some different, some not
                found = False  # not found
                break  # no need to look other properties

        if found:
            print("found:", card_0, card_1, card_2)


if __name__ == "__main__":
    main(manual=False)
else:
    main(manual=False)
print("if no line has been printed above, no matches")
