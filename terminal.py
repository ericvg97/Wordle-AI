#Terminal things


def parse(rulesText):
    rulesSplit = rulesText.split('-')
    rules = []
    for rule in rulesSplit:
        component = rule.split('.')
        letter = component[0]
        color = component[1]
        rules += [Rule(letter, color)]

    return rules


##########################3

        rules = [
        "i.B-n.B-u.B-l.Y-a.Y",
        "s.G-t.B-o.Y-r.Y-e.B"
    ]


 rulesParsed = []
    for rule in rules:
        rulesParsed += [parse(rule)]

start = time.time()


rule = [parse(input("Enter rule\n"))]
