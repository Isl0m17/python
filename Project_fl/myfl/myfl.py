from flask import Flask, render_template, url_for
app = Flask(__name__)

#Обработчик route с путем http://127.0.0.1:5000
@app.route("/")
def aaa():
    return render_template("aaa.html", title = "Python")

@app.route("/index")
def bbb():
    return render_template("bbb.html")

if __name__ == "__main__":
    app.run(debug = True)