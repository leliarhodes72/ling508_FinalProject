from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def load_tarot_cards(self) -> list:
        """Load tarot cards from the database."""
        raise NotImplementedError

    @abstractmethod
    def get_card(self, card_id: int) -> dict:
        """Get a specific tarot card by ID from the database."""
        raise NotImplementedError

    @abstractmethod
    def get_all_cards(self) -> list:
        """Get all tarot cards from the database."""
        raise NotImplementedError

    @abstractmethod
    def add_card(self, card_data: dict) -> None:
        """Add a new tarot card to the database."""
        raise NotImplementedError