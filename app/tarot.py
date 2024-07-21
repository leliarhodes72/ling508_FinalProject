class TarotCard:
    def __init__(self, id, name, description, upright_meaning, reversed_meaning, numerology, element, astrological_body):
        self.id = id #int
        self.name = name #string
        self.description = description #string
        self.upright_meaning = upright_meaning #meaning
        self.reversed_meaning = reversed_meaning #meaning
        self.numerology = numerology #numerology
        self.element = element #element
        self.astrological_body = astrological_body #ast.body

    def get_meaning(self):
        return self.meaning.text

class Meaning:
    def __init__(self, id, text):
        self.id = id #to dif between meanings, fool upright == 100 rev == 200, temp upright == 1014, rev == 2014
                     #((c1 or 2 for up or rev), del0, (card number)
        self.text = text

class AstrologicalBody:
    def __init__(self, id, name, significance):
        #order:
        #Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, and Pluto.
        self.id = id
        self.name = name
        self.significance = significance
        #https://labyrinthos.co/blogs/astrology-horoscope-zodiac-signs

class Element:
    def __init__(self, id, name, significance):
        self.id = id
        self.name = name
        self.significance = significance
        #https://labyrinthos.co/blogs/learn-tarot-with-labyrinthos-academy/tarot-elements-correspondences-and-working-with-elemental-dignities?_pos=1&_sid=2115a5342&_ss=r

class Keyword:
    def __init__(self, id, word):
        self.id = id
        self.word = word

class Numerology:
    def __init__(self, number, significance):
        self.number = number
        self.significance = significance



 #def create_card(?)
        #will take data from open(file) and input create a card object with all relevant data
        #astrological body, element, etc will be enumerated and written to a file seprately, [(0, air), (1, fire), (2, earth), ...]
            #for ast.bodies, also include importance??? Why jupiter?? (FIN)
            #how will files be laid out --- play around with that
            #start getting all info

