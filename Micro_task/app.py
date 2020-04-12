################################################################################
############################INSTRUCTIONS########################################
#open terminal in atom or which ever ide u r using
#make sure u have flask and its associated libraries installed
#library list is provided in the micro_task folder
#type in terminal "python app.py"
################################################################################
################################################################################
import os
from forms import  AddForm , DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
################################################################################
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)
################################################################################
class Market(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text, nullable=False)
    item = db.Column(db.Text, nullable=False)
    review = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return 'data'+str(self.name)+str(self.item)+str(self.review)
################################################################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    form = AddForm()

    if form.validate_on_submit():
        name1 = form.name.data
        item1 = form.item.data
        review1 = form.review.data
        new_item = Market(name=name1,item=item1,review=review1)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('thankyou'))
    return render_template('add.html',form=form)

@app.route('/list')
def list_item():
    data = Market.query.all()
    a=list(data)
    return render_template('list.html',a=a)

@app.route('/delete', methods=['GET', 'POST'])
def del_item():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        del_item = Market.query.get(id)
        db.session.delete(del_item)
        db.session.commit()
        return redirect(url_for('list_item'))
    return render_template('delete.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
################################################################################
if __name__ == '__main__':
    app.run(debug=True)
