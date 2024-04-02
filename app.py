from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/forecast', methods = ['POST'])
def get_forecast():
    state_code = request.form['states']
    response = requests.get(f'https://api.weather.gov/alerts/active?area={state_code}').json()
    return render_template('forecast.html', 
                           state=request.form['states'],
                           forecast=response)


app.run(debug=True, host='localhost', port='8080')