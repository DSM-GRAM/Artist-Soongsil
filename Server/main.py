from flask import Flask
from flask_cors import CORS

import preprocessor


def create_app():
    app = Flask(__name__)

    CORS(app)
    preprocessor.process(app)

    return app

_app = create_app()

if __name__ == '__main__':
    _app.run(debug=True)
