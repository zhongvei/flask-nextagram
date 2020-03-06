from app import app
from flask import render_template
from instagram_web.blueprints.users.views import users_blueprint
from instagram_web.blueprints.sessions.views import sessions_blueprint
from instagram_web.blueprints.donations.view import donations_blueprint
from instagram_web.blueprints.images.view import images_blueprint
from instagram_web.blueprints.followerfollowing.views import followerfollowing_blueprint 
from flask_assets import Environment, Bundle
from .util.assets import bundles
from models.user import User
from instagram_web.util.google_oauth import oauth

assets = Environment(app)
oauth.init_app(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(sessions_blueprint, url_prefix='/sessions')
app.register_blueprint(donations_blueprint, url_prefix='/donations')
app.register_blueprint(images_blueprint, url_prefix="/images")
app.register_blueprint(followerfollowing_blueprint, url_prefix='/followerfollowing')

@app.route("/")
def home():
    users = User().select()
    return render_template('home.html',users = users)

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 403