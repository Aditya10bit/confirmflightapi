from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import config  # Import the config file

app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(config.Config)

# Initialize the MySQL extension
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM flights")  # Fetch all flights
    results = cur.fetchall()  # Fetch all results
    cur.close()

    flights = []
    for row in results:
        flight = {
            'flight_number': row[1],
            'departure_date': str(row[2]),
            'departure_time': str(row[3]),
            'origin': row[4],
            'destination': row[5],
            'available_seats': row[6],
            'company_name': row[7],
            'logo_url': row[8],
            'price': row[9]
        }
        flights.append(flight)

    return jsonify(flights)

# Search functionality: Filter flights by origin, destination, or departure date
@app.route('/search', methods=['GET'])
def search_flights():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    departure_date = request.args.get('departure_date')  # Format: 'YYYY-MM-DD'

    query = "SELECT * FROM flights WHERE 1=1"  # Start with a query that always returns true
    params = []

    # Add filters dynamically if provided
    if origin:
        query += " AND origin = %s"
        params.append(origin)
    if destination:
        query += " AND destination = %s"
        params.append(destination)
    if departure_date:
        query += " AND departure_date = %s"
        params.append(departure_date)

    cur = mysql.connection.cursor()
    cur.execute(query, tuple(params))  # Execute the query with dynamic parameters
    results = cur.fetchall()
    cur.close()

    flights = []
    for row in results:
        flight = {
            'flight_number': row[1],
            'departure_date': str(row[2]),
            'departure_time': str(row[3]),
            'origin': row[4],
            'destination': row[5],
            'available_seats': row[6],
            'company_name': row[7],
            'logo_url': row[8],
            'price': row[9]
        }
        flights.append(flight)

    return jsonify(flights)

if __name__ == '__main__':
    app.run(debug=True)
