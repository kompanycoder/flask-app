from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app = pybrake.flask.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# to implement pybrake here
app.config['PYBRAKE'] = dict(
    project_id=237813,
    project_key='3ee9d6fc6b462f0dae3b37a41366e914'
)
try:
    raise ValueError('hello')
except Exception as err:
    notifier.notify(err)
    
# init db session for the whole app
db = SQLAlchemy(app)
# do something with app...

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(150), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return '<Item %r>' % self.id

# main route and add task route
@app.route('/', methods=['GET', 'POST'])
def Index():
    if request.method == 'POST':
        if request.form['todo'] != '':
            itemcontent = request.form['todo']
            newitem = Item(content=itemcontent)
            db.session.add(newitem)
            db.session.commit()
            return redirect('/')
        else:
            return 'Please input a task..'
            # add template for no input found
    else:
        items = Item.query.order_by(Item.date_created).all()
        return render_template('index.html', items=items)

# route to update task
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def Update(id):
    item = Item.query.get_or_404(id)

    if request.method == 'POST':
        item.content = request.form['todo']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error updating Task.'
    else:
        return render_template('update.html', item=item)

# route to delete
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def Delete(id):
    item = Item.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting item.'


if __name__ == "__main__":
    app.run(debug=True)
