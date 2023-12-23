from app.adapters.mtg_api import MTGApiAdapter
from app.domain.models import Card, db


class CardService:

    def __init__(self, adapter: MTGApiAdapter) -> None:
        self.adapter = adapter

    def fetch_all_cards(self):
        return self.adapter.get_all_cards()
    
    def fetch_standard_cards(self):
        return self.adapter.get_standard_english_cards()
    
    def save_cards_to_database(self):
        cards_data = self.adapter.get_all_cards()
        for card_data in cards_data:
            card = Card(**card_data)
            db.session.add(card)
        db.session.commit()