    cases = [
        # [
        #     "a.GREEN-z.BLACK-z.BLACK-z.BLACK-z.BLACK",
        #     "awake",
        #     True
        # ],
        # [
        #     "a.GREEN-z.BLACK-z.GREEN-z.BLACK-z.BLACK",
        #     "awake",
        #     False
        # ],
        # [
        #     "a.GREEN-z.BLACK-z.GREEN-z.BLACK-z.BLACK",
        #     "awzke",
        #     True
        # ],
        # [
        #     "u.BLACK-v.BLACK-u.GREEN-l.YELLOW-a.BLACK",
        #     "zlutt",
        #     True
        # ],
        # [
        #     "a.BLACK-a.GREEN-q.BLACK-q.BLACK-q.BLACK",
        #     "pazzz",
        #     True
        # ],
        # [
        #     "a.BLACK-a.GREEN-q.BLACK-q.BLACK-q.BLACK",
        #     "azzzz",
        #     False
        # ],
        # [
        #     "a.BLACK-a.GREEN-q.BLACK-q.BLACK-q.BLACK",
        #     "qazzz",
        #     False
        # ],
    ]


    # for case in cases:
    #     if (case[2] != isValid(case[1], parse(case[0]))):
    #         print("Failed")
    #         print(case)



    rules = "a.GREEN-b.GREEN-d.BLACK-o.BLACK-e.BLACK"
    for word in words:
        if isValid(word, parse(rules)):
            print(word)