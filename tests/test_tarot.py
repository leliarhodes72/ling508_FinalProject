from app.tarot import *

def test_tarot_card():
    card = TarotCard(id = 0,
                     name = "The Fool",
                     description = "The Fool depicts a youth walking joyfully into the world. He is taking his first steps, and he is exuberant, joyful, excited. He carries nothing with him except a small sack, caring nothing for the possible dangers that lie in his path. Indeed, he is soon to encounter the first of these possible dangers, for if he takes just a step more, he he topple over the cliff that he is reaching. But this doesn't seem to concern him - we are unsure whether he is just naive or simply unaware. The dog at his heels barks at him in warning, and if he does not become more aware of his surroundings soon, he may never see all the adventures that he dreams of encountering.",
                     upright_meaning = "beginnings, freedom, innocence, originality, adventure, idealism, spontaneity",
                     reversed_meaning = "reckless, careless, distracted, naive, foolish, gullible, stale, dull",
                     numerology = "0 - infinity, limitless potential, nothing",
                     element = "air",
                     astrological_body = "Uranus")
    assert card.id == 0
    assert card.name == "The Fool"
    assert card.element == "air"
    assert card.description == "The Fool depicts a youth walking joyfully into the world. He is taking his first steps, and he is exuberant, joyful, excited. He carries nothing with him except a small sack, caring nothing for the possible dangers that lie in his path. Indeed, he is soon to encounter the first of these possible dangers, for if he takes just a step more, he he topple over the cliff that he is reaching. But this doesn't seem to concern him - we are unsure whether he is just naive or simply unaware. The dog at his heels barks at him in warning, and if he does not become more aware of his surroundings soon, he may never see all the adventures that he dreams of encountering."
    assert card.upright_meaning == "beginnings, freedom, innocence, originality, adventure, idealism, spontaneity"
    assert card.reversed_meaning == "reckless, careless, distracted, naive, foolish, gullible, stale, dull"
    assert card.numerology == "0 - infinity, limitless potential, nothing"
    assert card.astrological_body == "Uranus"

def test_meaning():
    upright = Meaning(id = 100,
                      text = "beginnings, freedom, innocence, originality, adventure, idealism, spontaneity")
    reversed = Meaning(id = 200,
                       text = "reckless, careless, distracted, naive, foolish, gullible, stale, dull")
    assert upright.id == 100
    assert upright.text == "beginnings, freedom, innocence, originality, adventure, idealism, spontaneity"
    assert reversed.id == 200
    assert reversed.text == "reckless, careless, distracted, naive, foolish, gullible, stale, dull"

def test_astrological_body():
    body = AstrologicalBody(id = 8,
                            name = "Uranus",
                            significance = "Eccentricity, Unpredictable Changes, Rebellion, Reformation")
    assert body.id == 8
    assert body.name == "Uranus"
    assert body.significance == "Eccentricity, Unpredictable Changes, Rebellion, Reformation"

def test_element():
    element = Element(id = 4,
                      name = "Air",
                      significance = "logic, ideas, intellect, communication, conflict, awareness, perception")
    assert element.id == 4
    assert element.name == "Air"
    assert element.significance == "logic, ideas, intellect, communication, conflict, awareness, perception"

def test_keyword():
    key = Keyword(id = 0,
                  word = "risk")
    assert key.id == 0
    assert key.word == "risk"

def test_numerology():
    num = Numerology(number = 0,
                     significance = "infinity, limitless potential, nothing")
    assert num.number == 0
    assert num.significance == "infinity, limitless potential, nothing"
