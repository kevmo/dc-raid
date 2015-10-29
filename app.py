from flask import Flask, render_template, jsonify

from data_conversion import get_ward_data


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    wards = get_ward_data()
    for ward in wards:
        print ward
    return render_template("index.html")

@app.route("/ward-data", methods=["GET"])
def ward_data():
    data = get_ward_data()
    return jsonify([ward.serialize() for ward in data])


if __name__ == "__main__":
    app.run(debug=1)
