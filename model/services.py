from db.mysql_repository import MySQLRepository
from app.tarot import TarotCard

class TarotService:
    def __init__(self, repository: MySQLRepository):
        self.repository = repository

    # Add this method
    def get_tarot_card_by_name(self, card_name: str):
        all_cards = self.repository.get_all_cards()
        for card in all_cards:
            if card['name'].lower() == card_name.lower():
                return card
        return None

