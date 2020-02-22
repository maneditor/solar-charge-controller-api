import import_env_file
import os
from flask import Flask
from router import Router
from flask_json import FlaskJSON
from flask_cors import CORS

app = Flask(__name__)
# Plug JSON into flask app
FlaskJSON(app)
# Plug CORS into application
CORS(app, resources={
    r'/api/*': {
        'origins': '*'
    }
})

# Setup routes
Router.setup(app)

if __name__ == '__main__':
    # Run Application
    app.run(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        debug=True
    )
