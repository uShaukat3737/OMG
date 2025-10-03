from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "☁️ Welcome to Project OMG - Cloud System API is running!"

@app.route("/api/resource", methods=["GET"])
def get_resource():
    return jsonify({
        "id": 1,
        "name": "Virtual Cloud Resource",
        "status": "active",
        "region": "us-east-1"
    })

@app.route("/api/resource", methods=["POST"])
def create_resource():
    data = request.json
    data["id"] = 100  # Simple demo ID
    return jsonify({
        "message": "Resource created successfully",
        "resource": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)