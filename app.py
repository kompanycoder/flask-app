from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


db.session.add(User(name="Example", email="example@example.com"))
db.session.commit()
users = User.query.all()


@app.route('/')
def index():
    return 'Hello from Flask app'


if __name__ == "__main__":
    app.run(debug=True)
