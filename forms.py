from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, Optional, NumberRange
class AddPet(FlaskForm):

    name = StringField("Pet Name",validators=[InputRequired()])
    species = SelectField("Species",choices=[("dog","Dog"),("cat","Cat"),("p","Porcupine")])
    photo_url = StringField("Photo_url", validators=[Optional(), URL()])
    age = FloatField("Age",validators=[NumberRange(min=0, max=30)])
    notes = StringField("Notes")
    available = BooleanField('Available')
    