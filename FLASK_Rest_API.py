from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from Streamlit

latest_data = {}

@app.route('/predict', methods=['POST'])
def receive_data():
    global latest_data
    content = request.json
    content["timestamp"] = datetime.datetime.now().isoformat()
    latest_data = content
    print("Received data:", content)
    return jsonify({"status": "Data received"}), 200

@app.route('/data', methods=['GET'])
def send_data():
    if latest_data:
        return jsonify(latest_data)
    else:
        return jsonify({"message": "No data available"}), 404

if __name__ == '__main__':
    app.run(debug=True)
