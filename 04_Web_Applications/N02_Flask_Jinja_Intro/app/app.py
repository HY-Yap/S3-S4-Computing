from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/about/<name>/")
def about(name):
    return render_template(
        "about.html", 
        name=name,
        age=16)

@app.route('/<int:i>/<float:f>/<s>')
def test_variables(i, f, s):
    return f'You entered int: {i}, float: {f}, str: {s}.'

if __name__ == "__main__":
    app.run(debug=True)