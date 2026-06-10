from flask import Flask
from flask_cors import CORS



from controller.auth_controller import auth_bp
from persistence.db_configuration import init_db

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth_bp)

init_db()

# ── Avvio Server
if __name__ == "__main__":
    app.run(debug=True, port=5001)