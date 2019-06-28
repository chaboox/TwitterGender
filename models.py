from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, TextAreaField, SelectField, RadioField, BooleanField
from wtforms.validators import Length, Email, InputRequired
from wtforms.widgets import ListWidget, CheckboxInput
from mymodel import lr_predict

# Form ORM
class QuizForm(FlaskForm):
        essay_question = TextAreaField('Who do you think won the console wars of 1991, Sega Genesis or Super Nintendo? (2048 characters)', validators=[InputRequired(),Length(max=2047)] )
        email_addr = TextField('Enter Your Email', validators=[InputRequired(), Email()])
        email_addr2 = TextField('Enter Your Email2', validators=[InputRequired(), Email()])
        language = SelectField(
        'Langage',
        choices=[('fr', 'Francais'), ('ar', 'Arabe')])
        algo = SelectField(
        'Algorithme',
        choices=[('lr', 'Logistic Regression'), ('svc', 'SVC'), ('nb', 'Naive Bayes'), ('rf', 'Random Forest'), ('knn', 'KNN'), ('ada', 'AdaBoost'), 
                 ('gb', 'Gradient Boost'), ('xgb', 'XGBoost'), ('st', 'Stacking'), ('vt', 'Voting')])
        radio =  RadioField('Label', choices=[('value','description'),('value_two','whatever')])
        asc = BooleanField("Suppression des caractères ascii", default = False)
        html_m = BooleanField("Suppression des Markup HTML", default = False)
        special = BooleanField("Suppression des caractères spéciaux", default = False)
        double_space = BooleanField("Suppression des doubles espaces", default = False)
        url_ = BooleanField("Suppression des URLs", default = False)
        emo = BooleanField("Suppression des émoticones 🙁", default = False)
        minuscul = BooleanField("Minuscule", default = False)
        stop_words = BooleanField("Suppression des Stop Words", default = False)
        stemmer = BooleanField("Lemmatisation", default = False)
        cross_b = BooleanField("Cross validation", default = False)
        min_number = TextField('Nombre de mot minimal d\'un tweet', validators=[InputRequired()])
        cross_ = TextField('Nombre de folds')
        split = TextField('Split', validators=[InputRequired()])
        submit = SubmitField('Submit')
        

class BotForm(FlaskForm):
        essay_question = TextAreaField('Who do you think won the console wars of 1991, Sega Genesis or Super Nintendo? (2048 characters)', validators=[InputRequired(),Length(max=2047)] )
        email_addr = TextField('Enter Your Email', validators=[InputRequired(), Email()])
        email_addr2 = TextField('Enter Your Email2', validators=[InputRequired(), Email()])
        language = SelectField(
        'Langage',
        choices=[('fr', 'Francais'), ('ar', 'Arab')])
        algo = SelectField(
        'Algorithme',
        choices=[('lr', 'Logistic Regression'), ('svc', 'SVC'), ('nb', 'Naive Bayes'), ('rf', 'Random Forest'), ('knn', 'KNN'), ('ada', 'AdaBoost'), 
                 ('gb', 'Gradient Boost'), ('xgb', 'XGBoost'), ('st', 'Stacking'), ('vt', 'Voting')])
        time= TextField('Durée de la collecte', validators=[InputRequired()])
    
        submit = SubmitField('Submit')
        
class unique_f(FlaskForm):
        essay_question = TextAreaField('Who do you think won the console wars of 1991, Sega Genesis or Super Nintendo? (2048 characters)', validators=[InputRequired(),Length(max=2047)] )
        email_addr = TextField('Enter Your Email', validators=[InputRequired(), Email()])
        email_addr2 = TextField('Enter Your Email2', validators=[InputRequired(), Email()])
        language = SelectField(
        'Langage',
        choices=[('fr', 'Francais'), ('ar', 'Arab')])
        algo = SelectField(
        'Algorithme',
        choices=[('lr', 'Logistic Regression'), ('svc', 'SVC'), ('nb', 'Naive Bayes'), ('rf', 'Random Forest'), ('knn', 'KNN'), ('ada', 'AdaBoost'), 
                 ('gb', 'Gradient Boost'), ('xgb', 'XGBoost'), ('st', 'Stacking'), ('vt', 'Voting')])
        tweet = TextField('Entrez votre tweet', validators=[InputRequired()])
    
        submit = SubmitField('Submit')
        
class Dataset(FlaskForm):
       
        language = SelectField(
        'Langage',
        choices=[('fr', 'Francais'), ('ar', 'Arabe'), ('en', 'Anglais'), ('es', 'Espagnol'), ('de', 'Allemand')])
        typef = SelectField(
        'Format',
        choices=[ ('xlsx', 'xlsx'), ('json', 'Json')])
        
        asc = BooleanField("Suppression des caractères ascii", default = False)
        html_m = BooleanField("Suppression des Markup HTML", default = False)
        special = BooleanField("Suppression des caractères spéciaux", default = False)
        double_space = BooleanField("Suppression des doubles espaces", default = False)
        url_ = BooleanField("Suppression des URLs", default = False)
        emo = BooleanField("Suppression des émoticones 🙁", default = False)
        minuscul = BooleanField("Minuscule", default = False)
        stop_words = BooleanField("Suppression des Stop Words", default = False)
        stemmer = BooleanField("Lemmatisation", default = False)
        cross_b = BooleanField("Cross validation", default = False)
        manname = TextField('Prenoms d\'hommes', validators=[InputRequired()])
        cross_ = TextField('Nombre de folds')
        womenname = TextField('Prenoms de femmes', validators=[InputRequired()])
        min_number = TextField('Nombre de mot minimal d\'un tweet', validators=[InputRequired()])
        time= TextField('Durée de la collecte', validators=[InputRequired()])
        submit = SubmitField('Submit')
        