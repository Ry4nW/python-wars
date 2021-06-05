def disemvowel(str):
    newStr = ""

    for i in str:

        bool = False

        for j in 'aeiou':
            if j == i.lower():
                bool = True

        if not bool:
            newStr += i

    return newStr


print(disemvowel("This website is for losers LOL!"))
