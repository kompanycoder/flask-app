from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Item(content=''):
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h3>Hello from Flask app</h3>'


if __name__ == "__main__":
    app.run(debug=True)
