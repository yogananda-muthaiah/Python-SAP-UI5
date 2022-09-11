import os

from flask import Flask, render_template, make_response, send_from_directory

app = Flask(__name__)

# Render index.html initially
@app.route('/')
def render_index():
    return render_template('index.html')


port = int(os.getenv("PORT", 0))
if __name__ == '__main__':
    if port != 0:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(debug=True)
