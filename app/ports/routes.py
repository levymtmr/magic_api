from flask import jsonify, Blueprint

from app.domain.services import CardService
from app.adapters.mtg_api import MTGApiAdapter
from app.ports.api import CardAPI


api_bp = Blueprint('api_bp', __name__)
card_api = CardAPI()


@api_bp.route('/all-cards', methods=['GET'])
def get_all_cards():
    return card_api.get_all_cards()

@api_bp.route('/standard-cards', methods=['GET'])
def standard_cards_route():
    return card_api.get_standard_english_cards()

@api_bp.route('/update-cards', methods=['GET'])
def update_cards():
    card_service = CardService(adapter=MTGApiAdapter())
    card_service.save_cards_to_database()
    return "Cards updated successfully", 200