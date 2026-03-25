from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

@app.route("/")
def home():
    return "Go to /gael"

@app.route("/gael")
def gael():
    return render_template("template.html")

if __name__ == "__main__":
    app.run(debug=True)