#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, render_template, request     # public functions


# # request is to request from the internet

# In[4]:


app = Flask(__name__)


# In[5]:


import joblib

@app.route('/',methods = ['GET','POST'])       # @ is a decorator
def index():
    if request.method == 'POST':
        rates = float(request.form.get('rates'))
        print(rates)
        model1 = joblib.load("regression_DBS")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree_DBS")
        r2 = model2.predict([[rates]])
        return render_template('index.html',result1 = r1 , result2 = r2)
    else:
        return render_template('index.html',result1 = 'waiting', result2 = 'waiting')   # before you press enter, flask will redirect you here


# In[6]:


if __name__ == "__main__":     # if this programme is yours then run, else don't run
    app.run()


# # localhost is 127.0.0.1, everything is still local
# # flask uses 5000, can try 1111 for mac
# # jupyter uses 8888
# # in cloud, everything is equal; everything controlled by heroku

# In[ ]:




