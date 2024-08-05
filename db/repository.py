from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def load_tarot_cards(self):
        """Load tarot cards from the database."""
        raise NotImplementedError

    @abstractmethod
    def get_card(self, card_id):
        """Get a specific tarot card by ID from the database."""
        raise NotImplementedError