from flask import render_template,request
import requests
from program import app

@app.route('/')
@app.route('/covid',methods=['GET','POST'])
def covid():
    covid_list = []
    country = ''
    if request.method=='POST' and 'nation'in request.form:
        country = request.form.get('nation')
        covid_list = get_numbers(country)
    return render_template('covid.html',covid_list=covid_list,country=country)

def get_numbers(country):
    covid_list = []
    r = requests.get("https://covid-19.dataflowkit.com/v1/"+country)
    nation_data = r.json()
    
    covid_list.append(nation_data["Total Cases_text"])
    covid_list.append(nation_data["Total Deaths_text"])
    covid_list.append(nation_data["Total Recovered_text"])
    
    return covid_list
