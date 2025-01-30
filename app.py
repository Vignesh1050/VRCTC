from flask import Flask
from flask_jwt_extended import JWTManager
from auth import auth_bp
from routes import routes_bp
from models import create_tables
from config import SECRET_KEY

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = SECRET_KEY
jwt = JWTManager(app)

create_tables()

app.register_blueprint(auth_bp)
app.register_blueprint(routes_bp)
@app.route('/')
def home():
    return "Welcome to the Railway Management API!"
if __name__ == '__main__':
    app.run(debug=True)
