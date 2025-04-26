from flask import Flask, render_template
import os

app = Flask(__name__)

LOG_FILE = "log.txt"

@app.route('/')
def index():
    logs = ""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = f.read()
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
