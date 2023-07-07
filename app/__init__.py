from flask import Flask, Response, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import requests
import io
import base64

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    @app.context_processor
    def my_context_processor():
        def proxy(url):

            response = requests.get(url,stream=True, proxies={"https": "https://3c5334842c52-15660798139000638402.ngrok-free.app"})
            
            # Check if the response was successful
            if response.status_code == 200:
                # Create a BytesIO object and write the content chunks to it
                content_io = io.BytesIO()
                for chunk in response.iter_content(chunk_size=1024):
                    content_io.write(chunk)
                content_io.seek(0)  # Move the file pointer to the beginning of the BytesIO object
                return base64.b64encode(content_io.getvalue())
            else:
                return None


        return {"proxy": proxy}

    app.config.from_pyfile('settings.py')
    app.config["FLASK_DEBUG"] = True
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import Admin

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .pages import page as page_blueprint
    app.register_blueprint(page_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
