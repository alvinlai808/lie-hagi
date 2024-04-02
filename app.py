from flask import Flask, render_template, request, redirect, url_for
import json
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/forecast', methods = ['POST'])
def get_forecast():
    state_code = request.form['state']
    response = requests.get(f'https://api.weather.gov/alerts/active?area={state_code}').json()
    return render_template('forecast.html', 
                           state=request.form['state'],
                           forecast=response)


app.run(debug=True, host='localhost', port='8080')