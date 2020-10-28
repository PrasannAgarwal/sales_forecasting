import pred
from flask import Flask, request
from flask_restful import Resource, Api
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

app = Flask(__name__)
api = Api(app)

class fc(Resource):
    def get(self, first_number, second_number):
        return {pred.sales_forecast(first_number,second_number)}
    
api.add_resource(fc, '/4cast/<first_number>/<second_number>')

if __name__=='__main__':
    app.run()