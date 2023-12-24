from flask import Flask

from app.domain.models import db
from app.ports.routes import api_bp
from app.config import DevelopementConfig

app = Flask(__name__)

app.config.from_object(DevelopementConfig)

db.init_app(app)

# create database 
with app.app_context():
    db.create_all()

# Registre o Blueprint com as rotas da API
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)