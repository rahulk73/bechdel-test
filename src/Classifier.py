class Charac:
    name = ""
    line = ""

    def __init__(self, name, line):
        self.name = name
        self.line = line


Lili = Charac("Lili", "Oh my Go Mark is so annoying")

Emma = Charac("Emma", "I love your tee shirt Lili")

Barbara = Charac("Barbara", "He is sososososo dumb")

Mary = Charac("Mary", "Emma you're so nice her herself. and I like your bag")

menDict = {"Mark": 5, "Jeremy": 1}
femDict = {"Sally": 4, "Selina": 8, "Bobby": 5}
hePronouns = {"he", "him", "his", "himself", "mr."}

listing = [[Mary, Emma], [Mary, Mary], [Emma, Barbara]]


def correct(all_conv):
    for x in all_conv:
        for y in x:
            data = y.line.split()
            for z in data:
                if z in menDict or z.lower() in hePronouns:
                    return False
    return True


print(correct(listing))
