from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    print(request.method)
    return render_template("index.html")


@app.route("/form/")
def form():
    return render_template("form.html")


@app.route("/result/", methods=["POST"])
def result():
    # request.args only works for GET request
    # print(request.args)  # dictionary

    # username = request.args["username"]
    # email = request.args["email"]
    # message = request.args["message"]

    # request.form only works for POST request
    print(request.form) # dictionary

    username = request.form["username"]
    email = request.form["email"]
    message = request.form["message"]

    return render_template(
        "result.html",
        username=username,
        email=email,
        message=message)


if __name__ == "__main__":
    app.run(debug=True)
