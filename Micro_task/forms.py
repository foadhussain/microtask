from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Please Enter Your Name:')
    item = StringField('Enter the item:')
    review = StringField('Review')
    submit = SubmitField('Submit!')


class DelForm(FlaskForm):

    id = IntegerField('Enter the ID of Item to Remove:')
    submit = SubmitField('Remove data!')
