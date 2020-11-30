from flask import Flask, render_template

app = Flask(__name__)

# Fake Comment


@app.route('/')
def toIndex():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=0000, port=5000)
