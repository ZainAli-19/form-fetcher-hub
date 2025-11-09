from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app, origins=[
    "https://form-fetcher-hub.lovable.app",
    "https://form-fetcher-hub.zainlion999.workers.dev"
])

CSV_FILE = "submissions.csv"

# Ensure CSV exists with headers
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["name", "age", "email"])
    df.to_csv(CSV_FILE, index=False)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend is running successfully!"})

@app.route("/submit", methods=["POST"])
def submit_form():
    try:
        data = request.get_json()
        name = data.get("name")
        age = data.get("age")
        email = data.get("email")

        if not name or not age or not email:
            return jsonify({"error": "Missing one or more fields"}), 400

        # Append to CSV
        df = pd.DataFrame([[name, age, email]], columns=["name", "age", "email"])
        df.to_csv(CSV_FILE, mode="a", index=False, header=False)

        return jsonify({
            "message": "Form submission successful!",
            "data": {"name": name, "age": age, "email": email}
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/submissions.csv", methods=["GET"])
def get_csv():
    """Allow fetching the CSV file"""
    try:
        return send_file(CSV_FILE, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
