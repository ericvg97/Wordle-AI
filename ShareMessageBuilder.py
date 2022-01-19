from datetime import date

DAY_0 = date(2021, 6, 19)

class ShareMessageBuilder:
    def build(self, rules):
        days = (date.today() - DAY_0).days
        text = "Wordle " + str(days) + " " + str(len(rules)) + "/6\n"
        for rule in rules:
            for elem in rule:
                if elem.color == 'G':
                    text += "🟩"
                elif elem.color == 'Y':
                    text += "🟨"
                else:
                    text += "⬜"
            
            text += "\n"
        return text