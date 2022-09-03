from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import MarketForm
import pandas as pd
import numpy as np
import joblib

def processedFeature(alist):
    numeric_feat = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
    newFeat = ['age', 'blue-collar', 'technician', 'self-employed', 'admin.', 'management',
       'student', 'services', 'entrepreneur', 'housemaid', 'unknown', 'unemployed', 'retired',
       'married', 'single', 'divorced', 'secondary', 'primary', 'tertiary', 'unknown1', 'no', 'yes',
       'balance', 'yes1', 'no1', 'yes2', 'no2', 'cellular', 'unknown2', 'telephone', 'day', 'apr', 
       'jun', 'jul', 'feb', 'aug', 'may', 'jan', 'nov', 'sep', 'dec', 'oct', 'mar', 
       'duration', 'campaign', 'pdays', 'previous','unknown3', 'other', 'success', 'failure']
    cat_feat = {}
    cat_feat['job'] = ['blue-collar', 'technician', 'self-employed', 'admin.', 'management',
       'student', 'services', 'entrepreneur', 'housemaid', 'unknown',
       'unemployed', 'retired']
    cat_feat['marital'] = ['married', 'single', 'divorced']
    cat_feat['education'] = ['secondary', 'primary', 'tertiary', 'unknown1']
    cat_feat['default'] = ['no', 'yes']
    cat_feat['housing'] = ['yes1', 'no1']
    cat_feat['loan'] = ['yes2', 'no2']
    cat_feat['contact'] = ['cellular', 'unknown2', 'telephone']
    cat_feat['month'] = ['apr', 'jun', 'jul', 'feb', 'aug', 'may', 'jan', 'nov', 'sep', 'dec', 'oct', 'mar']
    cat_feat['poutcome'] = ['unknown3', 'other', 'success', 'failure']
    
    newList = []
    
    for key in alist:
        if key in numeric_feat:
            newList.append(alist[key])
        else:
            for ele in cat_feat[key]:
                if alist[key] == ele:
                    newList.append(1)
                else:
                    newList.append(0)
        
    return pd.Series(newList, index = newFeat)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', result = '')

@app.route('/form', methods = ['GET', 'POST'])
def form():
    mktform = MarketForm()
    if mktform.validate_on_submit():
        alist = {}
        idx = 0
        for ele in mktform:
            if idx >= 16:
                break
            alist[ele.name] = ele.data
            idx += 1
        data = processedFeature(alist)
        to_predict = np.array(data).reshape(1, -1)
        classifier = joblib.load('bankClassifier.pkl')
        prediction = classifier.predict(to_predict)
        '''
        to_print = ''
        if prediction[0] == 0:
            to_print = 'The client will not subscribed the term deposit'
        else:
            to_print = 'The Client will subscribed the term deposit'
        flash('{}'.format(to_print))
        '''
        return render_template('index.html', result = prediction[0])
    return render_template('form.html', form = mktform)
