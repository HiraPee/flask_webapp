from flask import Flask, render_template, jsonify, request, make_response
app = Flask(__name__)
from flask_cors import CORS

import text2wordcloud as t2w
import base64

CORS(app)  # CORS有効化

@app.route('/SPA')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    return jsonify({'message': 'Hello, world'})


@app.route('/api/', methods=["POST"])
def post():
    text = request.form["text"]
    print(request.form)
    img_root = t2w.create_spa_wordcloud_ja(text)
    with open('./templates/spa.png', "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode('utf-8')

    #result = {'img':img_root}
    result = {'img':img_base64}
    #print(result)
    return jsonify(result)
    #return make_response(result)


@app.route('/get/', methods=['GET'])
def get():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
