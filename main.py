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
        flights = data.get('data', [])
        return render_template_string("""
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <title>Flight Data</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        background-color: #f4f4f9;
                    }
                    h1 {
                        color: #333;
                    }
                    .flight {
                        background-color: #fff;
                        padding: 10px;
                        border: 1px solid #ddd;
                        border-radius: 5px;
                        margin-bottom: 20px;
                    }
                    .flight h2 {
                        margin-top: 0;
                    }
                </style>
                <script>
                    function updateData() {
                        fetch('/update')
                            .then(response => response.json())
                            .then(data => {
                                const flightsContainer = document.getElementById('flights-container');
                                flightsContainer.innerHTML = '';
                                data.flights.forEach(flight => {
                                    const flightDiv = document.createElement('div');
                                    flightDiv.className = 'flight';
                                    flightDiv.innerHTML = `
                                        <h2>Flight: ${flight.flight.iata} (${flight.flight.number})</h2>
                                        <p><strong>Airline:</strong> ${flight.airline.name}</p>
                                        <p><strong>Flight Date:</strong> ${flight.flight_date}</p>
                                        <p><strong>Flight Status:</strong> ${flight.flight_status}</p>
                                        <h3>Departure</h3>
                                        <p><strong>Airport:</strong> ${flight.departure.airport}</p>
                                        <p><strong>Scheduled:</strong> ${flight.departure.scheduled}</p>
                                        <p><strong>Estimated:</strong> ${flight.departure.estimated}</p>
                                        <h3>Arrival</h3>
                                        <p><strong>Airport:</strong> ${flight.arrival.airport}</p>
                                        <p><strong>Scheduled:</strong> ${flight.arrival.scheduled}</p>
                                        <p><strong>Estimated:</strong> ${flight.arrival.estimated}</p>
                                    `;
                                    flightsContainer.appendChild(flightDiv);
                                });
                            });
                    }
                </script>
              </head>
              <body>
                <h1>Flight Data</h1>
                <button onclick="updateData()">Update</button>
                <div id="flights-container">
                {% for flight in flights %}
                <div class="flight">
                    <h2>Flight: {{ flight.flight.iata }} ({{ flight.flight.number }})</h2>
                    <p><strong>Airline:</strong> {{ flight.airline.name }}</p>
                    <p><strong>Flight Date:</strong> {{ flight.flight_date }}</p>
                    <p><strong>Flight Status:</strong> {{ flight.flight_status }}</p>
                    <h3>Departure</h3>
                    <p><strong>Airport:</strong> {{ flight.departure.airport }}</p>
                    <p><strong>Scheduled:</strong> {{ flight.departure.scheduled }}</p>
                    <p><strong>Estimated:</strong> {{ flight.departure.estimated }}</p>
                    <h3>Arrival</h3>
                    <p><strong>Airport:</strong> {{ flight.arrival.airport }}</p>
                    <p><strong>Scheduled:</strong> {{ flight.arrival.scheduled }}</p>
                    <p><strong>Estimated:</strong> {{ flight.arrival.estimated }}</p>
                </div>
                {% endfor %}
                </div>
              </body>
            </html>
        """, flights=flights)
    else:
        return f"Error: {response.status_code} - {response.text}", response.status_code

@app.route('/update')
def update_flight_data():
    url = "https://api.aviationstack.com/v1/flights"
    params = {
        "access_key": "b042372742fb35942698bd9f5c97205d",
        "limit": 100,
        "offset": 0,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        flights = data.get('data', [])
        return jsonify(flights=flights)
    else:
        return jsonify(error=f"Error: {response.status_code} - {response.text}"), response.status_code

if __name__ == '__main__':
    app.run(debug=True)