from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your Google Maps API Key
GOOGLE_MAPS_API_KEY = 'AIzaSyCDa7FzfmNAF2Shcx9HqRY_rpEPpAE0fkQ'

@app.route('/get-route-estimation', methods=['POST'])
def get_route_estimation():
    # Extract start and end locations from the request body
    data = request.get_json()
    origin = data.get('origin')  # Starting point
    destination = data.get('destination')  # Ending point
    mode = data.get('mode', 'driving')  # Mode of transport (default: driving)

    if not origin or not destination:
        return jsonify({"error": "Origin and Destination are required"}), 400

    # Prepare the API request URL for Google Maps Directions API
    url = "https://maps.googleapis.com/maps/api/directions/json"

    # Set parameters for the Google Maps API request
    params = {
        'origin': origin,
        'destination': destination,
        'mode': mode,
        'key': GOOGLE_MAPS_API_KEY
    }

    try:
        # Send the request to the Google Maps Directions API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        directions_data = response.json()

        # Return the directions data from Google Maps API
        return jsonify(directions_data), 200

    except requests.RequestException as e:
        return jsonify({"error": f"Failed to retrieve route estimations: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
