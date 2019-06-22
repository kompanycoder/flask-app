from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(150), unique=True, nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.id


@app.route('/', methods=['GET', 'POST'])
def Index():
    if request.method == 'POST':
        if request.form['todo'] != '':
            itemcontent = request.form['todo']
            newitem = Item(content=itemcontent)
        else:
            return 'Please input a task..'

        try:
            db.session.add(newitem)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error creating new item in db'
    else:
        items = Item.query.order_by(Item.date_created).all()
        return render_template('index.html', items=items)


if __name__ == "__main__":
    app.run(debug=True)
