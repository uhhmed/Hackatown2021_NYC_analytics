from main import app




@app.route('/phaseCounts')
def phases_of_projects():
    phases = cityData.phase_of_projects_counts()
    return jsonify(phases)

@app.route('/dates')
def dateCompletion():
    ordered_data = cityData.dateCompletion()
    return jsonify(ordered_data)


