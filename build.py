from website import create_app
from flask_frozen import Freezer

app = create_app()
freezer = Freezer(app)

if __name__ == '__main__':
    # Generate the static files using Frozen-Flask
    freezer.freeze()
