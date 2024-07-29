from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def load_tarot_cards(self):
        """Load tarot cards from the database."""
        pass

    @abstractmethod
    def initialize_database(self):
        """Initialize the database."""
        pass

    @abstractmethod
    def add_card(self, card_data):
        """Add a tarot card to the database."""
        pass

    @abstractmethod
    def get_all_cards(self):
        """Get all tarot cards from the database."""
        pass

    @abstractmethod
    def get_card(self, card_id):
        """Get a specific tarot card by ID from the database."""
        pass