from flask import Flask, render_template

app = Flask(__name__)

model ="Shreya"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    return render_template('result.html', message="This message came from Flask!",model=model)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    