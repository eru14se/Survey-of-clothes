from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

survey_results = []

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        age = request.form['age']
        priorities = {
            "1st Priority": request.form['priority1'],
            "2nd Priority": request.form['priority2'],
            "3rd Priority": request.form['priority3'],
            "4th Priority": request.form['priority4'],
        }
        survey_results.append({"Age": age, **priorities})

    return render_template('survey.html')

@app.route('/results')
def results():
    df = pd.DataFrame(survey_results)
    age_groups = {}
    for age_group in ["Elementary", "Teen", "Adult"]:
        age_groups[age_group] = df[df['Age'] == age_group]

    return render_template('results.html', age_groups=age_groups)

if __name__ == '__main__':
    app.run(debug=True)