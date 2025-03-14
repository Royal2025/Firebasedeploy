import functions_framework
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello from Firebase!"})

# Firebase Function ke liye wrapper
@functions_framework.http
def main(request):
    return app(request)
