# forms.py
from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class SurveyForm(FlaskForm):
    satisfaction = IntegerField('Satisfacción (1-5)', validators=[DataRequired(), NumberRange(min=1, max=5)])
    recommendation = RadioField('¿Recomendarías nuestro servicio?', choices=[('Si', 'Sí'), ('No', 'No')], validators=[DataRequired()])
    product_type = SelectField('Tipo de producto', choices=[('Heladería', 'Heladería'), ('Coctelería', 'Coctelería'), ('Comidas Rápidas', 'Comidas Rápidas'), ('Pescadería', 'Pescadería'), ('Bebidas', 'Bebidas')], validators=[DataRequired()])
    comments = TextAreaField('Comentarios')
    submit = SubmitField('Enviar')