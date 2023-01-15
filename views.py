from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@views.route('/portfolio/', methods=['GET'])
def portfolio_index():
    return render_template("portfolio.html")
