from website import create_app
from flask_frozen import Freezer

app = create_app()
freezer = Freezer(app)

if __name__ == '__main__':

    print('\033[1m', 'DEVELOPMENT SERVER', '\033[0m')
    freezer.run(debug=True, port=5000, host='0.0.0.0')
