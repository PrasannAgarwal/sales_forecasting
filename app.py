import pred
import flask
import flask_restful
# from flask import Flask, request
# from flask_restful import Resource, Api
import math
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from pandas.plotting import register_matplotlib_converters
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
register_matplotlib_converters()
from time import time
from math import sqrt
from multiprocessing import cpu_count
from joblib import Parallel
from joblib import delayed
from warnings import catch_warnings
from warnings import filterwarnings
from sklearn.metrics import mean_squared_error

app = flask.Flask(__name__, template_folder='templates')
# api = Api(app)

@app.route('/', methods=['GET','POST'])
def main():
	if (flask.request.method == 'GET'):
		return (flask.render_template('main.html'))
	if (flask.request.method == 'POST'):
		item_id=flask.request.form['item_id']
		firm_id=flask.request.form['firm_id']
		res=pred.sales_forecast(item_id,firm_id)
		return flask.render_template('main.html',original_input={'item_id':item_id,'firm_id':firm_id},result=res,)

# class fc(Resource):
#     def get(self, first_number, second_number):
#         return {'data' :pred.sales_forecast(first_number,second_number)}
    
# api.add_resource(fc, '/4cast/<first_number>/<second_number>')



if __name__=='__main__':
    app.run()