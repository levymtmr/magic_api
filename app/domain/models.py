from flask_sqlalchemy import SQLAlchemy

from typing import TypedDict, Optional, List

db = SQLAlchemy()

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    original_text = db.Column(db.Text)
    card_type = db.Column(db.String(100))
    mana_cost = db.Column(db.String(50))
    legalities = db.Column(db.JSON)
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return f'<Card {self.name}>'
    
class CardData(TypedDict):
    name: str
    original_text: Optional[str]
    card_type: str
    mana_cost: Optional[str]
    legalities: List[dict]
    image_url: Optional[str]
