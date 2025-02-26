from flask import Flask, jsonify, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def get_flight_data():
    url = "https://api.aviationstack.com/v1/flights"
    params = {
        "access_key": "b042372742fb35942698bd9f5c97205d",
        "limit": 100,
        "offset": 0,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return render_template_string("""
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <title>Flight Data</title>
              </head>
              <body>
                <h1>Flight Data</h1>
                <pre>{{ data | tojson(indent=2) }}</pre>
              </body>
            </html>
        """, data=data)
    else:
        return f"Error: {response.status_code} - {response.text}", response.status_code

if __name__ == '__main__':
    app.run(debug=True)