def HQ9(code):
    lyrics = ("%d bottles of beer on the wall, ""%d bottles of beer.\n"
                "Take one down, pass it around, ""%d bottles of beer on the wall.")
    lyrics_1 = ("1 bottle of beer on the wall, 1 bottle of beer.\n"
                "Take one down and pass it around, no more bottles of beer on the wall.")
    template = ("No more bottles of beer on the wall, no more bottles of beer.\n"
                "Go to the store and buy some more, 99 bottles of beer on the wall.")
    if code == 'H':
        return "Hello World!"
    elif code == 'Q':
        return 'Q'
    elif code == '9':
        for i in range(99, 0, -1):
            if i > 1:
                print(lyrics % (i, i, i-1))
            elif i == 1:
                print(lyrics_1)

            print(template)
    else:
        return None

code = input()
result = HQ9(code)
print(result)

#on the sumbimition it was different I removed loop and I just made lyrics as printing all song as expecting requirement so it was shitty task
