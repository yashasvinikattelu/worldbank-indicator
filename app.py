from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country = request.form['country']
        indicator = request.form['indicator']
        years = int(request.form['years'])

        api_url = f'https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page=100'

        response = requests.get(api_url)
        if response.status_code == 200:
            try:
                data = response.json()
                records = data[1]
                # Sort by most recent and slice based on user input
                results = [{
                    'year': item['date'],
                    'value': item['value']
                } for item in records if item['value'] is not None]

                results = sorted(results, key=lambda x: x['year'], reverse=True)[:years]

                return render_template('results.html', results=results, country=country, indicator=indicator)
            except Exception as e:
                return render_template('results.html', error="No data found or bad response.")
        else:
            return render_template('results.html', error=f"API request failed. Status code: {response.status_code}")
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
