from flask import Flask, render_template, url_for, request, redirect

@app.route('/', methods=['GET', 'POST'])
def Index():
    if request.method == 'POST':
        if request.form['todo'] != '':
            itemcontent = request.form['todo']
            newitem = Item(content=itemcontent)
        else:
            message = 'Please input a task..'
            return  message
        except:
            return 'There was an error creating new item in db'
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

