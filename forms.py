from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf


class New_Pet(FlaskForm):

    name = StringField('Name', validators=[InputRequired()])

    species = StringField('Species', validators=[InputRequired(), AnyOf(['Cat','Dog','Porcupine'])])

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])

    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])

    notes = StringField('Notes')

    available = BooleanField('Available')
    
class Edit_Pet(FlaskForm):

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])

    notes = StringField('Notes')

    available = BooleanField('Available')
