from flask import Flask, jsonify
from database.personas import personas

app = Flask(__name__)


@app.route('/personas', methods=['GET'])
def get_personas():
    return jsonify({"personas":personas})

if __name__ == "_main_":
    app.run(debug=True,port=5000)