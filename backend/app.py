from flask import Flask, render_template
from api.routes import api
import os

app = Flask(__name__, static_folder="frontend", static_url_path="", template_folder="frontend")

app.register_blueprint(api)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
