#!/usr/bin/env python
# coding: utf-8

# In[18]:


from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('xgboost.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        Area=request.form['Area']
        INT_SQFT = int(request.form['INT_SQFT'])
        DIST_MAINROAD = int(request.form['DIST_MAINROAD'])
        N_BEDROOM = int(request.form['DIST_MAINROAD'])
        N_BATHROOM = int(request.form['N_BATHROOM'])
        N_ROOM = int(request.form['N_ROOM'])
        SALE_COND = request.form['SALE_COND']
        PARK_FACIL = request.form['PARK_FACIL']
        BUILDTYPE = request.form['BUILDTYPE']
        STREET = request.form['STREET']
        
        if SALE_COND=='abnormal':
            SALE_COND=0
        elif SALE_COND=='family':
            SALE_COND=2
        elif SALE_COND=='partial':
            SALE_COND=4
        elif SALE_COND=='adjLand':
            SALE_COND=1
        elif SALE_COND=='normal sale':
            SALE_COND=3
            
        if PARK_FACIL =='yes':
            PARK_FACIL=1
        elif PARK_FACIL =='no':
            PARK_FACIL=0
            
        if BUILDTYPE =='house':
            BUILDTYPE =1
        elif BUILDTYPE =='others':
            BUILDTYPE =2
        elif BUILDTYPE =='commercial':
            BUILDTYPE =0
            
        if STREET =='paved':
            STREET =2
        elif STREET =='gravel':
            STREET =0
        elif STREET =='no access':
            STREET =1
            
        if Area=='tnagar':
            Area=0
    
            MZZONE = 4.03
            QS_ROOMS = 3.54
            QS_BATHROOM = 3.50
            QS_BEDROOM = 3.52
            QS_OVERALL = 3.52
            Year_difference = 25.15
        elif Area=='anna nagar':
            Area=1
        
            MZZONE = 4.03
            QS_ROOMS = 3.54
            QS_BATHROOM = 3.47
            QS_BEDROOM = 3.47
            QS_OVERALL = 3.49
            Year_difference = 25.24
        elif Area=='adyar':
            Area=2
            
            MZZONE = 2.38
            QS_ROOMS = 3.50
            QS_BATHROOM = 3.50
            QS_BEDROOM = 3.49
            QS_OVERALL = 3.49
            Year_difference = 22.67
        elif Area=='kk nagar':
            Area=3
       
            MZZONE = 4.01
            QS_ROOMS = 3.55
            QS_BATHROOM = 3.52
            QS_BEDROOM = 3.51
            QS_OVERALL = 3.52
            Year_difference = 17.31
        elif Area=='velachery':
            Area=4
          
            MZZONE = 2.48
            QS_ROOMS = 3.52
            QS_BATHROOM = 3.50
            QS_BEDROOM = 3.46
            QS_OVERALL = 3.50
            Year_difference = 30.31
        elif Area=='karapakkam':
            Area=5
           
            MZZONE = 2.42
            QS_ROOMS = 3.49
            QS_BATHROOM = 3.48
            QS_BEDROOM = 3.49
            QS_OVERALL = 3.49
            Year_difference = 27.74
        elif Area=='chrompet':
            Area=6
           
            MZZONE = 4.03
            QS_ROOMS = 3.54
            QS_BATHROOM = 3.50
            QS_BEDROOM = 3.52
            QS_OVERALL = 3.52
            Year_difference = 25.15
        
        prediction=model.predict([[Area,INT_SQFT,DIST_MAINROAD,N_BEDROOM,N_BATHROOM,N_ROOM,SALE_COND,PARK_FACIL,BUILDTYPE,STREET,MZZONE,QS_ROOMS,QS_BATHROOM,QS_BEDROOM,QS_OVERALL,Year_difference]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Invalid Input")
        else:
            return render_template('index.html',prediction_text="You Can Sell The House at {}".format(output))
            
    else:
        return render_template('index.html')
if __name__=="__main__":
  
    app.run(debug=True)






