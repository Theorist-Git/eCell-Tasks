from flask import Flask, render_template


def create_app():
    """
    Initialization of the flask app. Configures all the settings and blueprints.
    :return: app (An instance of Flask)
    """
    app = Flask(__name__)

    # Importing views and portfolio blueprints from views.py and portfolio.py resp.
    from .views import views
    # from .portfolio import portfolio

    app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(portfolio, url_prefix='/portfolio')

    # 'app.errorhandler' decorator overrides default error pages and replaces them with custom ones
    # 404 status is set explicitly.
    @app.errorhandler(404)
    def page_not_found(_):
        return render_template('404.html'), 404

    return app
