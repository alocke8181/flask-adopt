from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional, NumberRange


class New_Pet(FlaskForm):

    name = StringField('Name', validators=[InputRequired()])

    species = StringField('Species', validators=[InputRequired()])

    photo_url = StringField('Photo URL')

    age = IntegerField('Age', validators=[NumberRange(min=0, message="Age cannot be less than 0")])

    notes = StringField('Notes')