import os
from flask import Flask, request, jsonify, render_template
from util import get_location_names, load_artifacts, price_prediction

# Define correct paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATE_DIR = os.path.join(BASE_DIR, "client/templates")
STATIC_DIR = os.path.join(BASE_DIR, "client/static")

# Configure Flask app
app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)

@app.route('/')
def home():
    return render_template("app.html")

@app.route('/get_location_names', methods=['GET'])
def get_location():
    locations = get_location_names()
    return jsonify({'locations': locations}), 200

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.get_json()

        total_sqft = float(data.get('total_sqft', 0))
        location = data.get('location', '').strip()
        bhk = int(data.get('bhk', 0))
        bath = int(data.get('bath', 0))

        if total_sqft <= 0 or not location or bhk <= 0 or bath <= 0:
            return jsonify({'error': 'Invalid input'}), 400

        estimated_price = price_prediction(location, total_sqft, bhk, bath)
        return jsonify({'estimated_price': round(estimated_price, 2)}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Loading model artifacts...")
    load_artifacts()
    app.run(debug=True)
