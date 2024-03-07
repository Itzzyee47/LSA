from flask import Flask, render_template, jsonify, request, url_for
from waitress import serve


app = Flask(__name__)

@app.route("/")
def chat():
    return render_template("base.html")

if __name__ =="__main__":
    app.run(debug=True, port=5000)
    