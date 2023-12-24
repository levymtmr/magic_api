import requests

from app.interfaces.mtg_api_interface import MTGApiInterface
from app.domain.models import CardData

class MTGApiAdapter(MTGApiInterface):

    def __init__(self) -> None:
        self.base_url = "https://api.magicthegathering.io/v1/cards"

    def get_all_cards(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            cards_data = response.json().get('cards', [])
            return [self._format_card_data(card) for card in cards_data]
        else:
            raise Exception("Error to fetch Magic api url to get all cards")
        
    def get_standard_cards(self):
        params = {
            'gameFormat': 'Standard'
        }
        response = requests.get(url=self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error to fetch Magic api url to get standard english cards")
        
    def _format_card_data(self, card_data) -> CardData:
        return CardData(
            name=card_data.get('name'),
            original_text=card_data.get('originalText'),
            card_type=card_data.get('type'),
            mana_cost=card_data.get('manaCost'),
            legalities=card_data.get('legalities'),
            image_url=card_data.get('imageUrl')
        )