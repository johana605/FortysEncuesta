# forms.py
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class SurveyForm(FlaskForm):
    satisfaction = IntegerField('Satisfaction', validators=[DataRequired()])
    recommendation = StringField('Recommendation', validators=[DataRequired(), Length(max=3)])
    product_type = StringField('Product Type', validators=[DataRequired(), Length(max=50)])
    comments = TextAreaField('Comments')
    submit = SubmitField('Submit')

