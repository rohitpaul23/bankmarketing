from random import choices
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class MarketForm(FlaskForm):
    age = IntegerField('Age ', validators = [DataRequired()])
    job = SelectField('Job ', validators = [DataRequired()], choices = [('admin.', 'Admin'),
                                                                        ('blue-collar', 'Blue Collar'),
                                                                        ('entrepreneur', 'Entrepreneur'),
                                                                        ('housemaid', 'Housemaid'),
                                                                        ('management', 'Management'),
                                                                        ('retired', 'Retired'),
                                                                        ('self-employed', 'Self Employed'),
                                                                        ('services', 'Services'),
                                                                        ('student', 'Student'),
                                                                        ('technician', 'Technician'),
                                                                        ('unemployed', 'Unemployed'),
                                                                        ('unknown', 'Unknown')])
    marital = SelectField('Marital Status ', validators = [DataRequired()], choices = [('divorced', 'Divorced'),
                                                                                       ('married', 'Married'),
                                                                                       ('single', 'Single')])
    education = SelectField('Education ', validators = [DataRequired()], choices = [('primary', 'Primary'),
                                                                                    ('secondary', 'Secondary'),
                                                                                    ('tertiary', 'Tertiary'),
                                                                                    ('unknown', 'Unknown')])
    default = SelectField('Default ', validators = [DataRequired()], choices = [('no', 'No'),
                                                                                ('yes', 'Yes')])
    balance = IntegerField('Balance ', validators = [DataRequired()])
    housing = SelectField('Housing ', validators = [DataRequired()], choices = [('no1', 'No'),
                                                                                ('yes1', 'Yes')])
    loan = SelectField('Loan ', validators = [DataRequired()], choices = [('no2', 'No'),
                                                                          ('yes2', 'Yes')])
    contact = SelectField('Contact ', validators = [DataRequired()], choices = [('cellular', 'Cellular'),
                                                                                ('telephone', 'Telephone'),
                                                                                ('unknown', 'Unknown')])
    day = IntegerField('Day ', validators = [DataRequired(), NumberRange(min = 1, max = 31)])
    month = SelectField('Month ', validators = [DataRequired()], choices = [('jan', 'January'),
                                                                            ('feb', 'February'),
                                                                            ('mar', 'March'),
                                                                            ('apr', 'April'),
                                                                            ('may', 'May'),
                                                                            ('jun', 'June'),
                                                                            ('jul', 'July'),
                                                                            ('aug', 'August'),
                                                                            ('sep', 'September'),
                                                                            ('oct', 'October'),
                                                                            ('nov', 'November'),
                                                                            ('dec', 'December')])
    duration = IntegerField('Duration ', validators = [DataRequired()])
    campaign = IntegerField('Campaign ', validators = [DataRequired()])
    pdays = IntegerField('P-Days ', validators = [DataRequired()])
    previous = IntegerField('Previous ', validators = [DataRequired()])
    poutcome = SelectField('P-Outcome ', validators = [DataRequired()], choices = [('failure', 'Failure'),
                                                                                ('other', 'Other'),
                                                                                ('success', 'Success'),
                                                                                ('unknown', 'Unknown')])
    submit = SubmitField('SUBMIT')
                                                                                            
    
