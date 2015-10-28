from flask import Flask

from data_conversion import get_ward_data


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    get_ward_data()
    return "HELLLO"


if __name__ == "__main__":
    app.run(debug=1)
