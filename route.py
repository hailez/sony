from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
API_URL = "https://www.travel-advisory.info/api"

@app.route('/health')
def health():
    return "Service is healthy", 200

@app.route('/diag')
def diag():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return jsonify({"api_status": {"code": 200, "status": "ok"}}), 200
    except Exception as e:
        return jsonify({"api_status": {"code": 500, "status": "error", "message": str(e)}}), 500
    
@app.route('/convert', methods=['POST'])
def convert():
    country_code = request.json.get('country_code')
    if not country_code:
        return jsonify({"error": "Missing 'country_code' in request data"}), 400

    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        
        if "data" in data and country_code in data["data"]:
            country_name = data["data"][country_code]["name"]
            return jsonify({"country_name": country_name}), 200
        else:
            return jsonify({"error": "Country code not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
