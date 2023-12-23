from flask import jsonify

from app.domain.services import CardService
from app.adapters.mtg_api import MTGApiAdapter


class CardAPI:

    def __init__(self) -> None:
        self.adapter = MTGApiAdapter()
        self.card_service = CardService(self.adapter)

    def get_all_cards(self):
        try:
            cards = self.card_service.fetch_all_cards()
            return jsonify(cards)
        except Exception as e:
            return jsonify({"error": str(e)})
        
    def get_standard_english_cards(self):
        try:
            cards = self.card_service.fetch_standard_cards()
            return jsonify(cards)
        except Exception as e:
            return jsonify({"error": str(e)})
        