from Tarot import *
from common_enums import AstrologicalBody, Element, Numerology

def test_tarot_card():
    card = TarotCard(
        id=0,
        name="The Fool",
        description="The Fool depicts a youth walking joyfully into the world. He is taking his first steps, and he is exuberant, joyful, excited. He carries nothing with him except a small sack, caring nothing for the possible dangers that lie in his path. Indeed, he is soon to encounter the first of these possible dangers, for if he takes just a step more, he will topple over the cliff that he is reaching. But this doesn't seem to concern him - we are unsure whether he is just naive or simply unaware. The dog at his heels barks at him in warning, and if he does not become more aware of his surroundings soon, he may never see all the adventures that he dreams of encountering.",
        upright_meaning="beginnings, freedom, innocence, originality, adventure, idealism, spontaneity",
        reversed_meaning="reckless, careless, distracted, naive, foolish, gullible, stale, dull",
        numerology="ONE",
        element="AIR",
        astrological_body="URANUS"
    )
    assert card.id == 0
    assert card.name == "The Fool"
    assert card.element == Element.AIR
    assert card.description == "The Fool depicts a youth walking joyfully into the world. He is taking his first steps, and he is exuberant, joyful, excited. He carries nothing with him except a small sack, caring nothing for the possible dangers that lie in his path. Indeed, he is soon to encounter the first of these possible dangers, for if he takes just a step more, he will topple over the cliff that he is reaching. But this doesn't seem to concern him - we are unsure whether he is just naive or simply unaware. The dog at his heels barks at him in warning, and if he does not become more aware of his surroundings soon, he may never see all the adventures that he dreams of encountering."
    assert card.upright_meaning == "beginnings, freedom, innocence, originality, adventure, idealism, spontaneity"
    assert card.reversed_meaning == "reckless, careless, distracted, naive, foolish, gullible, stale, dull"
    assert card.numerology == Numerology.ONE
    assert card.astrological_body == AstrologicalBody.URANUS

def test_meaning():
    upright = Meaning(id=100, text="beginnings, freedom, innocence, originality, adventure, idealism, spontaneity")
    reversed = Meaning(id=200, text="reckless, careless, distracted, naive, foolish, gullible, stale, dull")
    assert upright.id == 100
    assert upright.text == "beginnings, freedom, innocence, originality, adventure, idealism, spontaneity"
    assert reversed.id == 200
    assert reversed.text == "reckless, careless, distracted, naive, foolish, gullible, stale, dull"

def test_astrological_body():
    body = AstrologicalBody.URANUS
    assert body == AstrologicalBody.URANUS
    assert body.name == "URANUS"
    assert body.value == 8

def test_element():
    element = Element.AIR
    assert element == Element.AIR
    assert element.name == "AIR"
    assert element.value == 4

def test_keyword():
    key = Keyword(id=0, word="risk")
    assert key.id == 0
    assert key.word == "risk"

def test_numerology():
    num = Numerology.ONE
    assert num == Numerology.ONE
    assert num.name == "ONE"
    assert num.value == 1