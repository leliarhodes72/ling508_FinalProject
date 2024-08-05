from db.mysql_repository import MySQLRepository
from app.tarot import TarotCard

class Services:
    def __init__(self, repository: MySQLRepository):
        self.repository = repository

    def add_tarot_card(self, card: TarotCard):
        card_data = {
            'name': card.name,
            'description': card.description,
            'upright_meaning_id': card.upright_meaning,
            'reversed_meaning_id': card.reversed_meaning,
            'numerology_id': card.numerology,
            'element_id': card.element,
            'astrological_body_id': card.astrological_body,
        }
        self.repository.add_card(card_data)

    def get_all_tarot_cards(self):
        return self.repository.get_all_cards()

    def get_tarot_card_by_id(self, card_id: int):
        return self.repository.get_card(card_id)
