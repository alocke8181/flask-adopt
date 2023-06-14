from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf


class New_Pet(FlaskForm):
    """Form for creating new pets"""
    name = StringField('Name', validators=[InputRequired()])

    species = StringField('Species', validators=[InputRequired(), AnyOf(['Cat','Dog','Porcupine'])])

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])

    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])

    notes = TextAreaField('Notes', render_kw = {'rows':5, 'cols':50})

    available = BooleanField('Available')
    
class Edit_Pet(FlaskForm):
    """Form for editing existing pets"""
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])

    notes = TextAreaField('Notes', render_kw = {'rows':5, 'cols':50})

    available = BooleanField('Available')
