from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
