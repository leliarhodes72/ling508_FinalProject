from common_enums import AstrologicalBody, Element, Numerology

class TarotCard:
    def __init__(self, id, name, description, upright_meaning, reversed_meaning, numerology, element, astrological_body):
        self.id = id  # int
        self.name = name  # string
        self.description = description  # string
        self.upright_meaning = upright_meaning  # meaning
        self.reversed_meaning = reversed_meaning  # meaning
        self.numerology = Numerology[numerology]  # Numerology enum
        self.element = Element[element]  # Element enum
        self.astrological_body = AstrologicalBody[astrological_body]  # AstrologicalBody enum

    def get_meaning(self):
        return self.upright_meaning.text

class Meaning:
    def __init__(self, id, text):
        self.id = id  # to differentiate between meanings, e.g., Fool upright == 100, reversed == 200
        self.text = text

class Keyword:
    def __init__(self, id, word):
        self.id = id
        self.word = word