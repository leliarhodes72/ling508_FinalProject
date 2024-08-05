import pytest
from app.services import Services
from db.mysql_repository import MySQLRepository
from app.tarot import TarotCard, Meaning, Element, AstrologicalBody, Numerology

@pytest.fixture(scope="module")
def services():
    repository = MySQLRepository()
    return Services(repository)

def test_add_tarot_card(services):
    card = TarotCard(
        id=0,
        name="The Fool",
        description="The Fool depicts a youth walking joyfully into the world...",
        upright_meaning=100,
        reversed_meaning=200,
        numerology=0,
        element=Element.AIR.value,
        astrological_body=AstrologicalBody.URANUS.value
    )
    services.add_tarot_card(card)
    retrieved_card = services.get_tarot_card_by_id(card.id)
    assert retrieved_card['name'] == card.name
    assert retrieved_card['description'] == card.description

def test_get_all_tarot_cards(services):
    cards = services.get_all_tarot_cards()
    assert len(cards) > 0
    assert any(card['name'] == 'The Fool' for card in cards)

def test_get_tarot_card_by_id(services):
    card_id = 1  # Assuming this ID exists in the database
    card = services.get_tarot_card_by_id(card_id)
    assert card is not None
    assert card['id'] == card_id