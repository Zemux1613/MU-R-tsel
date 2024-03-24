def first_rule(word):
    out = word
    if word[-1] == 'I':
        out += 'U'
    return out


def second_rule(word):
    out = word
    if len(word) > 1:
        out = word + word[1:]
    return out


def threed_rule(word):
    out = word
    if "III" in word:
        out = word.replace("III", "U")
    return out


def fourth_rule(word):
    out = word
    if "UU" in word:
        out = word.replace("UU", "")
    return out


if __name__ == '__main__':
    # 1. Wenn Sie eine Kette besitzen, deren Buchstabe I ist, können Sie am Schluß ein U zufügen
    # 2. Angenommen Sie haben Mx. Dann können Sie Ihre Sammlung Mxx zufügen.
    # 3. Wenn in einer der Ketten Ihrer Sammlung III vorkommt, können Sie eine neue Kette mit U anstelle von III bilden
    # 4. Wenn UU in einer Kette vorkommt, kann man es streichen

    vocabular = set('MI')

    steps = 0

    while not 'MU' in vocabular:
        steps += 1
        # print(f"Words: {vocabular}")
        current = vocabular.copy()
        for w in current:
            vocabular.add(first_rule(w))
            vocabular.add(second_rule(w))
            vocabular.add(threed_rule(w))
            vocabular.add(fourth_rule(w))

    print(f"MU in {steps}")
