from flask import Flask, render_template, jsonify
from datetime import datetime 
import requests
import json
from CityData import CityData
from utils import get_data



app = Flask(__name__)


response = get_data('https://data.cityofnewyork.us/resource/g9ub-hrve.json')

cityData = CityData(response)

@app.route('/phaseCounts')
def phases_of_projects():
    phases = cityData.phase_of_projects_counts()
    return jsonify(phases)

@app.route('/dates')
def dateCompletion():
    ordered_data = cityData.dateCompletion()
    return jsonify(ordered_data)




@app.route('/')
def index():

    sumProjCost = cityData.sum_total_of_projects()

    return render_template('index.html', data=cityData.all_data(), totalCost=sumProjCost)



if __name__ == "__main__":

    app.run(debug=True)

