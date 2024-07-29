import pytest
from db.mysql_repository import MySQLRepository

@pytest.fixture(scope="module")
def mysql_repo():
    # Set up the MySQLRepository instance
    repo = MySQLRepository()
    yield repo
    del repo  # Clean up after tests

def test_load_tarot_cards(mysql_repo):
    # Test that we can load tarot cards from the database
    tarot_cards = mysql_repo.load_tarot_cards()
    
    # Verify that the expected cards are in the list
    assert len(tarot_cards) > 0  # Check that there is at least one card
    assert any(card['name'] == 'The Fool' for card in tarot_cards)
    assert any(card['name'] == 'The Magician' for card in tarot_cards)

def test_database_initialization(mysql_repo):
    # Test that the database was initialized correctly
    tarot_cards = mysql_repo.load_tarot_cards()
    
    # Check if the table was created and data was inserted
    assert len(tarot_cards) == 2  # Adjust based on how many initial cards you inserted