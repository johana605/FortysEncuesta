# app.py
from flask import Flask, render_template, redirect, url_for
from config import Config
from models import db, Survey
from forms import SurveyForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/', methods=['GET', 'POST'])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        survey = Survey(
            satisfaction=form.satisfaction.data,
            recommendation=form.recommendation.data,
            product_type=form.product_type.data,
            comments=form.comments.data
        )
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for('thank_you'))
    return render_template('survey.html', form=form)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
